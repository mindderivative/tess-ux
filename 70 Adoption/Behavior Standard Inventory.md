---
title: Behavior Standard Inventory
type: adoption
status: draft
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adoption, inventory, behavior-standard]
related: ["[[Adoption Plan]]", "[[Inventory]]", "[[Keyboard Navigation]]", "[[Selection]]", "[[Anchored Placement]]", "[[Hooks Needed]]"]
depends_on: []
---

# Behavior Standard Inventory

Inventory for a Tesserae behavior standard (item 28, direction approved by the owner). It cross-references the upstream UI SDK of vercel-labs/ui (`packages/core/src`: 51 components and 21 foundation jobs; the brief said 52, the components folder lists 51) against the vault notes, `COMPONENT_LIST.md` and the real code of tess-ui, tess-shell and tre. Clean-room: only names and behaviour contracts were taken, no code. Desk research by reading and grep only; nothing was run. Cells marked `[unverified]` rest on a grep hit without reading the logic. Judgement used: `covered` means a Tesserae spec note and code both exist, `divergent` means one exists or it behaves or is named differently, `missing` means neither.

Sources: upstream https://github.com/vercel-labs/ui and https://ui-sdk.dev/docs (names and contracts); tess-ui, tess-shell and tre at their `origin/main` (tre includes unreleased 0.6.12 work).

## Summary

- Upstream components: 20 covered, 21 divergent, 10 missing (autocomplete, avatar, command, image-cropper, menubar, otp-input, password-input, rating, timeline, waterfall).
- Upstream foundation jobs: 6 covered (disclosure, focus, motion, platform, popups, selection), 14 divergent, 1 missing (date).
- Behaviours implemented separately in two or more projects: roving focus, dismissal, disclosure, focus recovery, tooltip timing, shortcut and chord handling; partly: anchored placement, change reasons, drag threshold and cancel.
- tre already offers selection (PR 350, 353), anchored layers (346), state layers (335), outline (336) and accessibility roles (328).

## Table A and B: coverage

### Table A: upstream components

