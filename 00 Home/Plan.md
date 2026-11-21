---
title: Plan
type: plan
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [plan]
related: ["[[Inventory]]", "[[Existing Tokens]]", "[[Gaps and Contradictions]]", "[[Open Questions]]"]
depends_on: []
---

# Plan

How the two specifications get written, in what order, how their rules are tested, and what the maintainer must decide. Phase 0 delivered the [[Inventory]] (276 merged element rows from 478 source rows), [[Existing Tokens]] and [[Gaps and Contradictions]]. Everything below is proposed; nothing is decided until the maintainer says so.

## Progress (2026-11-22)

- Phase 0: inventory, tokens, plan (done). Phase 1: owner-feedback slice (done). Phase 2: chapters 03 to 17, 9 patterns, component families, shell surfaces and modules, blocks and engine surfaces (written, in review and merged). Phase 3: integration, vault lint, adoption worklists.
- Component notes: 113, patterns: 9, chapters: 17 (16 is the [[Deviations from MD3]] register). The [[Inventory]] maps all 276 rows: own note, covered in another note, or backlog (23 rows, `not yet specified`).
- Next: the Backlog in [[Inventory]], audits ([[Adoption Plan]]), the open decisions OQ-23 and OQ-32 in [[Open Questions]], and verification of the `#needs-verification` items ([[MD3 Verification Status]]).

## Principles of the work

- Material Design 3 is the baseline; each departure is a row in the deviation register of the target note and a proposed ADR.
- Each fact is defined once. Foundations own tokens; component notes link to them (`![[Note#Heading]]` for embeds).
- Each rule is testable: dp, ms, hex, contrast ratio, key sequence. A rule without a criterion is not done.
- Specs describe what the user sees and does; they do not invent engine API. A gap becomes a request note `UXREQ-###` (folder `80 Requests`), routed through `bot:Orchestrator`.
- Code status in [[Inventory]] marks what exists. A spec may describe the target before the code reaches it; the note says which criteria the code does not meet yet.

## UX Design Specification: chapters

Each chapter is one note in `10 UX Design Specification` (principles, rules) and, where it defines values, a note in `20 Foundations and Tokens`. Effort: S is one session, M two to three, L four or more, a session being one agent run that ends in a commit.

| # | Chapter | Note home | Content | Evidence in [[Existing Tokens]] | Effort |
|---|---|---|---|---|---|
| 1 | Principles and scope | 10 | Goals, audiences (desktop, shell, dashboard), keyboard first, MD3 baseline and deviation policy, conformance language | AGENTS.md of the vault | S |
| 2 | Colour roles and theming | 20 and 10 | Role set, tonal generation, light, dark, following the system, high contrast levels, the shell versus tess-ui vocabulary, contrast rules | colour groups | L |
| 3 | Typography | 20 | Type scale, tracking, line height, fonts and fallbacks, text rendering rules | type groups | M |
| 4 | Shape | 20 | Corner scale, per-component use, Expressive steps | shape groups | S |
| 5 | Elevation | 20 | Levels, shadow geometry, tonal containers, scrim | elevation groups | M |
| 6 | Motion | 20 and 10 | Durations, easings, springs, reduced motion, when to animate | motion groups | M |
| 7 | Spacing and density | 20 | Spacing scale, density levels, minimum target size, desktop defaults | spacing, density | L |
| 8 | Iconography | 20 | Icon set, sizes, optical sizing, fallback, animated icons | icon groups | M |
| 9 | State layers, ripple and focus | 20 and 10 | State percentages, disabled scheme, ripple, focus ring rules | state groups | M |
| 10 | Layout, overflow and scrolling | 10 | Window size classes, panes, ellipsis, wrapping, vertical centring, scrollbars, virtual lists | scrollbar, density | L |
| 11 | Interaction | 10 | Pointer, keyboard map, focus order, shortcuts, touch, hover versus focus, click-outside rules | focus groups | L |
| 12 | Overlays | 10 | Tooltips, popups, menus, dialogs, scrim, placement, dismissal | tooltip rows | L |
| 13 | Patterns | 40 | Empty, loading, error, validation, notifications, selection, drag and drop, forms, settings | none exist | L |
| 14 | Accessibility | 60 and 10 | Roles, names, announcements, live regions, contrast, target sizes, screen-reader support level | accessibility rows | L |
| 15 | Writing | 10 | Labels, errors, tooltips text, capitalisation (skill ux-writing) | none | S |
| 16 | Deviations from MD3 | 10 | The register of all departures with ADR links | built up across chapters | S, last |
| 17 | Conformance and testing | 60 | How each rule type is tested, per project | see below | M |

## UX Component Design Specification: order of families

One note per spec note name in [[Inventory]] (276 rows; many foundation, behaviour and state rows become sections of the chapters above, not component notes: roughly 170 component notes, [INFERENCE] until the families are written). Order follows dependency: tokens first, then the elements other elements are built from.

