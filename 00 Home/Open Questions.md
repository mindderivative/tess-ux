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
| OQ-01 | Verbatim config-app feedback | closed 2026-11-21: recorded in [[Owner Feedback 2026-11-20]] | | |
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
| OQ-12 | MD3 values: verified against Material Web tokens and other sources for the slice notes; the m3.material.io pages are unreadable by tools, so the remaining items stay open in [[MD3 Verification Status]] | partly closed |
| OQ-13 | Closed: the shared shell venv is stale; run `uv sync` per checkout with `UV_PROJECT_ENVIRONMENT=<venv>` (engine floor 0.6.10, schema 1.15 on origin/main); the Phase 0 counts came from a patched path | closed |
| OQ-14 | Escape closes a focused shell Popup in code (`surfaces/popup.py` `_key`); not re-verified on a real KWin, no test found | open, hand check or test requested via the Orchestrator |
| OQ-15 | Closed: the virtual list thumb is draggable (vertical only); keys and scroll-into-view are not handled (`tre:crates/engine-core/src/tree/scroll.rs`) | closed, request needed for keys |
| OQ-16 | Closed: factories are built on the shipped TDL views (PR 311, 0.6.1) | closed |
| OQ-17 | Closed: caret blink default is steady (0); text input default font size is 16 | closed |
| OQ-18 | Closed: the list of stylesheet pages is in the tess-ui answer; none for Tree and TreeLevel | closed |

## New questions from Phase 1

| ID | Question | Recommendation | Evidence |
|---|---|---|---|
| OQ-19 | WCAG 1.4.13 asks that hover content stays hoverable and dismissible; ADR-0004 dismisses a plain tooltip on pointer leave of the trigger. Grant the 150 ms grace to all tooltips? | Yes: pointer moving from trigger onto the tooltip keeps any tooltip open for 150 ms; this is a change to ADR-0004 and needs the owner | [[14 Accessibility Basics]], [[Tooltip]] |
| OQ-20 | The scrollbar thumb rest opacity of 38 percent fails the 3 to 1 non-text contrast rule; the notes require at least 60 percent. Accept? | Accept 60 percent rest, 80 percent hover, 100 percent drag | [[Scrollbar and Scroll Container]] |
| OQ-21 | The 12 dp scrollbar hit area is below the 24 dp target of WCAG 2.5.8; does the equivalent-control exception apply (keyboard scrolling exists)? | Accept with the keyboard path as the equivalent | [[Scrollbar and Scroll Container]] |
| OQ-22 | Focus and pressed state layers are 12 percent in older Material Web tokens, 10 percent in the latest; ADR-0009 uses 10 | Keep 10 (latest token set) | [[State Layers]] |
| OQ-23 | Shell state layers (ADR-0009): adoption not decided; the shell audit will record the gap | Orchestrator asks the owner at the shell audit | [[State Layers]] |
| OQ-24 | Requests to tre: virtual list keys and scroll-into-view, two-axis scrolling | Raise as UXREQ notes through the Orchestrator | [[Scrollbar and Scroll Container]] |

Back to [[Index]].