| Upstream | Tesserae counterpart (vault note) | tess-ui | tess-shell | tre | Status | Notes |
|---|---|---|---|---|---|---|
| accordion | Accordion | AccordionGroup_View, Accordion_View | Expander module (shell:shipped/Expander) | tree/layout, animation.rs | covered | AC-ACC |
| autocomplete | none (Search, Chip suggestion partial) | SearchBar/SearchView, ChipSuggestion | none | none | missing | no suggestion-list-on-input contract; AC-SRB is search only |
| avatar | none (Badge is different) | none | none | none | missing | no image/initials fallback component |
| button | Button, Icon Button, Button Group | ButtonFilled/Tonal/Elevated/Outlined/Text | shipped/Button | state_layer.rs | covered | MD3 variants; AC-BTN, AC-ICB, AC-BTG |
| calendar | Date Picker (grid part) | DatePicker, DatePickerDay* | none | none | divergent | grid is inside the picker, no standalone calendar, no range/multi; AC-DTP |
| carousel | Carousel | Carousel_View (Python only) | none | animation.rs | covered | AC-CRS |
| checkbox | Checkbox | Checkbox | shipped/Checkbox | none | covered | AC-CHK |
| collapsible | Accordion / Expander | AccordionHeader | Expander module | layout_anim.rs | divergent | no single-section primitive; Expander is a shell bar module; AC-ACC |
| color-picker | Colour Picker | ColourPicker, ColourPickerPanel | none | none | covered | named Colour; AC-CLP |
| combobox | Choice Picker | none | none | none | divergent | spec only, no code `[unverified]`; AC-CHO |
| command | none | none | Launcher is a note, no code `[unverified]` | none | missing | no command palette; Launcher AC-DEN only |
| date-input | Date Picker (input mode), Time Input | DatePicker, TimeInput | none | none | divergent | time-only input exists; typed segmented date field unverified; AC-DTP, AC-TMI |
| date-picker | Date Picker | DatePicker | none | none | covered | AC-DTP |
| dialog | Dialog | Dialog | none | overlay.rs, tree/layers.rs | covered | modal focus trap `[unverified]`; AC-DLG |
| drawer | Side Sheet, Navigation Drawer | SideSheet*, NavigationDrawer* | none | overlay.rs | divergent | MD3 names; no drag-to-dismiss sheet from bottom `[unverified]`; AC-LAY |
| field | Form Row, Text Field | FormRow via TextField_View | none | none | divergent | no Field wrapper (label+hint+error ids); Form Row is layout; AC-FRM, AC-FST |
| file-input | File Dialog | FileDialog | none | none | divergent | dialog browse only, no drop zone/input control; AC-FDL |
| hover-card | Peek | none found | none | overlay.rs | divergent | Peek spec only `[unverified]`; AC-PEK |
| image-cropper | none | none | none | none | missing | no crop UI |
| input | Text Field, Text Box | TextField | shipped/TextInput, TextBox | selection.rs | divergent | MD3 floating label; AC-TXF, AC-MOD |
| label | Label | Text (COMPONENT_LIST Content) | shipped/Label | none | covered | AC-MOD |
| listbox | List, Choice Picker | ListItem, List editor | shipped/List | tree/list_selection.rs | divergent | List has no typeahead/active-descendant listbox contract `[unverified]`; AC-LST, AC-ADE |
| menu | Menu, Menu Item | Menu, MenuItem | shipped/Menu, MenuItem | overlay.rs | covered | AC-MEN |
| menubar | none (Bar is shell panel, Title Bar) | none | Bar spec only | none | missing | no top menubar with arrow-key roving between menus |
| meter | Progress Indicator | LinearProgress/CircularProgress | shipped/ProgressBar | none | divergent | progress only, no low/high/optimum meter semantics; AC-PRG |
| navigation-menu | Navigation Rail, Navigation Drawer, Top App Bar | NavigationRail*, NavigationDrawer*, TopAppBar | none | none | divergent | app nav, no fly-out mega menu; AC-LAY |
| number-input | Spin Box | SpinBoxField | none | none | divergent | named Spin Box; AC-SPN |
| otp-input | none | none | none | none | missing | |
| pagination | Pagination | Pagination (Python only) | none | none | covered | AC-BTN (note shares prefix) |
| password-input | none (Text Field) | none | none | none | missing | no mask/reveal toggle `[unverified]` |
| popover | Popup, Anchored Placement | overlays.py, Menu | Popup Window note | overlay.rs, anchoring in layers.rs | divergent | Popup is MD3 overlay name; AC-POP, AC-ANC |
| progress | Progress Indicator | Linear/Circular/LoadingIndicator | shipped/ProgressBar | animation.rs | covered | AC-PRG |
| radio | Radio Button | RadioButton | none | none | covered | tess-shell has no module; AC-RAD |
| rating | none | none | none | none | missing | |
| resizable | Splitter | Splitter (Python only) | none | gesture.rs | divergent | named Splitter; AC-SPL `[unverified]` |
| scroll-area | Scrollbar and Scroll Container, ScrollBox | scrolling.py | none | scrollbar.rs, scrollbar_props.rs | covered | AC-SCB |
| segmented-control | Segmented Button | SegmentedButton (Python only) | none | none | divergent | MD3 name; AC-SEG |
| select | Choice Picker, Menu | none | none | none | divergent | no select control view; AC-CHO |
| separator | Divider | Divider | none | none | divergent | name; AC-DIV |
| slider | Slider | Slider | shipped/Slider | gesture.rs | covered | AC-SLD |
| switch | Switch, Toggle | Switch | shipped/Toggle | none | covered | AC-SWI |
| tabs | Tabs | Tabs | none | none | covered | AC-TBS |
| timeline | none | none | none | none | missing | |
| toast | Snackbar | Snackbar, SnackbarHost | Volume OSD only | none | divergent | MD3 name; Banner note too; AC-SNK, AC-BNR |
| toggle | Toggle (shell), Icon Button toggle | IconButton toggle | shipped/Toggle | none | covered | AC-MOD, AC-ICB |
| token-input | Token Button | ChipInput, TokenButton | none | none | divergent | chip input is the MD3 equivalent; AC-TKB, AC-CHP |
| toolbar | Toolbar | ToolbarDocked/Floating | none | none | covered | AC-TLB |
| tooltip | Tooltip | Tooltip | none | overlay.rs | covered | AC-TIP (65 ids) |
| tree | Tree, Tree Node | Tree, TreeNode | none | tree/container_selection.rs | covered | AC-TRE, AC-TRN |
| trigger-menu | Menu, Split Button | SplitButton, Menu | shipped/Tray_Menu | overlay.rs | divergent | no generic trigger-plus-menu primitive; AC-SPB |
| waterfall | none | none | none | none | missing | masonry layout; Grid/FlexBox only (AC-BLK) |