| Order | Family | Examples (provisional note names) | Why here |
|---|---|---|---|
| 0 | Foundations and behaviours | Colour Roles, Typography, Shape, Elevation, Motion, State Layers, Focus Ring, Ripple, Scrollbars | every component links to them |
| 1 | MD3 actions | Button, Icon Button, FAB, Extended FAB, Button Group, Split Button, Segmented Button, Token Button | most used; defines state rules |
| 2 | MD3 text inputs | Text Field, Spin Box, Time Input, Search Bar, Key Chord Field | the config app feedback sits here |
| 3 | MD3 selection | Checkbox, Radio Button, Switch, Chip, Slider, Date Picker, Time Picker | share the state scheme |
| 4 | MD3 communication | Badge, Progress Indicator, Snackbar, Banner, Tooltip | tooltips are owner-feedback priority |
| 5 | Tooltips, overlays, popups | Tooltip, Popup, Menu, Dialog, Side Sheet, Scrim, Anchored Placement | needs the interaction chapter |
| 6 | MD3 containment | Card, Divider, Accordion, Carousel, List, Bottom and Side Sheets | |
| 7 | Lists, trees, tables | List, Tree, Virtual List, Table (not in code), List Editor | density and indentation feedback |
| 8 | MD3 navigation | Top App Bar, Tabs, Navigation Rail, Navigation Drawer, Toolbar, Pagination, Status Bar | |
| 9 | Window, dock and panels | Window, Title Bar, Splitter, Dock, Dock Panel, Routed Views | |
| 10 | Pickers | File Dialog, Colour Picker, Font List, Icon Picker, Choice Picker | config app elements |
| 11 | Shell surfaces | Bar, Frame, Panel, Popup, Launcher, Volume OSD, Peek, Auto Hide | design intent in the shell vault |
| 12 | Shell modules | Clock, Battery, Audio, Network, Tray, Tasks, Workspaces, Applications, Media, TextBox, TextEditor | uses families 1 to 8 |
| 13 | Blocks and primitives | Box, FlexBox, Text, Rectangle, Circle, Ring, Path, Bitmap, SVG, Marquee, Canvas | structural; thin notes |
| 14 | Node graph, video, canvas, terminal | Node Graph, Video Player, Terminal, Canvas | Tesserae-specific, lowest priority |
| 15 | Engine surfaces | Application Window, Layer Window, Popup Window, Accessibility Tree | constraints the specs must respect |

Estimate: about 1 session per 3 to 5 component notes once the foundations are accepted, so 40 to 55 sessions for components, 25 to 30 for chapters and foundations, plus audits. Families 1 to 5 are the first release because they hold the owner feedback.

## Template check

`_templates/Component.md` was created from the vault `AGENTS.md` list: purpose, when to use and not, anatomy, variants, states, tokens used, sizing and density, layout and overflow, behaviour (pointer, keyboard, touch), tooltip and overlay behaviour, motion, accessibility, dark and light, defaults, acceptance criteria, source of truth in code, deviations from MD3. It matches the list one to one; the Phase 0 reading adds no section. Candidates for later: a `Related elements` section (the frontmatter `related` covers it) and a per-project status row inside the source table (already present).

`_templates/ADR.md` carries context, options with the recommendation first, decision, consequences, affected notes; status starts `proposed`.

## How acceptance criteria are tested and audited

| Criterion type | Example | Method | Where it runs |
|---|---|---|---|
| Token value | focus ring 3 px, offset 2 px | unit test reading the token | each project's test suite |
| Geometry | control height 40 dp at density default | layout test measuring node bounds | tess-ui and shell tests with headless rendering |
| Contrast | text over container at least 4.5 to 1 | script over the shipped themes, all roles and both modes | a tool in each project; the shell lacks it today |
| Timing | tooltip appears 500 ms after hover | test with a fake clock | tess-ui; the engine has no timers |
| Key sequence | Arrow Down opens a menu, Escape closes it, focus returns | scripted input test | tess-ui and shell |
| Accessibility | role, name, live announcement present | AccessKit tree assertion; screen-reader hand check where possible | tests plus hand checks listed per project |
| Visual | state layer visible at 8 percent | screenshot compare or review checklist | review |

Each criterion carries an identifier `AC-n` and a type, so an audit lists pass, fail, not testable. Audits are notes in `70 Adoption`, one per project, assigned through `bot:Orchestrator` to the project bots, who run the criteria against their code and report; this vault writes no code. Failures that need engine or project work become `UXREQ-###` notes.

## What I need from the maintainer

The decisions are in [[Open Questions]] with a recommendation first. Short list: shared token vocabulary (OQ-02), density (OQ-03), scrollbars (OQ-04), state feedback in the shell (OQ-05), tooltip rule (OQ-06), dark theme following the system (OQ-07), baseline MD3 versus Expressive (OQ-08), icon set (OQ-09), the verbatim owner feedback list (OQ-01), the publishing flow (OQ-10) and approval of the chapter and family order above (OQ-11).

## Gaps and contradictions found

The full list with evidence is [[Gaps and Contradictions]]. The ones named in the brief:

- Config app tree indentation and chevron gaps: no density token; `Tree` has `Compact` only (40 px rows against 56); no rule for indentation per level.
- Tooltip behaviour: delay and grace values in tess-ui code only, engine without timers, whole-row triggers in the config app, rich tooltip actions unreachable by keyboard.
- Dark theme: tess-ui follows the OS with a first-frame flash; the config app sets three rules and relies on roles; the shell is dark by default.
- Scrollbars: colour only in tess-ui, 4 px thumb in the engine, no horizontal-scrollbar rule, none in the shell.
- Text: ellipsis only until focus in the engine for single-line inputs; no vertical centring rule.
- Everything in the list at the top of [[Gaps and Contradictions]]: two token systems, state feedback, missing patterns, unbuilt shell keys, documentation drift, screen-reader testing, icon set.

## Phases after Phase 0

1. Foundations chapters 2 to 9 with proposed ADRs for each decision, then the maintainer accepts or changes.
2. Families 1 to 5 (actions, text inputs, selection, communication, overlays), including the owner feedback rules.
3. Remaining families in the order above; chapters 10 to 15 written alongside.
4. Chapter 16 and 17, adoption audits through the Orchestrator.

Back to [[Index]].
