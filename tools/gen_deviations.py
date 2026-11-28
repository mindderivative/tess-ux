#!/usr/bin/env python3
"""Regenerates the body of '10 UX Design Specification/Deviations from MD3.md' from the
'## Deviations ...' tables of the notes in the 10, 20, 30 and 40 folders.

Usage: python3 tools/gen_deviations.py <vault root> [--check]
Section order: the order already in the register, then new notes in folder and name order.
The frontmatter and the intro paragraph of the register are kept; 'updated' is set to today
only when the body changes."""
import datetime, re, sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
check = "--check" in sys.argv
reg = root / "10 UX Design Specification" / "Deviations from MD3.md"
text = reg.read_text(encoding="utf-8")
first = text.index("\n## ")
head, body = text[:first + 1], text[first + 1:]
tail = ""
if "\nBack to" in body:
    i = body.index("\nBack to")
    body, tail = body[:i], body[i:]
old_order = re.findall(r"^## \[\[(.+?)\]\]", body, re.M)

found = {}
for folder in ("10*", "20*", "30*", "40*"):
    for d in sorted(root.glob(folder)):
        for note in sorted(d.glob("*.md")):
            if note == reg:
                continue
            s = note.read_text(encoding="utf-8")
            m = re.search(r"^## Deviations[^\n]*\n(.*?)(?=^## |\Z)", s, re.M | re.S)
            if not m:
                continue
            rows = [l for l in m.group(1).splitlines() if l.startswith("|")]
            rows = [r for r in rows[2:] if r.strip("| -")]  # drop header and rule
            if rows:
                found[note.stem] = rows
order = [n for n in old_order if n in found] + sorted(n for n in found if n not in old_order)
out = []
for n in order:
    out += [f"## [[{n}]]", "", "| Deviation | Reason | ADR |", "|---|---|---|", *found[n], ""]
new_body = "\n".join(out)
body_cmp = body.strip()
if new_body.strip() == body_cmp:
    print("Register is current"); sys.exit(0)
if check:
    print("Register is stale"); sys.exit(1)
head = re.sub(r"updated: [\d-]+", f"updated: {datetime.date.today()}", head, count=1)
reg.write_text(head + new_body + tail, encoding="utf-8")
print(f"Register rewritten: {sum(map(len, found.values()))} rows from {len(found)} notes")