Counts A (51 rows, scripted tally): covered 20, divergent 21, missing 10.

### Table B: Foundation jobs

| Upstream job | What it does | Tesserae counterpart | Status | AC ids |
|---|---|---|---|---|
| canvas | connect lines and pan/zoom viewport for node canvases | Node Graph; tre canvas.rs, path.rs | divergent | AC-NGR |
| color | parse/convert/mix/format colours, gamut mapping, names | tess-ui:colour.py, Colour Roles (vault 02 Colour and Theming); tre scheme.rs | divergent (no gamut/names API `[unverified]`) | AC-CLP |
| date | plain-date type, week calc, parse and format | Date Picker; no date lib found | missing `[unverified]` | AC-DTP |
| direct-manipulation | move/resize/area drag, hold-repeat, previews | Splitter, Slider, Drag and Drop; tre gesture.rs | divergent | AC-SLD, AC-DND |
| disclosure | open/closed state for expandable sections | Accordion, Expander, Tree Node | covered | AC-ACC, AC-TRN |
| drag-and-drop | pointer drag, reorder, transfer, auto-scroll, tree reorder | vault Drag and Drop, 40 Drag and Drop Pattern | divergent (spec; code `[unverified]`) | AC-DND, AC-DNP |
| focus | roving focus, collections, focus recovery, keep-focus | vault 11 Interaction, Keyboard Navigation, Active Descendant; tess-ui:focusring.py; tre tree/focus.rs | covered | AC-INT, AC-KBN, AC-ADE, AC-FOC |
| forms | controls, validation, files, text-field hints | 40 Forms and Settings, Validation; tess-ui:binding.py | divergent (no form object) | AC-FST, AC-VAL |
| gauge | arc/linear value geometry | Progress Indicator | divergent | AC-PRG |
| image | image load, crop | Image, SVG, Bitmap; tre svg.rs | divergent (no crop) | AC-IMG, AC-SVG |
| kernel | action/controller/derive state core | tess-ui:reactive.py, viewmodel.py, binding.py | divergent | none |
| lists | listbox behaviour, async options, inline edit, findable rows | List, List Editor, Choice Picker; tre list_selection.rs | divergent | AC-LST, AC-LED, AC-CHO |
| motion | curves, physics, gesture handoff, panels | vault 06 Motion Rules; tess-ui:motion.py, transition.py; tre animation.rs, easing.rs | covered | AC-MOT, AC-C06 |
| number | parse/format/step/scale numbers | Spin Box | divergent | AC-SPN |
| platform | anchoring, announce, layers, keyboard, env | Anchored Placement, Accessibility Tree; tess-ui:a11y.py; tre access.rs, tree/layers.rs | covered | AC-ANC, AC-AXT, AC-A11Y |
| popups | popup creation, dismissal, hover, modal | 12 Overlays, Popup, Dialog; tess-ui:overlays.py | covered | AC-OVL, AC-POP, AC-TIP |
| preferences | colour scheme and pointer kind preferences | Theming, Density, shell Themes | divergent | none |
| selection | selection model, range, lasso | 40 Selection, Text Selection; tre selection.rs, container_selection.rs | covered | AC-SLT |
| shortcuts | shortcut registry, order, slots | Key Chord Field; tess-ui:key_chords.py | divergent | AC-KCF |
| storage | persistence | tess-ui:windowstate.py, shell settings | divergent `[unverified]` | none |
| text | accessible names, caret, fuzzy match, input history | 03 Typography, Text Editor; typing_effects.py | divergent | AC-TXF |

