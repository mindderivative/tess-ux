---
title: Open Questions
type: questions
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [questions, decisions]
related: ["[[Plan]]", "[[Gaps and Contradictions]]"]
depends_on: []
---

# Open Questions

Decisions for the maintainer, recommendation first, and facts still to verify. A decision becomes a `proposed` ADR in `50 Decisions` when the topic is written; only the maintainer accepts.

## Decisions

| ID | Question | Recommendation | Alternatives | Evidence |
|---|---|---|---|---|
| OQ-01 | Provide the verbatim config-app demo feedback of 2026-11-20 (tooltips on whole rows and not closing, tree indentation and chevron gaps, text without ellipsis, missing horizontal scrollbars, top-aligned single-line text, dark theme ignored)? It is item 17 on the Orchestrator's list; the first rules are written from it | Yes, as text before the foundation chapters start | Rules written from the summary only | [[Gaps and Contradictions]] |
| OQ-02 | One token vocabulary for all projects? | The specification uses MD3 role names; projects keep separate code (shell ADR-0006) and map to it; the shell's 12 roles become a documented mapping | Keep two vocabularies; shell adopts MD3 roles fully | [[Existing Tokens]] |
| OQ-03 | Density: MD3 touch sizes or a desktop scale? | Three levels (default, compact, dense) for desktop, with a documented minimum target of 24 px (WCAG 2.2) and 48 px in touch contexts; default level for the config app and shell set per ADR | MD3 sizes only; one compact desktop size | no density in any project |
| OQ-04 | Scrollbar rule? | Both axes, visible when content overflows, track-less thumb allowed, width and hit area in tokens, auto-hide off by default on desktop; requests to tre for hover widening if wanted | Platform-native bars; engine default as is | engine thumb 4 px, owner feedback |
| OQ-05 | State feedback in the shell? | Adopt the MD3 state layer percentages as the specification and ask the shell to implement them (request through the Orchestrator) | Keep opacity literals and document them | shell stylesheet literals |
| OQ-06 | Tooltip rule? | Trigger on the control, not the row; 500 ms hover delay, immediate on keyboard focus; dismiss on Escape, scroll, pointer leave and activation; never on disabled-only information; rich tooltips reachable by keyboard | Row-level triggers where the row is the control | tess-ui tooltips, engine without timers |
| OQ-07 | Dark and light? | Follow the system by default, user override persists, no first-frame flash (decide before drawing) | Always dark default for the shell | tess-ui `follow.py`, shell default |
| OQ-08 | MD3 baseline or Expressive? | Baseline MD3 tokens (2022 role and shape scales) with named Expressive adoptions recorded as deviations (for example button sizes) | Full Expressive | tess-ui mixes both |
| OQ-09 | Icon set? | Specify the icon rules (size, optical sizing, fallback) independently of the set; keep Material Design Icons for now and record the difference from Material Symbols as a deviation | Move to Material Symbols | tess-icons, engine draws paths only |
| OQ-10 | Publishing flow: a PR per task to `main`, who merges, are branches kept? | Keep the provisional flow: branch `docs/<task>`, PR to `main`, the Orchestrator and the owner merge | Direct commits to `main` after review | SOUL.md |
| OQ-11 | Approve the chapter order and family order in [[Plan]]? | Approve, with families 1 to 5 as the first release | Reorder by project priority | [[Plan]] |

## To verify

| ID | Item | Status |
|---|---|---|
| OQ-12 | MD3 values and links in [[Existing Tokens]] and [[Inventory]] were quoted by the readers and not opened | #needs-verification |
| OQ-13 | `tesserae-shell schema --json` fails in the shell's own venv (engine 0.6.7 installed, 0.6.9 required, `tess_utils` missing); counts of 27 kinds, 25 roots and 31 modules were taken from a run with the engine working tree on the path | #needs-verification, ask the shell bot |
| OQ-14 | Whether Escape closes shell popups after the tre `input_region` fix | #needs-verification, ask the shell bot |
| OQ-15 | Whether the virtual list thumb is draggable in tre and whether keys work | #needs-verification, ask the tre bot |
| OQ-16 | The unfinished unification of tess-ui Python factories and TDL views (design note `factories-on-tdl-views.md`) | #needs-verification, ask the tess-ui bot |
| OQ-17 | Caret blink period default and default text input font size (16 in creation code, 14 in docs) | #needs-verification |
| OQ-18 | Which tess-ui stylesheet pages exist per component (only `buttons` was checked) | #needs-verification |

Back to [[Index]].
