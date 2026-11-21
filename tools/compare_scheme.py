#!/usr/bin/env python3
"""Compare an engine or project colour scheme with the Colour Roles reference table.

Usage: python3 tools/compare_scheme.py scheme.json [vault root] [--json]

scheme.json is {"light": {"primary": "#6750A4", ...}, "dark": {...}} with the 49
snake_case role names of the Colour Roles note. Standard library only. The
reference is the standard-contrast light and dark table in
"20 Foundations and Tokens/Colour Roles.md" (parsed with tools/contrast_check.py).

A role matches when every channel differs by at most 2 on the 0 to 255 scale or
CIEDE2000 is below 1.0 (Colour Roles, rule 11). The report lists mismatched roles
with both hex values, the maximum channel difference and the CIEDE2000 value, and
roles missing on either side. Exit code 1 when any role mismatches or is missing.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import contrast_check as cc  # noqa: E402

CHANNEL_TOL = 2
DE_TOL = 1.0


def to_rgb(h: str) -> tuple[int, int, int]:
    h = h.strip().lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def srgb_to_lab(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    def lin(c: float) -> float:
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883

    def f(t: float) -> float:
        return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def ciede2000(l1, l2) -> float:
    L1, a1, b1 = l1
    L2, a2, b2 = l2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if C1p else 0.0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if C2p else 0.0
    dLp, dCp = L2 - L1, C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    else:
        dhp = h2p - h1p
        dhp -= 360 if dhp > 180 else 0
        dhp += 360 if dhp < -180 else 0
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lpm, Cpm = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hpm = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hpm = (h1p + h2p) / 2
    else:
        hpm = (h1p + h2p + 360) / 2 if h1p + h2p < 360 else (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hpm - 30)) + 0.24 * math.cos(math.radians(2 * hpm))
         + 0.32 * math.cos(math.radians(3 * hpm + 6)) - 0.20 * math.cos(math.radians(4 * hpm - 63)))
    dTheta = 30 * math.exp(-(((hpm - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lpm - 50) ** 2 / math.sqrt(20 + (Lpm - 50) ** 2)
    Sc, Sh = 1 + 0.045 * Cpm, 1 + 0.015 * Cpm * T
    Rt = -math.sin(math.radians(2 * dTheta)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh))


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    scheme = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    root = Path(args[1]).resolve() if len(args) > 1 else Path(__file__).resolve().parent.parent
    ref_all = cc.parse_roles((root / cc.COLOUR_NOTE).read_text(encoding="utf-8"))
    rows, bad = [], 0
    for mode, key in (("light", "light_std"), ("dark", "dark_std")):
        ref = {k: tuple(round(c * 255) for c in v) for k, v in ref_all[key].items()}
        got = {k: to_rgb(v) for k, v in scheme.get(mode, {}).items()}
        for role in sorted(set(ref) | set(got)):
            if role not in got:
                rows.append({"mode": mode, "role": role, "status": "missing in scheme"}); bad += 1; continue
            if role not in ref:
                rows.append({"mode": mode, "role": role, "status": "not in the reference table"}); bad += 1; continue
            dmax = max(abs(a - b) for a, b in zip(ref[role], got[role]))
            de = ciede2000(srgb_to_lab(ref[role]), srgb_to_lab(got[role]))
            ok = dmax <= CHANNEL_TOL or de < DE_TOL
            if not ok:
                bad += 1
            rows.append({"mode": mode, "role": role, "status": "ok" if ok else "MISMATCH",
                         "reference": "#%02X%02X%02X" % ref[role], "scheme": "#%02X%02X%02X" % got[role],
                         "max_channel_diff": dmax, "ciede2000": round(de, 2)})
    if "--json" in argv:
        json.dump({"mismatches": bad, "rows": rows}, sys.stdout, indent=1)
        print()
    else:
        total = len(rows)
        print(f"Scheme compare: {total} role values, {bad} mismatch or missing (tolerance: channel +-{CHANNEL_TOL} or CIEDE2000 < {DE_TOL})")
        for r in rows:
            if r["status"] != "ok":
                print(f"{r['mode']:5} {r['role']:28} {r['status']}" + (f" ref {r['reference']} scheme {r['scheme']} max diff {r['max_channel_diff']} dE {r['ciede2000']}" if "reference" in r else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