Counts B (21 rows, scripted tally): covered 6, divergent 14, missing 1.

## Duplicated behaviours

The same behaviour implemented separately in tess-ui, tess-shell and tre, first because they are the candidates for one shared standard.

| Behaviour | tess-ui (path, how) | tess-shell (path, how) | tre (path, how) | Duplicated? | Vault AC ids | Reusable from tre today |
|---|---|---|---|---|---|---|
| Roving / arrow-key focus groups | tess-ui:composed.py `_GROUP_KEYS`, key handler near L1154-1216: one tab stop per `focus_group`, arrows by mode (horizontal/vertical/both), Home/End, wrap | tess-shell:binder/build.py L175, L321, L746: "active" menu row driven by arrows, own key_down handler | tre:crates/engine-core/src/tree/dispatch.rs L434-442 arrow keys scroll/move focus; tree/focus.rs Tab order; no group/roving primitive [unverified] | yes (tess-ui, tess-shell) | vault:Keyboard Navigation (40 Patterns) [AC ids not read]; AC-MEN-*; AC-LST-* | none (only Tab order and key events) |
| Dismissal: Escape, click-away | tess-ui:overlays.py table L11 (per overlay outside press/Escape), `dismiss_surface` L50, composed.py `_dismiss_layer` L1061 writes `open=false` | tess-shell:surfaces/popup.py L793-804 Escape closes innermost level; `_closed` L922 reasons `dismissed`/`failed`/`app`; binder/build.py L134 press anywhere dismisses | tre:overlay.rs L239-240 `dismiss_on_outside_click`, `dismiss_on_escape`; tree/layers.rs `take_dismissals`; `show_layer(..., dismissible)` and `dismiss` event (docs/guide/layers.md L11, L40) | yes (tess-ui layer path vs tess-shell popup path both wrap tre) | vault:AC-POP-*, AC-MEN-*, AC-DLG-*, AC-ANC-* | `show_layer(dismissible=)`, `dismiss` event, `modal` |
| Typeahead | tess-ui:composed.py `_typeahead` L1218, printable key in focus group | none found | none found | no (one project) | vault:AC-LST-* [unverified] | none |
| Active descendant | none found | tess-shell:binder/build.py L175, L746 ("active" row look, one row) | tre:`active_descendant` property (node_props.rs L105, L1791, L2097), tree/access.rs | no real logic duplicated; tre has the property, shell fakes the look | vault:Active Descendant#AC-ADE-1..8 | `active_descendant` get/set |
| Positioning / flip / anchored placement | tess-ui:overlays.py L111-117 `open(anchor, placement)` -> `window.show_layer`; spec/placement.py; composed.py flip [unverified] | tess-shell:surfaces/popup.py, schema/default_popups.py, binder/rebuild.py: popup placement and flip, `Flip` in schema/shell.py, surfaces/outline.py | tre:overlay.rs `Placement`, `flip`, `flip_threshold`, viewport margin; PR 346; docs/guide/layers.md L44-67 | partly (both map spec names onto tre; neither re-implements flip) | vault:Anchored Placement#AC-ANC-1..9; AC-POP-* | `placement`, `anchor`, `offset`, `flip`, `align`, `layer_viewport_margin`, `layer_flip_threshold`, `layer_placement` (read-back) |
| Selection ranges (single, multi, Shift/Ctrl, anchor) | tess-ui:widgets/selection.py, list_controls.py [unverified, grep only for shift/ctrl found nothing] | tess-shell:binder/controls.py `Item` kind L725 (single-choice only) | tre:`selection_mode` (single/multiple), `selection`, `selection_anchor` (read-only), `select_all_key`, `select_on_focus`, `selection_change` event; list_selection.rs, tree/container_selection.rs; PRs 350 (virtual_list), 353 (container children) | no (apps lack it; tre owns it) | vault:Selection#AC-SLT-1..15; AC-LST-*; AC-TRE-* | all of it: set `selection_mode` instead of coding Shift/Ctrl logic |
| Disclosure (expand/collapse) | tess-ui:widgets/structural.py L247 expanded `Signal`, click/Enter/Space/arrows, AT expand/collapse; a11y.py L34 | tess-shell:binder/controls.py `Expand` L725 | tre:`expanded` property (access.rs, node_props.rs L89, L1241, L2035); PR 328 roles | yes (tess-ui and tess-shell each own the toggle logic) | vault:AC-ACC-01..; AC-TRE-01..; Expander | `expanded`, `set_size`, `pos_in_set` for AT |
| Change reasons (pointer / keyboard / api) | tess-ui:structural.py L248 `on_change` "hears what the user does, not what the program sets" (user vs api only); composed.py L696 heat reasons (unrelated) | tess-shell:surfaces/popup.py `_closed` reason (`dismissed`/`failed`/`app`/`escape`), close(op, why) | tre:`dismiss`/`closed` reasons; `selection_change` carries rows only [unverified whether a source field exists]; no per-change source enum | partial (user-vs-api convention in both) | vault:none found | none (no reason enum) |
| Focus recovery after close | tess-ui:overlays.py docstring L8 "focus goes back to where it was" | tess-shell:surfaces/popup.py `_free` L910-919 opener -> `restore_focus`; binder/build.py L705 `restore_focus` | tre:overlay.rs L277 `restore_focus: Option{NodeId}`; tree/layers.rs; engine-py window_layers.rs | yes (app code also restores itself in the shell) | vault:AC-FOC-*; AC-DLG-*; AC-MEN-* | `restore_focus` on a layer |
| Focus trap | tess-ui:overlays.py L87 modal "traps focus" (via modal layer) | tess-shell: none found | tre:overlay.rs L246 `modal` (blocks input, scopes focus); PR 328 `modal` role flag | no | vault:AC-DLG-*; AC-FOC-* | `modal` |
| Tooltip timing | tess-ui:overlays.py L25 opens 500 ms after hover, at once on keyboard focus; hover grace per ADR-0011 | tess-shell:binder/build.py, binder/marquee.py `tooltip_gate`, binder/tables.py; engine tooltips [unverified delay] | tre:`tooltip` role (node_props.rs L174, docs/guide/accessibility.md L77); hover rules docs/guide/events-and-input.md L48; no delay property found (only scrollbar `hover_delay_ms`) | yes (delay owned in app code in both) | vault:Tooltip#AC-TIP-1..; ADR-0004, ADR-0011 | `tooltip` role only |
| Drag threshold / cancel | tess-ui:docking.py `_drag_past_threshold` L470, `pointer_cancel` L425 | tess-shell:binder/controls.py Slide `dragging` L394-615 (no threshold; Escape cancel not found) | tre:tree/dispatch.rs L128 press on chosen row may become app drag; scrollbar thumb drag L122; UXREQ-007 asks Escape cancel and edge auto-scroll (not done) | partial | vault:Drag and Drop#AC-DND-1..9; Drag and Drop Pattern#AC-DNP-1..14; UXREQ-007 | none |
| Scroll into view | tess-ui:scrolling.py L6 focus scrolls into view; answers `scroll_into_view`; a11y.py L34 | tess-shell:binder/controls.py L270 `child.tre.scroll_into_view()` | tre:tree/scroll.rs, tree/focus.rs, tree/container_selection.rs, tree/virtual_scroll.rs; engine-py `scroll_into_view` | no (both call tre) | vault:AC-SCB-*; UXREQ-002 | `scroll_into_view()`, focus scrolls itself |
| Keyboard shortcuts / chord registry | tess-ui:key_chords.py (`normalise`, `from_event`, `canonical_key`), chord_controls.py | tess-shell:services/shortcuts.py `ShortcutService` (compositor global shortcuts, Action list), schema/keys.py, config/settings.py | tre:input.rs L111-130 `KeyChord` (parse, exact modifier match; PR UXREQ-006); no registry | yes (chord text normalisation in tess-ui key_chords.py, schema/keys.py in shell) [unverified equal] | vault:Key Chord Field#AC-KCF-1..16; ADR-0019; ADR-0021; AC-KBN-* | `KeyChord.parse` (only per-node chord e.g. terminal `escape_chord`) |

