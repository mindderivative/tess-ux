#!/usr/bin/env python3
"""Lint the Tesserae UX vault.

Usage: python3 tools/lint_vault.py [vault root] [--json]

Standard library only. Exit code 1 when any finding has severity "error".
Checks (see "60 Quality/Vault Lint.md"):
  FM      frontmatter keys, status, type
  LINK    wikilinks resolve (title, file name, alias)
  ORPHAN  every note is linked; every folder has its index note
  COMP    component notes carry all template sections in order
  AC      acceptance criteria format, ids, check type, pass condition, citations
  TOKEN   token names exist in the foundation notes
  MD      markdown rules: no emoji, no bold or italic touching a code span, no raw HTML
  PRIV    no home-directory paths or secrets
  NV      #needs-verification tags counted and listed
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REQUIRED_KEYS = ["title", "type", "status", "owner", "created", "updated", "tags", "related", "depends_on"]
STATUSES = {"draft", "proposed", "accepted", "stable", "superseded", "research", "active", "approved", "rejected", "done"}
TYPES = {
    "adr", "audit", "chapter", "component", "dashboard", "foundation", "glossary", "index",
    "inventory", "pattern", "plan", "quality", "questions", "register", "request", "research",
    "template", "tokens", "adoption",
}
CHECK_TYPES = [
    "token test", "geometry check", "pixel check", "contrast script",
    "scripted input", "at tree assertion", "review", "static check",
]
SKIP_DIRS = {".git", ".obsidian", ".claude", ".copilot", "tools", "graphify-out", "node_modules", "_templates"}
COMPONENT_DIR = "30 Component Specifications"
DIM_SECTION = "Dimensions and defaults"
DIMENSIONS_ENFORCED = False  # set True when every component note carries the table
DIM_COLUMNS = ["Part", "Property", "Token", "Default", "Compact", "Dense", "Source", "Settable"]
SETTABLE_PROJECTS = ["tess-ui", "tess-shell", "tre"]
SETTABLE_VALUE = re.compile(r"^(yes\b.*|via\s+\S.*|hardcoded in tre.*|no hook.*|n/a:\s*.{8,})$", re.I)
DIM_PROPS = {"height", "min width", "min height", "padding", "margin", "gap", "border width", "border color",
             "corner radius", "font", "icon size", "elevation"}
DIM_REQUIRED = ["height", "padding", "margin", "gap", "border width", "border color", "corner radius", "font",
                "icon size", "elevation"]
FOUNDATION_DIR = "20 Foundations and Tokens"
TOKEN_DEFINING_EXTRA = ["30 Component Specifications/Scrollbar and Scroll Container.md"]

WIKILINK = re.compile(r"!?\[\[([^\]\n]+?)\]\]")
CODESPAN = re.compile(r"(`+)(.+?)\1")
AC_LINE = re.compile(r"^\s*-\s*\[(.)\]\s*(AC-([A-Z0-9]+(?:-[A-Z0-9]+)*)-(\d+))(.*)$")
AC_CITE = re.compile(r"(?<![A-Za-z0-9-])AC-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d+\b")
ROLE_SHAPE = re.compile(
    r"^(?:on_|inverse_on_)?(?:primary|secondary|tertiary|error|surface|outline|background|scrim|shadow|inverse)(?:_[a-z_]+)?$"
)
HTML_TAG = re.compile(r"</?[A-Za-z][A-Za-z0-9-]*(?:\s[^<>]*)?/?>|<!--")
SECRETS = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"), re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"), re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[bp]-[A-Za-z0-9-]{10,}"), re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9/+_-]{16,}"),
]
PATH_PATTERNS = [re.compile(r"/home/[A-Za-z0-9_.-]+"), re.compile(r"/Users/[A-Za-z0-9_.-]+"),
                 re.compile(r"[A-Za-z]:\\Users\\")]
EMOJI_WARN = {0x2713, 0x2714, 0x2717, 0x2718}


def is_emoji(cp: int) -> bool:
    if cp in (0xFE0F, 0x200D, 0x20E3):
        return True
    return (0x1F000 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x27BF or cp in (0x2B50, 0x2B55, 0x2B1B, 0x2B1C)
            or 0x231A <= cp <= 0x231B or 0x23E9 <= cp <= 0x23FA or cp in (0x25B6, 0x25C0)
            or 0x25FB <= cp <= 0x25FE or cp in (0x2934, 0x2935, 0x3030, 0x303D, 0x3297, 0x3299))


class Note:
    def __init__(self, root: Path, path: Path):
        self.path = path
        self.rel = path.relative_to(root).as_posix()
        self.stem = path.stem
        self.text = path.read_text(encoding="utf-8", errors="replace")
        self.lines = self.text.split("\n")
        self.fm: dict[str, str] = {}
        self.fm_keys: list[tuple[str, int]] = []
        self.has_fm = False
        self.kind: list[str] = []  # 'fm' | 'fence' | 'body' per line
        self._parse()

    def _parse(self) -> None:
        n = len(self.lines)
        fm_end = -1
        if n and self.lines[0].strip() == "---":
            for i in range(1, n):
                if self.lines[i].strip() == "---":
                    fm_end = i
                    break
        if fm_end > 0:
            self.has_fm = True
            for i in range(1, fm_end):
                m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", self.lines[i])
                if m:
                    self.fm[m.group(1)] = m.group(2).strip()
                    self.fm_keys.append((m.group(1), i + 1))
        in_fence = False
        fence_char = ""
        for i, line in enumerate(self.lines):
            if i <= fm_end and fm_end > 0:
                self.kind.append("fm")
                continue
            m = re.match(r"^\s*(```+|~~~+)", line)
            if m:
                if not in_fence:
                    in_fence, fence_char = True, m.group(1)[0]
                    self.kind.append("fence")
                    continue
                if m.group(1)[0] == fence_char:
                    in_fence = False
                    self.kind.append("fence")
                    continue
            self.kind.append("fence" if in_fence else "body")

    def fm_scalar(self, key: str) -> str:
        return self.fm.get(key, "").strip().strip("'\"")

    def aliases(self) -> list[str]:
        raw = self.fm.get("aliases", "")
        out = []
        if raw.startswith("["):
            out += [a.strip().strip("'\"") for a in raw.strip("[]").split(",") if a.strip()]
        elif raw:
            out.append(raw.strip("'\""))
        else:
            # block list under aliases:
            for key, ln in self.fm_keys:
                if key == "aliases":
                    j = ln
                    while j < len(self.lines) and re.match(r"^\s*-\s+", self.lines[j]):
                        out.append(re.sub(r"^\s*-\s+", "", self.lines[j]).strip().strip("'\""))
                        j += 1
        return [a for a in out if a]

    def title(self) -> str:
        return self.fm_scalar("title")

    def masked(self, i: int) -> str:
        """Line with inline code span contents blanked (same length)."""
        return CODESPAN.sub(lambda m: " " * len(m.group(0)), self.lines[i])


class Findings:
    def __init__(self):
        self.items: list[dict] = []

    def add(self, check: str, sev: str, note: Note | str, line: int, msg: str) -> None:
        rel = note.rel if isinstance(note, Note) else note
        self.items.append({"check": check, "severity": sev, "file": rel, "line": line, "message": msg})


def collect_notes(root: Path) -> list[Note]:
    notes = []
    for p in sorted(root.rglob("*.md")):
        parts = p.relative_to(root).parts
        if any(part in SKIP_DIRS or part.startswith(".") for part in parts[:-1]):
            continue
        if len(parts) == 1:  # README.md etc. at the root are not vault notes
            continue
        notes.append(Note(root, p))
    return notes


# ---- check 1: frontmatter -------------------------------------------------
def check_frontmatter(notes: list[Note], f: Findings) -> None:
    for n in notes:
        if not n.has_fm:
            f.add("FM", "error", n, 1, "no frontmatter block")
            continue
        for key, ln in n.fm_keys:
            if key != key.lower():
                f.add("FM", "error", n, ln, f"frontmatter key '{key}' is not lowercase")
        keys = {k.lower() for k, _ in n.fm_keys}
        for req in REQUIRED_KEYS:
            if req not in keys:
                f.add("FM", "error", n, 1, f"missing frontmatter key '{req}'")
        st = n.fm_scalar("status")
        if "status" in keys and st not in STATUSES:
            f.add("FM", "error", n, dict(n.fm_keys).get("status", 1), f"invalid status '{st}' (allowed: {', '.join(sorted(STATUSES))})")
        ty = n.fm_scalar("type")
        if "type" in keys and ty not in TYPES:
            f.add("FM", "error", n, dict(n.fm_keys).get("type", 1), f"invalid type '{ty}'")
        for k in ("created", "updated"):
            v = n.fm_scalar(k)
            if k in keys and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
                f.add("FM", "warn", n, dict(n.fm_keys).get(k, 1), f"{k} '{v}' is not YYYY-MM-DD")


# ---- check 2 and 3: links, orphans, folder index -------------------------
def build_name_index(notes: list[Note]) -> dict[str, Note]:
    idx: dict[str, Note] = {}
    for n in notes:
        for name in [n.stem, n.title(), *n.aliases()]:
            if name:
                idx.setdefault(name, n)
                idx.setdefault(name.lower(), n)
    return idx


def iter_links(n: Note):
    for i, line in enumerate(n.lines):
        if n.kind[i] == "fence":
            continue
        text = n.masked(i) if n.kind[i] == "body" else line
        # masked() blanks code spans; links inside code spans are not links
        for m in WIKILINK.finditer(text):
            raw = m.group(1).rstrip("\\")
            target = raw.split("|")[0].split("#")[0].strip().rstrip("\\")
            yield i + 1, target, m.group(0)


def check_links_and_orphans(root: Path, notes: list[Note], f: Findings) -> None:
    idx = build_name_index(notes)
    inbound: dict[str, set[str]] = defaultdict(set)
    for n in notes:
        for ln, target, raw in iter_links(n):
            if target == "":
                continue
            t = target.split("/")[-1]
            tgt = idx.get(t)
            if tgt is None:
                tgt = idx.get(t.lower())
                if tgt is not None:
                    f.add("LINK", "warn", n, ln, f"link {raw} resolves only case-insensitively to '{tgt.stem}'")
            if tgt is None:
                f.add("LINK", "error", n, ln, f"unresolved wikilink {raw}")
                continue
            if tgt is not n:
                inbound[tgt.rel].add(n.rel)
    for n in notes:
        if not inbound.get(n.rel):
            f.add("ORPHAN", "error", n, 1, "orphan: no other note links to this note")
    folders = {n.path.parent for n in notes}
    for d in sorted(folders):
        if d == root:
            continue
        bare = re.sub(r"^\d+\s+", "", d.name)  # "00 Home" may be indexed by "Home.md"
        if not (d / f"{d.name}.md").exists() and not (d / f"{bare}.md").exists():
            f.add("ORPHAN", "error", d.relative_to(root).as_posix() + "/", 0, f"folder has no index note '{d.name}.md'")
    # every folder index must be linked from its parent index or Index (covered by orphan check above)


# ---- check 4: component sections -----------------------------------------
def template_sections(root: Path) -> list[str]:
    t = root / "_templates" / "Component.md"
    secs = []
    if t.exists():
        for line in t.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"^##\s+(.*?)\s*$", line)
            if m and (DIMENSIONS_ENFORCED or m.group(1) != DIM_SECTION):
                secs.append(m.group(1))
    return secs


def check_components(root: Path, notes: list[Note], f: Findings) -> None:
    secs = template_sections(root)
    if not secs:
        f.add("COMP", "error", "_templates/Component.md", 0, "template not readable or has no sections")
        return
    for n in notes:
        if not n.rel.startswith(COMPONENT_DIR + "/") or n.fm_scalar("type") != "component":
            continue
        if n.stem in ("Inventory", COMPONENT_DIR):
            continue
        heads = []
        for i, line in enumerate(n.lines):
            if n.kind[i] == "body":
                m = re.match(r"^##\s+(.*?)\s*$", line)
                if m:
                    heads.append((m.group(1), i + 1))
        pos = 0
        names = [h for h, _ in heads]
        for s in secs:
            if s not in names:
                f.add("COMP", "error", n, 1, f"missing section '## {s}'")
                continue
            j = names.index(s, pos) if s in names[pos:] else -1
            if j < 0:
                f.add("COMP", "error", n, dict(heads).get(s, 1), f"section '## {s}' out of template order")
            else:
                pos = j + 1


# ---- check 4b: dimensions and defaults table --------------------------------
VALUE_OK = re.compile(r"\d|`[^`]+`")
NA = re.compile(r"^N/A:\s*(.{8,})$")


def parse_dimensions(n: Note) -> tuple[int, list[tuple[int, list[str]]]] | None:
    """Return (heading line, [(line, cells)]) of the Dimensions and defaults table, or None."""
    start = None
    for i, line in enumerate(n.lines):
        if n.kind[i] == "body" and re.match(r"^##\s+" + re.escape(DIM_SECTION) + r"\s*$", line):
            start = i
            break
    if start is None:
        return None
    rows = []
    for j in range(start + 1, len(n.lines)):
        line = n.lines[j]
        if re.match(r"^##\s", line):
            break
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append((j + 1, cells))
    return start + 1, rows


def check_dimensions(notes: list[Note], f: Findings) -> tuple[int, int]:
    total = valid = 0
    for n in notes:
        if not n.rel.startswith(COMPONENT_DIR + "/") or n.fm_scalar("type") != "component":
            continue
        if n.stem in ("Inventory", COMPONENT_DIR):
            continue
        total += 1
        parsed = parse_dimensions(n)
        if parsed is None:
            if DIMENSIONS_ENFORCED:
                f.add("DIM", "error", n, 1, f"missing section '## {DIM_SECTION}'")
            else:
                f.add("DIM", "info", n, 1, f"no '## {DIM_SECTION}' table yet")
            continue
        head, rows = parsed
        errs = 0
        if not rows or [c.lower() for c in rows[0][1]] != [c.lower() for c in DIM_COLUMNS]:
            f.add("DIM", "error", n, head, "table header must be: " + " | ".join(DIM_COLUMNS))
            continue
        seen = set()
        for ln, cells in rows[1:]:
            if len(cells) != 8:
                f.add("DIM", "error", n, ln, f"row has {len(cells)} cells, expected 8"); errs += 1; continue
            part, prop, tok, d, c, ds, src, settable = cells
            if prop not in DIM_PROPS:
                f.add("DIM", "error", n, ln, f"unknown property '{prop}'"); errs += 1; continue
            seen.add(prop)
            if not part:
                f.add("DIM", "error", n, ln, "empty Part cell"); errs += 1
            for lvl, v in (("Default", d), ("Compact", c), ("Dense", ds)):
                if not (NA.match(v) or (VALUE_OK.search(v) and "TBD" not in v.upper())):
                    f.add("DIM", "error", n, ln, f"{prop} {lvl}: needs a value or 'N/A: <reason of 8+ characters>' (got '{v}')"); errs += 1
            segs = [s.strip() for s in settable.split(";") if s.strip()]
            got = {}
            for s in segs:
                k, _, v = s.partition(":")
                got[k.strip()] = v.strip()
            bad = [k for k in SETTABLE_PROJECTS if k not in got or not SETTABLE_VALUE.match(got[k])]
            if bad or set(got) - set(SETTABLE_PROJECTS):
                f.add("DIM", "error", n, ln, f"{prop}: Settable needs 'tess-ui: <v>; tess-shell: <v>; tre: <v>' with v = yes | via <route> | hardcoded in tre | no hook | n/a: <reason> (problem: {', '.join(bad) or 'extra key'})"); errs += 1
            if not src:
                f.add("DIM", "error", n, ln, f"{prop}: empty Source cell"); errs += 1
            elif not re.search(r"\[\[|https?://|tess-ui:|tess-shell:|tre:|shell-vault:|MD3|WCAG", src):
                f.add("DIM", "error", n, ln, f"{prop}: Source must link a note, a URL or a project path (got '{src}')"); errs += 1
            elif "design choice" in src.lower() and "ADR" not in src:
                f.add("DIM", "error", n, ln, f"{prop}: a design choice names its ADR or a proposed ADR"); errs += 1
        for req in DIM_REQUIRED:
            if req not in seen:
                f.add("DIM", "error", n, head, f"required property row missing: {req}"); errs += 1
        if errs == 0:
            valid += 1
    f.add("DIM", "info", "vault", 0, f"dimensions coverage: {valid} of {total} component notes carry a valid table")
    return valid, total


# ---- check 5: acceptance criteria ----------------------------------------
def check_ac(notes: list[Note], f: Findings) -> None:
    defs: dict[str, list[tuple[Note, int]]] = defaultdict(list)
    norm: dict[tuple[str, int], str] = {}
    for n in notes:
        per_prefix: dict[str, list[tuple[int, int]]] = defaultdict(list)
        for i, line in enumerate(n.lines):
            if n.kind[i] != "body":
                continue
            m = AC_LINE.match(line)
            if not m:
                if re.match(r"^\s*-\s*\[.\]\s*AC\b", line):
                    f.add("AC", "error", n, i + 1, "AC line does not match '- [ ] AC-<PREFIX>-<n>'")
                continue
            box, acid, prefix, num, rest = m.group(1), m.group(2), m.group(3), int(m.group(4)), m.group(5)
            if box != " ":
                f.add("AC", "warn", n, i + 1, f"{acid}: checkbox is '[{box}]', criteria stay '[ ]' in the specification")
            defs[acid].append((n, i + 1))
            norm.setdefault((prefix, num), acid)
            per_prefix[prefix].append((num, i + 1))
            head = rest.strip()
            region = ""
            mm = re.match(r"^\(([^)]*)\)", head) or re.match(r"^:\s*([^.:]*)[.:]", head)
            if mm:
                region = mm.group(1).lower()
            found = [t for t in CHECK_TYPES if t in region]
            if not found:
                f.add("AC", "error", n, i + 1, f"{acid}: no check type from Test Method (got '{region.strip() or head[:30]}')")
            body = re.sub(r"^\([^)]*\)|^:\s*", "", head)
            if len(body.strip()) < 30:
                f.add("AC", "error", n, i + 1, f"{acid}: no pass condition (the text after the check type must state the assertion, at least 30 characters)")
        for prefix, items in per_prefix.items():
            nums = [x for x, _ in items]
            expected = list(range(1, len(nums) + 1))
            if nums != expected:
                f.add("AC", "error", n, items[0][1], f"AC-{prefix}: numbers {nums} are not consecutive from 1 in order of appearance")
    for acid, locs in defs.items():
        if len(locs) > 1:
            where = ", ".join(f"{n.rel}:{ln}" for n, ln in locs)
            for n, ln in locs[1:]:
                f.add("AC", "error", n, ln, f"duplicate AC id {acid} (also at {where})")
    for n in notes:
        for i, line in enumerate(n.lines):
            if n.kind[i] == "fence":
                continue
            for m in AC_CITE.finditer(line):
                cite = m.group(0)
                if cite in defs:
                    continue
                mm = re.match(r"AC-([A-Z0-9]+(?:-[A-Z0-9]+)*)-(\d+)$", cite)
                alt = norm.get((mm.group(1), int(mm.group(2)))) if mm else None
                if alt:
                    f.add("AC", "warn", n, i + 1, f"{cite} cited; defined as {alt} (zero-padding differs)")
                else:
                    f.add("AC", "error", n, i + 1, f"cited {cite} is not defined in any note")


# ---- check 6: token names -------------------------------------------------
def spans(line: str):
    return [m.group(2).strip() for m in CODESPAN.finditer(line)]


def token_key(s: str) -> str:
    return re.sub(r"@\d+%?$", "", s)


def check_tokens(root: Path, notes: list[Note], f: Findings) -> None:
    allowed: set[str] = set()
    extra: set[str] = set()
    for n in notes:
        in_found = n.rel.startswith(FOUNDATION_DIR + "/")
        in_extra = n.rel in TOKEN_DEFINING_EXTRA
        if not (in_found or in_extra):
            continue
        for i, line in enumerate(n.lines):
            if n.kind[i] == "fence":
                continue
            for s in spans(line):
                s = token_key(s)
                for part in re.split(r"[\s,/]+", s):
                    part = part.strip(" `")
                    if re.fullmatch(r"[a-z][a-z0-9_.-]*", part):
                        (allowed if in_found else extra).add(part)
    # scrollbar.* tokens defined only in the component note: allowed, reported once
    only_extra = sorted(t for t in extra if t not in allowed and re.match(r"(scrollbar|density)\.", t))
    if only_extra:
        f.add("TOKEN", "warn", TOKEN_DEFINING_EXTRA[0], 0,
              f"{len(only_extra)} scrollbar/density tokens are defined only in this component note, not in {FOUNDATION_DIR} (e.g. {only_extra[0]}); foundation notes should own token definitions")
    allowed |= extra
    for n in notes:
        for i, line in enumerate(n.lines):
            if n.kind[i] != "body":
                continue
            for s in spans(line):
                s = token_key(s)
                if "*" in s or "<" in s or " " in s:
                    continue
                s = s.rstrip(".,;:")
                if re.fullmatch(r"(?:scrollbar|density)\.[a-z0-9_.]+", s):
                    if s not in allowed:
                        f.add("TOKEN", "error", n, i + 1, f"token `{s}` is not defined in the foundation notes")
                elif ROLE_SHAPE.match(s) and s not in allowed:
                    f.add("TOKEN", "warn", n, i + 1, f"colour role name `{s}` is not in the foundation notes")


# ---- check 7: markdown rules ---------------------------------------------
def check_markdown(notes: list[Note], f: Findings) -> None:
    for n in notes:
        for i, line in enumerate(n.lines):
            for ch in line:
                cp = ord(ch)
                if is_emoji(cp):
                    sev = "warn" if cp in EMOJI_WARN else "error"
                    f.add("MD", sev, n, i + 1, f"emoji or pictograph U+{cp:04X}")
                    break
            if n.kind[i] != "body":
                continue
            for m in CODESPAN.finditer(line):
                s, e = m.start(), m.end()
                before = line[s - 1] if s > 0 else ""
                after = line[e] if e < len(line) else ""
                b2 = line[s - 2] if s > 1 else " "
                a2 = line[e + 1] if e + 1 < len(line) else " "
                touch = False
                if before == "*" or (before == "_" and not b2.isalnum()):
                    touch = True
                if after == "*" or (after == "_" and not a2.isalnum()):
                    touch = True
                if touch:
                    f.add("MD", "error", n, i + 1, f"bold or italic marker touches code span {m.group(0)[:40]}")
            for m in HTML_TAG.finditer(n.masked(i)):
                f.add("MD", "error", n, i + 1, f"raw HTML {m.group(0)[:40]}")


# ---- check 8: privacy -----------------------------------------------------
def check_privacy(notes: list[Note], f: Findings) -> None:
    for n in notes:
        for i, line in enumerate(n.lines):
            for p in PATH_PATTERNS:
                m = p.search(line)
                if m:
                    f.add("PRIV", "error", n, i + 1, f"absolute home-directory path '{m.group(0)}'")
            for p in SECRETS:
                m = p.search(line)
                if m:
                    f.add("PRIV", "error", n, i + 1, f"possible secret '{m.group(0)[:12]}...'")


# ---- check 9: needs-verification -----------------------------------------
def check_needs_verification(notes: list[Note], f: Findings) -> dict:
    per = {}
    for n in notes:
        lines = [i + 1 for i, l in enumerate(n.lines) if "#needs-verification" in l]
        count = sum(l.count("#needs-verification") for l in n.lines)
        if count:
            per[n.rel] = count
            f.add("NV", "info", n, lines[0], f"{count} #needs-verification tag(s), first at line {lines[0]}")
    return per


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    as_json = "--json" in argv
    root = Path(args[0]).resolve() if args else Path(__file__).resolve().parent.parent
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    notes = collect_notes(root)
    f = Findings()
    check_frontmatter(notes, f)
    check_links_and_orphans(root, notes, f)
    check_components(root, notes, f)
    check_dimensions(notes, f)
    check_ac(notes, f)
    check_tokens(root, notes, f)
    check_markdown(notes, f)
    check_privacy(notes, f)
    nv = check_needs_verification(notes, f)
    items = sorted(f.items, key=lambda x: (x["check"], {"error": 0, "warn": 1, "info": 2}[x["severity"]], x["file"], x["line"]))
    counts: dict[str, dict[str, int]] = defaultdict(lambda: {"error": 0, "warn": 0, "info": 0})
    for it in items:
        counts[it["check"]][it["severity"]] += 1
    errors = sum(c["error"] for c in counts.values())
    if as_json:
        json.dump({"root": str(root), "notes": len(notes), "needs_verification_total": sum(nv.values()),
                   "needs_verification_notes": len(nv), "counts": counts, "findings": items}, sys.stdout, indent=1)
        print()
    else:
        print(f"Vault lint: {len(notes)} notes under {root}")
        cur = None
        for it in items:
            if it["check"] != cur:
                cur = it["check"]
                c = counts[cur]
                print(f"\n== {cur}: {c['error']} error, {c['warn']} warn, {c['info']} info ==")
            loc = f"{it['file']}:{it['line']}" if it["line"] else it["file"]
            print(f"{it['severity'].upper():5} {loc}: {it['message']}")
        print("\nSummary")
        for ck in ["FM", "LINK", "ORPHAN", "COMP", "DIM", "AC", "TOKEN", "MD", "PRIV", "NV"]:
            c = counts.get(ck, {"error": 0, "warn": 0, "info": 0})
            print(f"  {ck:7} error {c['error']:4}  warn {c['warn']:4}  info {c['info']:4}")
        print(f"  #needs-verification: {sum(nv.values())} tags in {len(nv)} notes")
        print(f"Result: {'FAIL' if errors else 'OK'} ({errors} errors)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
