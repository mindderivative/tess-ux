#!/usr/bin/env python3
"""Recompute the WCAG 2.2 contrast ratios stated in the Tesserae UX vault.

Usage: python3 tools/contrast_check.py [vault root] [--json]

Standard library only. Exit code 1 when a stated ratio differs from the
recomputed ratio by more than 0.05, or a pair falls below its required limit.

Sources read:
  - "20 Foundations and Tokens/Colour Roles.md": the role table (light and dark
    standard), the medium and high contrast table, the required-pairs tables
    (six schemes), the shell 12-role table and its measured pairs;
  - every other note: lines of the form `A` on|over|against `B` with a stated
    ratio (N:1 or N to 1, optionally tagged light or dark) or a limit
    ("at least N:1"), checked against the standard light and dark schemes;
  - computed extras: scrollbar thumb at 0.70 over the surface roles, the scrim
    band at 0.60 with on_scrim, the focus ring over the surface roles.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

COLOUR_NOTE = "20 Foundations and Tokens/Colour Roles.md"
SCHEMES = ["light_std", "dark_std", "light_med", "dark_med", "light_high", "dark_high"]
TOLERANCE = 0.05
SURFACES = ["surface", "surface_dim", "surface_bright", "surface_container_lowest", "surface_container_low",
            "surface_container", "surface_container_high", "surface_container_highest"]
THUMB_REST = 0.70  # ADR-0012 as amended by OQ-32
KNOWN_VIOLATIONS_FILE = "tools/known_violations.json"
SKIP_DIRS = {".git", ".obsidian", ".claude", ".copilot", "tools", "graphify-out", "_templates"}


def hex_rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def lum(rgb: tuple[float, float, float]) -> float:
    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b) -> float:
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def composite(fg, alpha: float, bg):
    return tuple(f * alpha + g * (1 - alpha) for f, g in zip(fg, bg))


class Report:
    def __init__(self):
        self.rows: list[dict] = []

    def add(self, section: str, sev: str, where: str, msg: str) -> None:
        self.rows.append({"section": section, "severity": sev, "where": where, "message": msg})


def parse_roles(text: str):
    """Return {scheme: {role: rgb}} and the ordered role list."""
    roles: dict[str, dict[str, tuple]] = {s: {} for s in SCHEMES}
    lines = text.split("\n")
    mode = None
    for line in lines:
        if line.startswith("### Role set and baseline"):
            mode = "std"
            continue
        if line.startswith("### Medium and high contrast"):
            mode = "mh"
            continue
        if line.startswith("##") and mode and not line.startswith("### Role") and not line.startswith("### Medium"):
            mode = None if mode else mode
        if mode == "std":
            m = re.match(r"^\|\s*`([a-z_]+)`\s*\|.*\|\s*(#[0-9A-Fa-f]{6})\s*\|\s*(#[0-9A-Fa-f]{6})\s*\|\s*$", line)
            if m:
                roles["light_std"][m.group(1)] = hex_rgb(m.group(2))
                roles["dark_std"][m.group(1)] = hex_rgb(m.group(3))
        elif mode == "mh":
            m = re.match(r"^\|\s*`([a-z_]+)`\s*\|" + r"\s*(#[0-9A-Fa-f]{6})\s*\|" * 4 + r"\s*$", line)
            if m:
                for s, g in zip(["light_med", "light_high", "dark_med", "dark_high"], m.groups()[1:]):
                    roles[s][m.group(1)] = hex_rgb(g)
    return roles


def parse_pair_tables(text: str):
    """Rows of the required-pairs tables: (line, role_a, role_b, nontext, [6 ratios])."""
    out = []
    nontext = False
    in_pairs = False
    for i, line in enumerate(text.split("\n")):
        if line.startswith("### Required pairs"):
            in_pairs = True
            continue
        if in_pairs and line.startswith("##"):
            in_pairs = False
        if not in_pairs:
            continue
        if line.startswith("Non-text pairs"):
            nontext = True
        m = re.match(r"^\|\s*`([a-z_]+)`\s+on\s+`([a-z_]+)`\s*\|(.*)\|\s*$", line)
        if m:
            vals = [float(x) for x in re.findall(r"\d+\.\d+", m.group(3))]
            if len(vals) == 6:
                out.append((i + 1, m.group(1), m.group(2), nontext, vals))
    return out


def parse_shell(text: str):
    """Shell role table and measured pair rows."""
    shell: dict[str, list[str]] = {}
    pairs = []
    sec = None
    for i, line in enumerate(text.split("\n")):
        if line.startswith("| Shell role"):
            sec = "roles"
            continue
        if line.startswith("| Pair (shell role names)"):
            sec = "pairs"
            continue
        if not line.startswith("|"):
            if line.strip() == "" and sec == "pairs" and pairs:
                sec = None
            continue
        if sec == "roles":
            m = re.match(r"^\|\s*`\$color\.([a-z_]+)`\s*\|\s*([^|]+?)\s*\|", line)
            if m:
                vals = [v.strip() for v in m.group(2).split("/")]
                if len(vals) == 3:
                    shell[m.group(1)] = vals
        elif sec == "pairs":
            m = re.match(r"^\|\s*`([a-z_]+)`\s+on\s+`([a-z_]+)`(\s*\(non-text\))?\s*\|(.*)\|\s*$", line)
            if m:
                vals = [float(x) for x in re.findall(r"\d+\.\d+", m.group(4))]
                if len(vals) == 3:
                    pairs.append((i + 1, m.group(1), m.group(2), bool(m.group(3)), vals))
    return shell, pairs


def check_colour_note(root: Path, rep: Report):
    path = root / COLOUR_NOTE
    if not path.exists():
        rep.add("setup", "error", COLOUR_NOTE, "Colour Roles note not found")
        return None, {}
    text = path.read_text(encoding="utf-8")
    roles = parse_roles(text)
    for s in SCHEMES:
        if len(roles[s]) < 40:
            rep.add("setup", "error", COLOUR_NOTE, f"scheme {s}: only {len(roles[s])} roles parsed")
    n_std = len(roles["light_std"])
    rep.add("setup", "info", COLOUR_NOTE, f"parsed roles: " + ", ".join(f"{s} {len(roles[s])}" for s in SCHEMES))
    rows = parse_pair_tables(text)
    rep.add("setup", "info", COLOUR_NOTE, f"required-pairs rows parsed: {len(rows)}")
    for ln, a, b, nontext, vals in rows:
        for s, stated in zip(SCHEMES, vals):
            if a not in roles[s] or b not in roles[s]:
                rep.add("pairs", "error", f"{COLOUR_NOTE}:{ln}", f"{a} on {b} [{s}]: role missing from the role tables")
                continue
            got = ratio(roles[s][a], roles[s][b])
            if abs(got - stated) > TOLERANCE:
                rep.add("pairs", "error", f"{COLOUR_NOTE}:{ln}", f"{a} on {b} [{s}]: stated {stated:.2f}, computed {got:.2f}")
            limit = 3.0 if nontext else (7.0 if s.endswith("high") else 4.5)
            if got + 1e-9 < limit:
                rep.add("pairs", "error", f"{COLOUR_NOTE}:{ln}", f"{a} on {b} [{s}]: computed {got:.2f} is below the limit {limit}")
    # outline_variant claim
    for s, claim in (("light_std", 1.62), ("dark_std", 1.99)):
        got = ratio(roles[s]["outline_variant"], roles[s]["surface"])
        if abs(got - claim) > TOLERANCE:
            rep.add("pairs", "error", COLOUR_NOTE, f"outline_variant on surface [{s}]: stated {claim}, computed {got:.2f}")
    # shell table
    shell, spairs = parse_shell(text)
    rep.add("setup", "info", COLOUR_NOTE, f"shell roles parsed: {len(shell)}; shell pair rows: {len(spairs)}")
    for ln, a, b, nontext, vals in spairs:
        for k, (scheme, stated) in enumerate(zip(["Dark", "Light", "High_Contrast"], vals)):
            if a not in shell or b not in shell:
                rep.add("shell", "error", f"{COLOUR_NOTE}:{ln}", f"{a} on {b}: shell role missing")
                break
            fa, fb = shell[a][k], shell[b][k]
            inherited = False
            if fa == "inherits":
                fa, inherited = shell[a][0], True
            if fb == "inherits":
                fb, inherited = shell[b][0], True
            if not (re.fullmatch(r"#[0-9A-Fa-f]{6}", fa) and re.fullmatch(r"#[0-9A-Fa-f]{6}", fb)):
                continue
            got = ratio(hex_rgb(fa), hex_rgb(fb))
            note = " (inherited value taken from Dark)" if inherited else ""
            if abs(got - stated) > TOLERANCE:
                rep.add("shell", "warn" if inherited else "error", f"{COLOUR_NOTE}:{ln}",
                        f"{a} on {b} [{scheme}]: stated {stated:.2f}, computed {got:.2f}{note}")
            limit = 3.0 if nontext else 4.5
            if got + 1e-9 < limit:
                rep.add("shell", "warn" if inherited else "error", f"{COLOUR_NOTE}:{ln}", f"{a} on {b} [{scheme}]: computed {got:.2f} is below the limit {limit}{note}")
    return roles, shell


R = r"`([a-z_]+)`"
NOT_PAIR = r"(?! (?:\w+ )?(?:on|over|against) )"
ROLE_LIST = r"`[a-z_]+`(?:(?:, | and on | and | or )`[a-z_]+`" + NOT_PAIR + r")*"
PAIR = re.compile(r"(?P<xs>" + ROLE_LIST + r") (?P<kw>on|over|against)(?: each of)? (?P<ys>" + ROLE_LIST + r")")
RATIO = re.compile(r"(?<![\d.])(\d+(?:\.\d+)?)\s*(?::1|to 1)(?![\d])")


def shell_rgb(shell, role, k):
    v = shell.get(role, [None] * 3)[k]
    if v == "inherits" and k:
        v = shell[role][0]
    return hex_rgb(v) if v and re.fullmatch(r"#[0-9A-Fa-f]{6}", v) else None


def scan_notes(root: Path, roles, rep: Report, shell):
    light, dark = roles["light_std"], roles["dark_std"]
    n_pairs = n_stated = n_limits = 0
    for p in sorted(root.rglob("*.md")):
        parts = p.relative_to(root).parts
        if any(x in SKIP_DIRS or x.startswith(".") for x in parts[:-1]) or len(parts) == 1:
            continue
        rel = p.relative_to(root).as_posix()
        in_fence = False
        for i, line in enumerate(p.read_text(encoding="utf-8").split("\n")):
            if re.match(r"^\s*(```|~~~)", line):
                in_fence = not in_fence
                continue
            if in_fence or "|---" in line:
                continue
            if rel == COLOUR_NOTE and 150 <= i + 1 <= 250:
                continue  # pair tables are checked as tables
            matches = list(PAIR.finditer(line))
            if not matches:
                continue
            for k, m in enumerate(matches):
                xs = re.findall(R, m.group("xs"))
                ys = re.findall(R, m.group("ys"))
                if not all(r in light for r in xs + ys):
                    continue
                alpha_seg = re.search(r"\bat 0\.\d+\b", seg_all := line[m.end():(matches[k + 1].start() if k + 1 < len(matches) else len(line))])
                seg_end = matches[k + 1].start() if k + 1 < len(matches) else len(line)
                seg = line[m.end():seg_end]
                n_pairs += 1
                limit = None
                stated: list[tuple[float, str | None]] = []
                for rm in RATIO.finditer(seg):
                    val = float(rm.group(1))
                    before = seg[max(0, rm.start() - 14):rm.start()]
                    after = seg[rm.end():rm.end() + 16]
                    ctx = seg[max(0, rm.start() - 12):rm.start()]
                    if re.search(r"(at least|reach(?:es)?|meets?|above|of) $", before) or re.search(r"at least\s*$", before):
                        limit = limit if limit is not None else val
                        continue
                    scheme = None
                    if re.match(r"[\s,]*(in |is )?(light)\b", after, re.I) or re.search(r"in light\s*$", ctx):
                        scheme = "light"
                    elif re.match(r"[\s,]*(in |is )?(dark)\b", after, re.I) or re.search(r"in dark\s*$", ctx):
                        scheme = "dark"
                    stated.append((val, scheme))
                if limit is None:
                    # a limit stated later on the line applies to the pair too
                    tail = RATIO.search(line[seg_end:]) if False else None
                    lm = re.search(r"at least (\d+(?:\.\d+)?)\s*(?::1| to 1)", line[m.end():])
                    if lm:
                        limit = float(lm.group(1))
                for xr in xs:
                    for yr in ys:
                        if xr == yr:
                            continue
                        rl = ratio(light[xr], light[yr])
                        rd = ratio(dark[xr], dark[yr])
                        where = f"{rel}:{i + 1}"
                        for val, scheme in stated:
                            if alpha_seg:
                                continue  # a composited alpha colour, not the plain pair
                            n_stated += 1
                            if scheme == "light":
                                ok = abs(rl - val) <= TOLERANCE
                                msg = f"{xr} on {yr}: stated {val} in light, computed {rl:.2f}"
                            elif scheme == "dark":
                                ok = abs(rd - val) <= TOLERANCE
                                msg = f"{xr} on {yr}: stated {val} in dark, computed {rd:.2f}"
                            else:
                                if val in (3.0, 3, 4.5, 7.0, 7):
                                    continue  # a limit, not a measurement
                                ok = abs(rl - val) <= TOLERANCE or abs(rd - val) <= TOLERANCE
                                msg = f"{xr} on {yr}: stated {val} (no scheme named), computed {rl:.2f} light and {rd:.2f} dark"
                            if not ok and shell:
                                for k2, nm2 in ((0, "dark"), (1, "light")):
                                    a, b = shell_rgb(shell, xr, k2), shell_rgb(shell, yr, k2)
                                    if a and b and (scheme in (None, nm2)) and abs(ratio(a, b) - val) <= TOLERANCE:
                                        ok = True
                            if not ok:
                                rep.add("notes-stated", "error", where, msg)
                        if limit is not None:
                            n_limits += 1
                            for nm, got in (("light", rl), ("dark", rd)):
                                if got + 1e-9 < limit:
                                    rep.add("notes-limit", "error", where,
                                            f"{xr} on {yr}: requires at least {limit:g}, computed {got:.2f} in {nm} standard")
    rep.add("setup", "info", "vault", f"role pairs scanned in notes: {n_pairs}; stated ratios compared: {n_stated}; limits checked: {n_limits}")


def computed_extras(root: Path, roles, rep: Report):
    # scrollbar thumb at the rest opacity
    stated = {}
    sb = root / "30 Component Specifications" / "Scrollbar and Scroll Container.md"
    if sb.exists():
        m = re.search(r"at 0\.70 it is (\d+\.\d+) and (\d+\.\d+)", sb.read_text(encoding="utf-8"))
        if m:
            stated = {"dark_std": float(m.group(1)), "light_std": float(m.group(2))}
    for s in ("light_std", "dark_std", "light_high", "dark_high"):
        fg = roles[s]["on_surface_variant"]
        for surf in SURFACES:
            bg = roles[s][surf]
            got = ratio(composite(fg, THUMB_REST, bg), bg)
            sev = "info"
            msg = f"thumb on_surface_variant at {THUMB_REST:.2f} over {surf} [{s}]: {got:.2f}"
            if got < 3.0:
                sev, msg = "error", msg + " (below 3.0)"
            if surf == "surface" and s in stated and abs(got - stated[s]) > TOLERANCE:
                sev, msg = "error", msg + f"; the Scrollbar note states {stated[s]}"
            rep.add("thumb", sev, "computed", msg)
    # scrim band: on_scrim is not a Colour Roles role; ADR-0016 names it, taken as white
    scrim = roles["light_std"]["scrim"]
    for label, img in (("white image", (1, 1, 1)), ("mid-grey image", (0.5, 0.5, 0.5)), ("black image", (0, 0, 0))):
        band = composite(scrim, 0.60, img)
        got = ratio((1, 1, 1), band)
        sev = "info" if got >= 4.5 else "error"
        rep.add("scrim", sev, "computed", f"on_scrim (taken as #FFFFFF; not a role in Colour Roles) over scrim at 0.60 on a {label}: {got:.2f}"
                + ("" if got >= 4.5 else " (below 4.5)"))
    band = composite(scrim, 0.60, (1, 1, 1))
    got = ratio((1, 1, 1), band)
    if abs(got - 5.7) > TOLERANCE:
        rep.add("scrim", "error", "ADR-0016, Carousel, Image, Video Player", f"stated 5.7 over a white image, computed {got:.2f}")
    # scrim itself at 0.32 over surface (informational)
    for s in ("light_std", "dark_std"):
        bg = roles[s]["surface"]
        rep.add("scrim", "info", "computed", f"on_surface over surface under scrim 0.32 [{s}]: {ratio(roles[s]['on_surface'], composite(roles[s]['scrim'], 0.32, bg)):.2f}")
    # focus ring over the surface roles
    for s in SCHEMES:
        ring = roles[s]["secondary"]
        for surf in SURFACES:
            got = ratio(ring, roles[s][surf])
            sev = "info" if got >= 3.0 else "error"
            rep.add("focus-ring", sev, "computed", f"focus ring secondary over {surf} [{s}]: {got:.2f}" + ("" if got >= 3.0 else " (below 3.0)"))
    for s, claim in (("light_std", 6.0), ("dark_std", 10.9)):
        got = ratio(roles[s]["secondary"], roles[s]["surface"])
        if abs(got - claim) > 0.15:
            rep.add("focus-ring", "error", "20 Foundations and Tokens/Focus Ring.md:50",
                    f"stated about {claim} for secondary over surface [{s}], computed {got:.2f}")


def apply_known_violations(root: Path, rep: Report) -> None:
    """Downgrade errors that a project is known to violate (spec stays strict, project debt is listed).

    tools/known_violations.json is a list of objects: project, ac, section, match
    (the message must start with it), tracked (worklist id), reason. A matched
    error becomes a warning naming the project and the worklist id. An entry that
    no longer matches anything is reported as a warning so the table stays honest.
    """
    path = root / KNOWN_VIOLATIONS_FILE
    if not path.exists():
        return
    entries = json.loads(path.read_text(encoding="utf-8"))
    for e in entries:
        hit = False
        for r in rep.rows:
            if r["severity"] == "error" and r["section"] == e["section"] and r["message"].startswith(e["match"]):
                r["severity"] = "warn"
                r["message"] += f" [known violation by {e['project']}: {e['tracked']}, {e['ac']}]"
                hit = True
        if not hit:
            rep.add("known", "warn", KNOWN_VIOLATIONS_FILE, f"entry no longer matches an error, remove it: {e['match']} ({e['project']} {e['tracked']})")


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    as_json = "--json" in argv
    root = Path(args[0]).resolve() if args else Path(__file__).resolve().parent.parent
    rep = Report()
    roles, shell = check_colour_note(root, rep)
    if roles is not None and roles["light_std"]:
        scan_notes(root, roles, rep, shell)
        computed_extras(root, roles, rep)
    apply_known_violations(root, rep)
    errors = sum(1 for r in rep.rows if r["severity"] == "error")
    if as_json:
        json.dump({"root": str(root), "errors": errors, "rows": rep.rows}, sys.stdout, indent=1)
        print()
    else:
        print(f"Contrast check under {root}")
        sections: dict[str, list[dict]] = {}
        for r in rep.rows:
            sections.setdefault(r["section"], []).append(r)
        for sec, rows in sections.items():
            e = sum(1 for r in rows if r["severity"] == "error")
            w = sum(1 for r in rows if r["severity"] == "warn")
            print(f"\n== {sec}: {e} error, {w} warn, {len(rows) - e - w} info ==")
            for r in rows:
                print(f"{r['severity'].upper():5} {r['where']}: {r['message']}")
        print(f"\nResult: {'FAIL' if errors else 'OK'} ({errors} errors)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