## Reusable from tre today

| Area | Property / event names | Source |
|---|---|---|
| Anchored layers (PR 346) | `show_layer(node, anchor, placement, modal, dismissible, offset, flip)`; `placement` sides below/above/start/end and points top_start/top_end/bottom_start/...; `align` start/centre/end; `layer_viewport_margin`, `layer_flip_threshold`; read-back `layer_placement`; events `dismiss`, `closed` | tre:docs/guide/layers.md; overlay.rs |
| Layer focus | `modal`, `restore_focus`, `dismiss_on_escape`, `dismiss_on_outside_click` | tre:overlay.rs L239-277 |
| Selection (PR 350, 353) | `selection_mode` none/single/multiple, `selection`, `selection_anchor` (get), `select_all_key`, `select_on_focus`, event `selection_change`; container children selectable; Tab/click skip unselectable | tre:docs/guide/nodes-and-layout.md L563-581 |
| Roles and AT (PR 328) | `expanded`, `checked` (mixed), `set_size`, `pos_in_set`, `orientation`, `modal`, `active_descendant`, plus 18 roles incl. `tooltip` | tre:node_props.rs L89-105; docs/guide/accessibility.md |
| State layers (PR 335) | `hover_layer`, `pressed_layer`, `focus_layer` | node_props.rs L115-117 |
| Outline (PR 336) | `outline`, `focus_outline` (ring outside the box) | tre commit 7c23d8b9 |
| Misc | `scroll_into_view()`, `KeyChord` parse and exact match, text-selection Shift+arrows/Home/End | tre:tree/scroll.rs; input.rs; dispatch.rs L350 |

Not in tre (gaps for a standard): roving/focus group, typeahead, tooltip delay, drag threshold and Escape cancel (UXREQ-007), change-reason enum, shortcut registry.

## Where the vault already defines the behaviour

The vault defines the contract, with acceptance criteria: [[Keyboard Navigation]] (AC-KBN: focus order, roving focus, F6, shortcut display, Shortcut Mode), [[Selection]] (AC-SLT: models, ranges, anchor, announcements, selection_source), [[11 Interaction]] (AC-INT: Escape order, typeahead, chords, double click, drag), [[12 Overlays]] and [[Popup]], [[Menu]], [[Dialog]], [[Tooltip]] (AC-OVL, AC-POP, AC-MEN, AC-DLG, AC-TIP: dismissal, placement, focus return, grace), [[Anchored Placement]] (AC-ANC), [[Active Descendant]] (AC-ADE), [[Drag and Drop]] and [[Drag and Drop Pattern]] (AC-DND, AC-DNP), [[Scrollbar and Scroll Container]] (AC-SCB: keys, scroll into view), [[Focus Ring]] and [[State Layers]] (AC-FOC, AC-STL). Per-id mapping to upstream behaviours was not done: the tables cite note prefixes.

## Open questions

1. Standard form: a vault chapter of behaviour contracts (one note per behaviour with testable ACs, as for components), or a shared library API? The vault can only specify contracts (hard rule 5, no engine API).
2. Where should the shared behaviour live? tre already owns selection, layers, focus restore and state layers; roving focus, typeahead, a change-reason enum, a tooltip delay service and a shortcut registry are tre gaps (UXREQ candidates under ADR-0020) or toolkit code in tess-ui that tess-shell reuses.
3. The vault has no contract for the 10 missing components (autocomplete, avatar, command, image-cropper, menubar, otp-input, password-input, rating, timeline, waterfall): which are in scope for Tesserae (a desktop shell has no use for some)?
4. Upstream behaviours the vault lacks as named jobs (for example direct-manipulation, gauge, preferences, storage, canvas, forms) need a decision on whether each becomes a pattern or stays out.
5. The change-reason vocabulary (pointer, keyboard, api; tre now has `selection_source`) could become one enum across the three projects: confirm the names.
6. Items marked `[unverified]` need a read by the project bots before they feed a decision (tess-ui selection widgets, the shell tooltip delay, tess-ui and tess-shell chord normalisation).

Back to [[70 Adoption]].
