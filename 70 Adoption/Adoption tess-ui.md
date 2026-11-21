---
title: Adoption tess-ui
type: adoption
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [adoption, tess-ui, worklist, audit]
related: ["[[17 Conformance]]", "[[Test Method]]", "[[Audit Template]]", "[[70 Adoption]]", "[[Owner Feedback 2026-11-20]]", "[[Spacing and Density]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Tree]]", "[[Tree Node]]", "[[Form Row]]", "[[Theme Following the System]]", "[[Open Questions]]", "[[80 Requests]]", "[[Adoption tre]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]", "[[ADR-0020 The engine never blocks the design]]", "[[UXREQ-001 Two-axis scroll view with the specified scrollbar]]", "[[UXREQ-002 Virtual list keys and scroll to index]]", "[[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]]", "[[UXREQ-004 Accessibility roles]]", "[[UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input]]", "[[UXREQ-007 Drag cancel by Escape and edge auto-scroll]]", "[[UXREQ-008 Outline property for focus rings]]", "[[UXREQ-009 First frame hold]]"]
depends_on: ["[[17 Conformance]]", "[[Test Method]]", "[[Owner Feedback 2026-11-20]]"]
---

# Adoption tess-ui

> [!info] Summary
> The ordered worklist of what tess-ui (the toolkit, its stylesheets and the shell configuration app) has to change to meet the specifications, built from the `Status in code` tables of the vault and checked against the tess-ui source on origin/main. It is an adoption note, not an audit: no criterion was run, and nothing here is a conformance claim ([[17 Conformance]]). Each row names the failing criteria, the file that shows the failure, and the change to make. A project bot confirms or corrects every row before it becomes an issue ([[17 Conformance]], audit workflow).

## Header

| Field | Value |
|---|---|
| Audit target | tess-ui: toolkit (`tess-ui:src/tess_ui`), view stylesheets (`tess-ui:src/tess_ui/views`), docs (`tess-ui:docs`), the shell configuration app (`tess-ui:apps/shell_config`) |
| Commit read | origin/main `c0cedca42626cf32c9d0e6b0115586e990bfbce5` ("App: dark=True without a seed warns once (#331)"), committed 2026-11-20 |
| Date | 2026-11-21 |
| Method | Desk audit by reading, in two passes. Pass 1: every `Status in code` row for tess-ui in the foundation, chapter, component and pattern notes (`partly meets`, `absent`, failing ids). Pass 2: the claims that decide severity re-read in the source of origin/main with `git show`. Result values follow [[17 Conformance]]: a row is a `fail` only where the source shows it; a claim not confirmed in source is marked unverified. No harness was run, so no row is a `pass` |
| Conformance level | none claimed; Level 1 needs no `fail` and no `not run` ([[17 Conformance]]) |
| Dropped | findings that origin/main already fixes are listed under "Fixed on origin/main" and are not in the table |

Severity:

| Level | Meaning |
|---|---|
| P0 | blocks use: an owner-feedback item of [[Owner Feedback 2026-11-20]] (F1 to F9) still failing, a keyboard trap, content unreachable, a missing accessible name on a core control |
| P1 | breaks a rule: fails a MUST criterion |
| P2 | polish: a SHOULD criterion, a value off the table by a small amount, a component no app uses |

No keyboard trap was found in the code read: the modal layers keep Tab inside by design and return focus on close (AC-DLG-7 meets by reading), and no dead end was read in the dock and splitter keys. No P0 row is a keyboard trap; a desk audit does not prove their absence.

## Fixed on origin/main

| Item | Evidence | Note |
|---|---|---|
| F2 hide on pointer leave and on press | `tess-ui:src/tess_ui/composed.py` `_wire_tooltips`: `pointer_leave` runs `away`, `pointer_down` runs `away` (pull request 328) | the other F2 triggers remain open: TUI-011 |
| F7 single-line field text top aligned | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_Stylesheet.tdl` line 10: `TextInput` `Padding: 8`, field centred by padding (pull request 329) | centring by padding only, see TUI-024 |
| F1 for the config app | `tess-ui:apps/shell_config/src/tess_shell_config/app.py` line 50 sets `theme_seed` (pull request 330) | the toolkit default remains open: TUI-001 |
| F5 for the config tree label | `Main_Stylesheet.tdl` line 14: label `Flex: expand_horizontal`, `Min_Width: 0` | the toolkit default remains open: TUI-023 |
| Warning for `dark=True` with no seed | `tess-ui:src/tess_ui/app.py` `_warn_dark_needs_a_seed` (pull request 331) | a warning, not a scheme: TUI-001 |

## Summary by severity

| Severity | Rows |
|---|---|
| P0 | 8 |
| P1 | 39 |
| P2 | 22 |
| Total | 69 |

## Worklist

Ids are stable once the note leaves draft. Criteria are cited by id; the spec note column links the note that holds them. Evidence paths are relative to the repository root of tess-ui at the commit above.

### Density

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-001 | P0 | F1: an `App` with no `theme_seed` has no scheme and ignores `dark`, so every surface is the engine light default; only a warning exists now | AC-TH-9, AC-COL-6, AC-TH-11 | `tess-ui:src/tess_ui/app.py` (`_has_scheme`, `_warn_dark_needs_a_seed`) | Generate the baseline scheme when no seed is given so `dark` always reaches the surfaces | [[Theme Following the System]] |
| TUI-002 | P0 | F3: the toolkit `TreeNode` row is 56 px with left padding 16 plus 24 per level, right 16, gap 8, chevron 24 by 24; the specified indent is 20, 16, 12 dp | AC-TRN-02, AC-TRN-03, AC-TRN-04, AC-TRN-05, AC-TRN-06, AC-DEN-3, AC-DEN-5 | `tess-ui:src/tess_ui/views/TreeNode_Stylesheet.tdl` lines 10 to 17 | Replace the literals with density tokens: row 40, 32, 24; indent 20, 16, 12; chevron 24, 20, 16 | [[Tree Node]] |
| TUI-003 | P0 | F4: left padding of a depth-0 row is 16 px at every level; the chevron box edge must sit at 12, 8, 4 dp from the container edge | AC-TRN-03, AC-DEN-4 | `TreeNode_Stylesheet.tdl` line 10; config override `Main_Stylesheet.tdl` line 13 uses 4 where compact needs 8 | Set the depth-0 start padding to the density value; make the config app use compact 8 | [[Tree Node]] |
| TUI-004 | P1 | No density setting or token exists: every control has one size (Button, Icon Button, Switch, Checkbox, Radio, Slider, Chip, Menu item 48, List item 56, Tabs, Toolbar 64, Title Bar 40, Dock tab 48) | AC-DEN-2, AC-DEN-3, AC-DEN-6, AC-DEN-11, AC-BTN-1, AC-ICB-1, AC-SWI-1, AC-CHK-1, AC-RAD-1, AC-SLD-1, AC-CHP-1, AC-MEN-1, AC-MEN-3, AC-TBS-1, AC-TTB-1, AC-DKP-1 | `tess-ui:src/tess_ui/views/*_Stylesheet.tdl`, `tess-ui:src/tess_ui/controls.py` (`TARGET_SIZE` 48) | Add a project and per-container density setting with the three levels of [[ADR-0002 Desktop density levels and target sizes]], then drive every size from it | [[Spacing and Density]] |
| TUI-005 | P1 | Spacing and size literals off the token scale (14 in the snackbar text padding, 18 for dock close, 16 for handles) | AC-DEN-1, AC-BLK-FLX-2, AC-DEN-7 | `tess-ui:src/tess_ui/views/Snackbar_Stylesheet.tdl`; `tess-ui:src/tess_ui/docking.py` (`CLOSE_SIZE` 18, `HANDLE_SPAN` 16) | Replace with scale values; raise hit areas to 24 dp | [[Spacing and Density]] |
| TUI-006 | P1 | List item heights 56, 72, 88 and padding 16 with no density; divider inset on one side; Accordion header 56 (spec 40) | AC-LSI-02, AC-LSI-03, AC-LSI-10, AC-ACC-01, AC-ACC-02 | `tess-ui:src/tess_ui/views/ListItem_Stylesheet.tdl`; `tess-ui:src/tess_ui/views/Accordion_Stylesheet.tdl` | Move heights and paddings to the density table; inset the divider at both ends | [[List Item]] |
| TUI-007 | P2 | Icon button sizes xs to xl are 32 to 136 px, not the 40, 32, 28 levels; no 48 dp touch target around a 40 dp button | AC-ICB-1, AC-ICB-2 | `tess-ui:src/tess_ui/views/IconButton_Stylesheet.tdl` | Map sizes to the density levels and add the touch target ring | [[Icon Button]] |

### Tooltips

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-010 | P0 | F8: the config app puts the tooltip on the `label_box` container, not on the label text; the toolkit lets any node carry a tooltip | AC-TIP-1, AC-TIP-2, AC-FRM-04, AC-FRM-05, AC-SWI-8 | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` line 449 (`Tooltip: <| item['doc'] |>` on `label_box`) | Move the tooltip to the smallest control (the label `Text`); have the toolkit warn on a tooltip on a container | [[Tooltip]] |
| TUI-011 | P0 | F2: a tooltip is not dismissed on scroll of an ancestor or on activation other than a press; only leave, press, focus loss and Escape are wired | AC-TIP-6, AC-TIP-7, AC-TIP-8 | `tess-ui:src/tess_ui/composed.py` `_wire_tooltips` (events `pointer_enter`, `pointer_leave`, `pointer_down`, `focus`, `unfocus`, `long_press`); no `scroll` or trigger-removal hook beyond the `live` set | Hide on a `scroll` event of any ancestor, on click and on trigger hide | [[Tooltip]] |
| TUI-012 | P1 | The 150 ms hover grace exists for rich tooltips only; a plain tooltip is removed on leave and is not hit testable | AC-TIP-4, AC-TIP-17 | `composed.py` `leave` (`self._tip_rich(inst)` branch), `_show_tip` (`hit_testable=rich`) | Apply `TIP_GRACE` to plain tooltips and make them hit testable ([[ADR-0011 Tooltip hover grace for all tooltips]]) | [[Tooltip]] |
| TUI-013 | P1 | F9: a click on a switch drew tooltip text with no background; the cause is not recorded and no test covers it; the container fill falls back to `tokens.BASELINE` when no scheme exists | AC-TIP-10, AC-TIP-11, AC-TIP-15, AC-TIP-21, AC-SWI-5 | `composed.py` `_show_tip` (`scheme = self._scheme or tokens.BASELINE`); `tess-ui:tests/test_tooltip.py` | Add the pixel test of AC-TIP-11 and AC-SWI-5 and reproduce the demo; unverified on origin/main | [[Tooltip]] |
| TUI-014 | P1 | Tooltip text uses literal Roboto 12 and 14/500, so a theme `Typography` override does not reach it | AC-TYP-3, AC-TIP-13 | `composed.py` `_show_tip` (`font_family="Roboto"`, `font_size=12.0`) | Read the `label_small` and `label_large` roles from the theme | [[Tooltip]] |
| TUI-015 | P1 | The tooltip layer is placed by engine anchor with `dismissible=False`; clipping to the window at the four edges and layer-surface hosts is not tested | AC-TIP-15, AC-TIP-16 | `composed.py` `_show_tip` (`show_layer`) | Add the geometry tests; ask tre for the clip rule if the layer escapes | [[Tooltip]] |
| TUI-016 | P2 | Tooltip rules not verified: touch long press removal time, reduced motion, description equals the tooltip text, keyboard show only for `focus_visible` | AC-TIP-19, AC-TIP-22, AC-TIP-23, AC-TIP-10 | `composed.py` (`now`, `held`) | Add scripted tests | [[Tooltip]] |
| TUI-017 | P2 | No tooltip on tree labels, chip, colour swatch, icon picker cell, font list trigger, tab, status bar items | AC-TRN-08, AC-CHP-12, AC-CLP-12, AC-ICP-7, AC-FNT-11, AC-TBS-12 | `tess-ui:src/tess_ui/views/TreeNode_View.tdl`, `Chip_View.tdl`, `TokenButton_View.tdl` | Add the optional tooltip part to each | [[Tree Node]] |

### Scrolling and overflow

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-020 | P0 | F6: `ScrollView` scrolls one axis; content wider than a panel is unreachable and has no horizontal bar; every config scroll view is vertical | AC-SCB-03, AC-SCB-04, AC-SCB-18, AC-LAY-7, AC-LAY-8, AC-FRM-15, AC-TRE-13 | `tess-ui:src/tess_ui/scrolling.py` (a `Scroller` for one offset); `Main_View.tdl` lines 207, 341, 387, 1033 (vertical `ScrollView`s); no `ScrollView` view file on origin/main | Add a two-axis `ScrollView` and use it in the config panels; the engine side needs a tre hook ([[UXREQ-001 Two-axis scroll view with the specified scrollbar]]); until it exists nest a horizontal view inside a vertical one | [[Scrollbar and Scroll Container]] |
| TUI-021 | P1 | The scrollbar colour is `outline`, not `on_surface_variant` at 0.70 rest, 0.80 hover, 1.00 drag; thickness, hit strip and opacities are fixed in the engine today and need a tre hook | AC-SCB-01, AC-SCB-08, AC-SCB-09 | `tess-ui:docs/guide/layout.md` (Scrolling); `scrolling.py` | Needs a tre hook for the scrollbar tokens ([[UXREQ-001 Two-axis scroll view with the specified scrollbar]]); set the colour role in the stylesheet | [[Scrollbar and Scroll Container]] |
| TUI-022 | P1 | Wheel step, page step on lane press, drag mapping and content-clear-of-thumb rule are not set or verified | AC-SCB-11, AC-SCB-13, AC-SCB-16, AC-SCB-07 | `scrolling.py`; `tess-ui:tests/` (none by AC id) | Add geometry tests; the wheel step, page step and lane click need a tre hook ([[UXREQ-001 Two-axis scroll view with the specified scrollbar]]) | [[Scrollbar and Scroll Container]] |
| TUI-023 | P1 | `Text` and `Link` default to `Overflow: clip`; ellipsis is opt-in per node. The `TreeNode` label already ellipsizes (`Overflow: ellipsis`, `TreeNode_View.tdl` line 60) but has no `Min_Width`, so a long label can still push the row wider than the container (F5 for the toolkit tree label) | AC-TXT-3, AC-TXT-14, AC-LNK-7, AC-TRN-07, AC-LAY-3, AC-LAY-6 | `tess-ui:docs/components/text.md`; `tess-ui:src/tess_ui/views/TreeNode_View.tdl` line 60; `TreeNode_Stylesheet.tdl` (label has no `Min_Width`) | Default single-line text to ellipsis and give the tree label `Min_Width: 0` and `Flex: expand_horizontal` | [[Text]] |
| TUI-024 | P1 | F7: single-line field text is centred by hand-tuned padding, valid only for one line box height; the engine has no vertical-align and needs a tre hook | AC-TXF-1, AC-TXF-2, AC-TXF-4, AC-FRM-11, AC-DEN-9, AC-TXT-5 | `Main_Stylesheet.tdl` line 10 (`Padding: 8`); `tess-ui:src/tess_ui/views/TextField_Stylesheet.tdl` | Use the vertical-align hook of [[UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input]] when it exists; until then compute the padding from the role line height | [[Text Field]] |
| TUI-025 | P1 | Path and crumb buttons do not truncate in the middle; status bar texts have no ellipsis; tab and chip labels have no `Max_Lines` | AC-FDL-11, AC-FDL-12, AC-STB-3, AC-TBS-12, AC-CHP-11 | `tess-ui:src/tess_ui/views/FileDialog_View.tdl`, `StatusBar_View.tdl`, `Tabs_View.tdl` | Add the ellipsis and the middle-truncation rule | [[File Dialog]] |
| TUI-026 | P2 | A tab strip has fixed `Tab_Width` 120 and no scrolling when tabs overflow; dock tab strip has no overflow rule | AC-TBS-3, AC-TBS-13, AC-DKP-12, AC-DKP-14 | `tess-ui:src/tess_ui/views/Tabs_View.tdl`; `tess-ui:src/tess_ui/docking.py` (`_tab`) | Scroll or overflow-menu the strip | [[Tabs]] |

### Trees and lists

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-030 | P1 | Left does not move to the parent and Right does not move to the first child of an open branch; `*` is absent | AC-TRE-04, AC-TRE-05, AC-TRE-08 | `tess-ui:src/tess_ui/composed.py` (`Focus_Group`, `_typeahead`) | Add the tree key handlers | [[Tree]] |
| TUI-031 | P1 | The tree name is the literal "Tree"; children are not in a `group`; no multi select; no Page keys; no empty-state slot | AC-TRE-01, AC-TRE-10, AC-TRE-11, AC-TRE-16, AC-TRE-18 | `tess-ui:src/tess_ui/views/Tree_View.tdl`, `TreeLevel_View.tdl` | Make the name a required parameter; add the group, slot and keys | [[Tree]] |
| TUI-032 | P1 | Hover, focus and press layers are absent from the tree row stylesheet | AC-TRN-10 | `TreeNode_Stylesheet.tdl` (no state layer rule) | Add the 8, 10, 10 percent layers | [[Tree Node]] |
| TUI-033 | P1 | A plain list has no roving focus, no type-ahead, no Home and End, no empty slot | AC-LST-02, AC-LST-03, AC-LST-04, AC-LST-05, AC-LST-06, AC-LST-09 | `tess-ui:src/tess_ui/views/ListItem_View.tdl`; no `List` view | Add a `List` view with `Focus_Group: vertical` and type-ahead | [[List]] |
| TUI-034 | P1 | Trees have no virtualisation; a long tree builds every row | AC-TRE-12, AC-LAY-11, AC-LAY-13 | `Tree_View.tdl` | Build the tree on `VirtualList` with set size and position; needs the tre hooks of [[UXREQ-002 Virtual list keys and scroll to index]] (keys, scroll to index) and [[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]] (set size and position) | [[Tree]] |
| TUI-035 | P2 | No multi selection in Tree, List or NodeGraph; no start indicator | AC-SLT-1, AC-SLT-2, AC-SLT-3, AC-SLT-9 | `tess-ui:docs/guide/lists.md` ("Not built: selecting several") | Add selection models | [[Selection]] |
| TUI-036 | P2 | Choice picker, font list and icon picker use roles `list` and `listitem`, not `listbox` and `option`; no arrow, Home, End or type-ahead in the picker list | AC-CHO-2, AC-CHO-3, AC-CHO-5, AC-CHO-6, AC-FNT-6, AC-ICP-6, AC-FDL-2 | `Main_View.tdl` (`picker_list`); `tess-ui:src/tess_ui/views/FontList_View.tdl` | Use listbox roles (needs the tre hook of [[UXREQ-004 Accessibility roles]]) and the roving group | [[Choice Picker]] |

### Forms and fields

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-040 | P1 | The form is hand built: no `FormRow` view; the error line has no icon; no narrow stacked layout | AC-FRM-09, AC-FRM-14, AC-FRM-01, AC-FRM-06 | `Main_View.tdl` (`form_item`, `row_error`, `reset_button`) | Ship a `FormRow` view with these parts | [[Form Row]] |
| TUI-041 | P1 | The text field disabled state is a whole-field 0.38 opacity, not the per-part scheme; no density | AC-TXF-12, AC-TXF-3 | `TextField_Stylesheet.tdl` | Use the per-part disabled roles | [[Text Field]] |
| TUI-042 | P1 | The plain `TextInput` has no error, helper or required marker; no form summary with links; no re-validation rule | AC-VAL-6, AC-VAL-2, AC-VAL-9, AC-VAL-3 | `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`Refused`), `problems.py` | Add the validation slots to the field view | [[Validation]] |
| TUI-043 | P1 | The spin box field role is `textbox`, not `spinbutton`; time input fields and the config number widget do not use it | AC-SPN-10, AC-TMI-9, AC-SPN-1 | `tess-ui:src/tess_ui/controls.py` (`SpinBox`); `widgets.py` (`NumberWidget`) | Set `spinbutton` with value, min and max | [[Spin Box]] |
| TUI-044 | P1 | Checkbox sets colours only for error, with no `invalid` and no `mixed`; radio groups have no `radiogroup` node | AC-CHK-8, AC-RAD-7, AC-SEG-6, AC-TMP-9, AC-TLB-8 | `controls.py` (`Checkbox`, `RadioGroup`); `Toolbar_View.tdl` (role `group`) | Set the group roles in the views; `mixed` needs a tre hook ([[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]]) and `radiogroup` another ([[UXREQ-004 Accessibility roles]]) | [[Checkbox]] |
| TUI-045 | P2 | A disabled filled Button and Icon Button fade the whole control instead of the 12 and 38 percent scheme; same for FAB, Badge, Segmented | AC-BTN-6, AC-ICB-7, AC-FAB-5, AC-BDG-9, AC-SEG-3 | `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl`, `Fab_Stylesheet.tdl` | Use the per-part disabled colours | [[Button]] |
| TUI-046 | P2 | Slider has no stop indicator or value text; Key Chord Field button is 56 at every density | AC-SLD-11, AC-SLD-12, AC-KCF-11 | `controls.py` (`Slider`); `KeyChordField_Stylesheet.tdl` | Add both | [[Slider]] |
| TUI-047 | P2 | Search Escape closes and never clears; no Up and Down from the input into the rows | AC-SRB-5, AC-SRB-6 | `tess-ui:src/tess_ui/views/SearchBar_View.tdl` | Add the two key rules | [[Search]] |

### Roles and accessibility

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-050 | P0 | An icon-only FAB without `Label` has no accessible name and no tooltip | AC-FAB-8, AC-FAB-9 | `tess-ui:src/tess_ui/views/Fab_View.tdl`, `tess-ui:src/tess_ui/widgets/buttons.py` (`fab`) | Make `Label` required for an icon-only FAB | [[Floating Action Button]] |
| TUI-051 | P1 | A routed screen change moves no focus and sends no announcement; an unmatched route raises `KeyError`; `app.py` has no `announce` and `focus_first` calls | AC-RTV-9, AC-RTV-10, AC-RTV-13 | `tess-ui:src/tess_ui/app.py` (`navigate`, `show`; grep finds no `announce`) | Focus the new screen heading, announce the title, fall back to home | [[Routed View]] |
| TUI-052 | P1 | No code moves focus to the first control when a window opens; the `spec/window.py` docstring example shows `min_width: 480` and `min_height: 320` as sample values, and the defaults of a Window spec without the keys are unconfirmed (the `App` constructor defaults are 0, `app.py` line 228); `system_menu` off by default | AC-WIN-6, AC-WIN-1, AC-WIN-10 | `tess-ui:src/tess_ui/spec/window.py`, `app.py` | Confirm the Window spec defaults, set them per the note and focus the first control after the first frame | [[Window]] |
| TUI-053 | P1 | A Dialog does not focus a default action or the first field ("not built"); a modal menu opened by pointer is not focused | AC-DLG-6, AC-KBN-9, AC-MEN-14 | `tess-ui:src/tess_ui/views/Dialog_View.tdl`; `tess-ui:src/tess_ui/views/Menu_View.tdl` line 32 (`Focus_First` default false) | Default the focus to the safe action and set `Focus_First` true | [[Dialog]] |
| TUI-054 | P1 | The toolbar in the config app has seven Tab stops (no `Focus_Group`), no overflow, role `group` not `toolbar`; the shipped `Toolbar` assumes 44 px per item | AC-TLB-4, AC-TLB-5, AC-TLB-6, AC-TLB-8 | `Main_View.tdl` line 17 (`toolbar` container); `Toolbar_View.tdl` | Use the shipped `Toolbar` with `Focus_Group: both` and measured overflow; the `toolbar` role needs a tre hook ([[UXREQ-004 Accessibility roles]]) | [[Toolbar]] |
| TUI-055 | P1 | Splitter and Dock handle role is `slider`, not `separator`; Enter does nothing; Home and End can collapse a pane to 0 in the Python `splitter()`; handle 16 dp, not 24 | AC-SPL-10, AC-SPL-4, AC-SPL-3, AC-SPL-6, AC-SPL-1, AC-DCK-10, AC-DCK-2 | `tess-ui:src/tess_ui/widgets/containment.py` (`HANDLE_SPAN`), `tess-ui:src/tess_ui/composed.py` (`_wire_splitters`) | Set the role, add Enter collapse and minimums, raise the hit area | [[Splitter]] |
| TUI-056 | P1 | Snackbar role is `alert` not `status`, action default 4000 ms, no keyboard path to the action, queue unbounded | AC-SNK-3, AC-SNK-4, AC-SNK-9, AC-SNK-7, AC-SNK-5 | `tess-ui:src/tess_ui/views/Snackbar_View.tdl`, `SnackbarHost_View.tdl` | Set role (`status` needs a tre hook, [[UXREQ-004 Accessibility roles]]) and durations; add a chord to the action | [[Snackbar]] |
| TUI-057 | P1 | The focus ring is not recomputed on resize; ring clip in scroll containers not verified | AC-FOC-6, AC-FOC-5, AC-FOC-8 | `tess-ui:src/tess_ui/focusring.py` | Recompute on layout change; a ring outside the border box and clear of a clipping ancestor needs a tre hook ([[UXREQ-008 Outline property for focus rings]], held) | [[Focus Ring]] |
| TUI-058 | P2 | No real screen reader run; no `active_descendant` support; Date picker, Tabs, Time picker lack grid, `tabpanel` and `radiogroup` roles | AC-AXT-12, AC-ADE-1, AC-ADE-8, AC-TBS-5, AC-DTP-1 | `tess-ui:src/tess_ui/a11y.py`; `tess-ui:tests/test_a11y*.py` | Run Orca; add the roles (`grid` and `radiogroup` need a tre hook, [[UXREQ-004 Accessibility roles]]) | [[Accessibility Tree]] |
| TUI-059 | P2 | Carousel caption is `#FFFFFF` on a 32 percent band, 2.2:1 over white; colour literals exist in stylesheets | AC-CRS-10, AC-COL-5, AC-COL-9 | `tess-ui:src/tess_ui/views/Carousel_Stylesheet.tdl` | Use roles and check the composited pair | [[Carousel]] |

### Theming

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-060 | P0 | F1 on macOS and Windows: the app starts dark and flips after the window opens, a visible flash; no hold of the first frame; Linux reads the OS at construction | AC-TH-1, AC-TH-2, AC-TH-7, AC-TH-8 | `tess-ui:src/tess_ui/app.py` (`_os_dark`, `_adopt_os_appearance`), `tess-ui:src/tess_ui/follow.py` | Hold the first frame until the platform answers or 200 ms pass; the hold needs a tre window feature ([[UXREQ-009 First frame hold]], held) | [[Theme Following the System]] |
| TUI-061 | P1 | The override is not stored: `set_dark` changes the live value only | AC-TH-4, AC-TH-5, AC-TH-6 | `app.py` (`set_dark`) | Add a persistent store with a corrupt-value fallback | [[Theme Following the System]] |
| TUI-062 | P1 | The no-theme baseline overlays 2021 values and differs from the 2022 baseline in 19 of 49 light roles | AC-COL-2 | `tess-ui:src/tess_ui/tokens.py` (`BASELINE`) | Replace with the published baseline | [[Colour Roles]] |
| TUI-063 | P1 | No contrast script, so required pairs and the shipped theme files are unchecked | AC-COL-3, AC-COL-4 | `tess-ui:tests/` | Add the script to CI | [[Colour Roles]] |
| TUI-064 | P1 | The scrim is a literal, not the `scrim` role at 0.32: `overlays.py` defines `SCRIM = "#00000052"` and uses it as the background of the modal Dialog, SideSheet and NavigationDrawer scrim containers, and the modal-window scrim of `appwindows.py` is `fill=(0, 0, 0, 82)`, so a `Scrim` override does not reach them. `Dialog_Stylesheet.tdl` has no baked scrim (its header says the scrim is the modal Overlay's), and the declarative `Overlay` path already uses `scrim@32%` | AC-SCR-3, AC-NDR-11, AC-SSH-6 | `tess-ui:src/tess_ui/overlays.py` (`SCRIM` line 44; used at lines 182, 470 and 491), `tess-ui:src/tess_ui/appwindows.py` lines 73 to 74; the declarative path is `tess-ui:src/tess_ui/spec/build.py` line 727 | Use the `scrim` role at 0.32 in `overlays.py` and `appwindows.py` | [[Scrim]] |
| TUI-065 | P1 | Tracking is 0 for all 15 type roles; component sheets carry shape literals (12, 16, 28, 8, 24, 20, 3) | AC-TYP-2, AC-SHP-4, AC-C04-8 | `tess-ui:src/tess_ui/tokens.py` (`TYPE_SCALE`, `MD3_TRACKING`); `Button_Stylesheet.tdl` | Set tracking; use shape tokens | [[Typography]] |
| TUI-066 | P2 | Elevation holds the level index only, with no dp value; Expressive tokens absent | AC-ELV-1, AC-ELV-7 | `tokens.py` (`ELEVATION_LEVELS`) | Store the dp values | [[Elevation]] |

### Motion and state feedback

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-070 | P1 | `emphasized` is (0.2, 0, 0, 1) in `theme.py` and (0.3, 0, 0, 1) in `spec/transition.py` | AC-MOT-2 | `tess-ui:src/tess_ui/theme.py` line 47; `tess-ui:src/tess_ui/spec/transition.py` line 38 | Use one curve | [[Motion]] |
| TUI-071 | P1 | Stylesheets use the literals 150 and 200 ms instead of duration names; the reduced-motion path is not run | AC-MOT-6, AC-MOT-5, AC-SWI-10 | `TreeNode_Stylesheet.tdl` (`Transition { Background: 150 }`); `tess-ui:src/tess_ui/motion.py` | Use duration tokens; add the reduced-motion test | [[Motion]] |
| TUI-072 | P1 | Cards have no hover or dragged elevation; chevron rotation and the height easing of Accordion and extended FAB are absent; modal drawer does not slide | AC-CRD-2, AC-ACC-09, AC-EFB-9, AC-NDR-16, AC-TRN-13 | `Card_Stylesheet.tdl`, `Accordion_View.tdl`, `Fab_Stylesheet.tdl` | Needs a tre hook for an animatable height (no UXREQ yet; to be requested); add the rest | [[Card]] |
| TUI-073 | P2 | Loading: no delay or minimum display, no skeleton, no timeout rule | AC-LOD-1, AC-LOD-4, AC-LOD-6, AC-PRG-10 | `tess-ui:src/tess_ui/widgets/progress.py` | Add the delay rule | [[Loading States]] |
| TUI-074 | P2 | State layer precedence verified for plain nodes only; layers apply to `Rect` nodes | AC-STL-4 | `tess-ui:src/tess_ui/interaction.py`, `ripple.py` | Test the MD3 controls | [[State Layers]] |

### Overlays

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-080 | P1 | Side sheet and navigation drawer: no size-class switch, standard sheet takes no focus, role `group`; no escape cancel in dock drag | AC-SSH-4, AC-SSH-9, AC-SSH-10, AC-NDR-5, AC-DCK-6, AC-DND-7 | `tess-ui:src/tess_ui/views/SideSheet_View.tdl`, `NavigationDrawer_View.tdl`; `docking.py` | Switch by `width_class`; add Escape cancel (a dock drag needs a tre hook, [[UXREQ-007 Drag cancel by Escape and edge auto-scroll]], held) | [[Side Sheet]] |
| TUI-081 | P1 | Menus: item height 48 literal, submenu hover timer undocumented, `Focus_First` false | AC-MEN-1, AC-MEN-12, AC-MEN-14 | `Menu_Stylesheet.tdl`, `MenuItem_Stylesheet.tdl` | Move to density; add the hover timer | [[Menu]] |
| TUI-082 | P2 | Dialog: no 24 dp window inset, no full-screen switch below 328 dp; hiding the content beneath is unverified | AC-DLG-4, AC-DLG-14, AC-DLG-15 | `Dialog_Stylesheet.tdl` | Add the inset rule | [[Dialog]] |
| TUI-083 | P2 | Notifications: no banner view (hand-built in the config app), no dismiss, no queue limit or priority | AC-BNR-2, AC-BNR-4, AC-BNR-7, AC-NOT-10 | `Main_View.tdl` (`disk_banner`) | Ship a `Banner` view | [[Banner]] |

### Components not used by any app

No app or example in `tess-ui:apps` and `tess-ui:examples` uses these components, so their rows are desk findings only (the Inventory has the usage claim; confirm with the bot, question 6).

| ID | Sev | Finding | Failing AC | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TUI-090 | P2 | Pagination: no density; dots colour unverified | AC-PGN-1, AC-PGN-10 | `tess-ui:src/tess_ui/views/Pagination_Stylesheet.tdl` | Apply density and the dot role | [[Pagination]] |
| TUI-091 | P2 | Top app bar: actions beyond three are cut with no More menu; icon colour wrong | AC-TAB-10, AC-TAB-4 | `tess-ui:src/tess_ui/views/TopAppBar_View.tdl` | Add the overflow menu | [[Top App Bar]] |
| TUI-092 | P2 | Video player: no Home, End, Page keys; no slider value text; minutes unbounded | AC-VID-3, AC-VID-5, AC-VID-8 | `tess-ui:src/tess_ui/views/VideoPlayer_View.tdl` | Add keys and `value_text` | [[Video Player]] |
| TUI-093 | P2 | Node graph: no Escape, no keyboard zoom or pan, edges not exposed | AC-NGR-5, AC-NGR-6, AC-NGR-7, AC-NGR-8 | `tess-ui:src/tess_ui/widgets/media.py` (`node_graph`) | Add the key set | [[Node Graph]] |
| TUI-094 | P2 | Link, token button, list editor, date and time pickers, colour picker, icon picker: density and overflow fail by one rule each | AC-LNK-7, AC-TKB-1, AC-LED-1, AC-DTP-1, AC-TMP-1, AC-CLP-8, AC-ICP-1 | `tess-ui:src/tess_ui/views/*_Stylesheet.tdl` | Resolve with TUI-004 | [[Link]] |
| TUI-095 | P2 | Absent as blocks: Circle, Ring Block, Grid, Spacer, Terminal, Banner, Choice Picker | AC-BLK-CIR-1, AC-BLK-RNG-1, AC-BLK-GRD-1 | `tess-ui:src/tess_ui/views/` (none) | Decide per block whether tess-ui ships it ([[Open Questions]]) | [[Grid]] |

## Engine hooks needed

The tre hooks that tess-ui rows need, by request; the table of what each unlocks is in [[Adoption tre]]. Under [[ADR-0020 The engine never blocks the design]] the toolkit owns the look and the engine offers the hook.

- [[UXREQ-001 Two-axis scroll view with the specified scrollbar]]: TUI-020, TUI-021, TUI-022
- [[UXREQ-002 Virtual list keys and scroll to index]]: TUI-034
- [[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]]: TUI-034, TUI-044
- [[UXREQ-004 Accessibility roles]]: TUI-036, TUI-044, TUI-054, TUI-056, TUI-058
- [[UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input]]: TUI-024, TUI-065 (tracking on inputs)
- [[UXREQ-007 Drag cancel by Escape and edge auto-scroll]] (held): TUI-080
- [[UXREQ-008 Outline property for focus rings]] (held): TUI-057
- [[UXREQ-009 First frame hold]] (held): TUI-060
- [[UXREQ-006 Terminal escape chord and history scrollbar]]: TUI-095 (the Terminal block, if tess-ui ships it)
- No request yet: animatable height (TUI-072)

## AC coverage

Counts are approximate: they come from reading the free text of each `Status in code` table for tess-ui, not from runs. "Meeting" counts ids the row says meet or pass; "Partly" counts ids it says meet in part; "Failing" counts ids it says fail or are absent; "Not run or unmarked" is the rest. Notes whose tess-ui row is not applicable are left out. Rows for absent components count every criterion as failing.

| Note | ACs | Meeting | Partly | Failing | Not run or unmarked |
|---|---|---|---|---|---|
| [[Accessibility Tree]] | 13 | 0 | 0 | 2 | 11 |
| [[Accordion]] | 14 | 3 | 0 | 8 | 3 |
| [[Active Descendant]] (absent) | 8 | 0 | 0 | 8 | 0 |
| [[Anchored Placement]] | 9 | 1 | 0 | 0 | 8 |
| [[Application Window]] | 10 | 0 | 1 | 2 | 7 |
| [[Auto Hide]] | 19 | 0 | 0 | 0 | 19 |
| [[Badge]] | 9 | 0 | 2 | 4 | 3 |
| [[Banner]] | 12 | 0 | 2 | 5 | 5 |
| [[Bar]] | 20 | 0 | 0 | 0 | 20 |
| [[Bitmap]] | 6 | 0 | 0 | 0 | 6 |
| [[Box]] | 7 | 0 | 0 | 0 | 7 |
| [[Button Group]] | 11 | 0 | 1 | 7 | 3 |
| [[Button]] | 12 | 0 | 4 | 1 | 7 |
| [[Canvas]] | 6 | 0 | 0 | 0 | 6 |
| [[Card]] | 16 | 0 | 5 | 4 | 7 |
| [[Carousel]] | 15 | 0 | 4 | 5 | 6 |
| [[Checkbox]] | 13 | 0 | 3 | 4 | 6 |
| [[Chip]] | 14 | 0 | 2 | 9 | 3 |
| [[Choice Picker]] | 13 | 0 | 2 | 9 | 2 |
| [[Circle]] (absent) | 6 | 0 | 0 | 6 | 0 |
| [[Colour Picker]] | 16 | 9 | 0 | 5 | 2 |
| [[Date Picker]] | 15 | 0 | 2 | 10 | 3 |
| [[Dialog]] | 17 | 1 | 2 | 14 | 0 |
| [[Divider]] | 7 | 3 | 0 | 3 | 1 |
| [[Dock Panel]] | 14 | 0 | 0 | 13 | 1 |
| [[Dock]] | 15 | 5 | 1 | 5 | 4 |
| [[Drag and Drop]] | 9 | 1 | 0 | 1 | 7 |
| [[Extended Floating Action Button]] | 10 | 0 | 1 | 5 | 4 |
| [[File Dialog]] | 20 | 9 | 0 | 6 | 5 |
| [[FlexBox]] | 7 | 0 | 0 | 1 | 6 |
| [[Floating Action Button]] | 13 | 0 | 0 | 8 | 5 |
| [[Font List]] | 12 | 7 | 3 | 0 | 2 |
| [[Form Row]] | 16 | 2 | 1 | 4 | 9 |
| [[Frame]] | 24 | 0 | 0 | 0 | 24 |
| [[Grid]] (absent) | 6 | 0 | 0 | 6 | 0 |
| [[Icon Button]] | 10 | 2 | 0 | 3 | 5 |
| [[Icon Picker]] | 12 | 7 | 3 | 0 | 2 |
| [[Image]] | 12 | 0 | 0 | 7 | 5 |
| [[Key Chord Field]] | 16 | 0 | 4 | 6 | 6 |
| [[Launcher]] | 22 | 0 | 0 | 0 | 22 |
| [[Link]] | 12 | 0 | 5 | 2 | 5 |
| [[List Editor]] | 14 | 7 | 0 | 6 | 1 |
| [[List Item]] | 11 | 1 | 0 | 5 | 5 |
| [[List]] | 11 | 0 | 0 | 6 | 5 |
| [[Menu Item]] | 8 | 0 | 0 | 0 | 8 |
| [[Menu]] | 17 | 4 | 3 | 6 | 4 |
| [[Navigation Drawer]] | 18 | 1 | 5 | 8 | 4 |
| [[Navigation Rail]] | 17 | 2 | 1 | 10 | 4 |
| [[Node Graph]] | 12 | 0 | 0 | 3 | 9 |
| [[Pagination]] | 12 | 0 | 3 | 6 | 3 |
| [[Panel and Surface]] | 13 | 1 | 0 | 7 | 5 |
| [[Path Block]] | 7 | 0 | 0 | 0 | 7 |
| [[Peek]] | 18 | 0 | 0 | 0 | 18 |
| [[Popup]] | 16 | 1 | 3 | 6 | 6 |
| [[Progress Indicator]] | 12 | 0 | 0 | 6 | 6 |
| [[Radio Button]] | 12 | 0 | 3 | 4 | 5 |
| [[Rectangle Block]] | 6 | 0 | 0 | 0 | 6 |
| [[Ring Block]] (absent) | 6 | 0 | 0 | 6 | 0 |
| [[Routed View]] | 14 | 3 | 0 | 5 | 6 |
| [[SVG]] | 10 | 0 | 0 | 7 | 3 |
| [[ScrollBox]] | 5 | 0 | 0 | 0 | 5 |
| [[Scrollbar and Scroll Container]] | 21 | 0 | 0 | 3 | 18 |
| [[Search]] | 17 | 0 | 5 | 4 | 8 |
| [[Segmented Button]] | 12 | 2 | 1 | 5 | 4 |
| [[Side Sheet]] | 16 | 1 | 2 | 10 | 3 |
| [[Slider]] | 15 | 0 | 3 | 8 | 4 |
| [[Snackbar]] | 14 | 0 | 0 | 11 | 3 |
| [[Spacer]] (absent) | 5 | 0 | 0 | 5 | 0 |
| [[Spin Box]] | 16 | 1 | 1 | 6 | 8 |
| [[Split Button]] | 11 | 0 | 3 | 3 | 5 |
| [[Splitter]] | 15 | 4 | 0 | 8 | 3 |
| [[Status Bar]] | 12 | 2 | 1 | 4 | 5 |
| [[Switch]] | 12 | 0 | 4 | 3 | 5 |
| [[Tabs]] | 16 | 0 | 1 | 9 | 6 |
| [[Terminal]] (absent) | 8 | 0 | 0 | 8 | 0 |
| [[Text Editor]] | 8 | 0 | 0 | 0 | 8 |
| [[Text Field]] | 16 | 0 | 0 | 8 | 8 |
| [[Text Selection]] | 10 | 3 | 0 | 0 | 7 |
| [[Text]] | 14 | 1 | 3 | 4 | 6 |
| [[Time Input]] | 14 | 0 | 2 | 4 | 8 |
| [[Time Picker]] | 14 | 0 | 3 | 7 | 4 |
| [[Title Bar]] | 18 | 4 | 0 | 6 | 8 |
| [[Toggle]] | 8 | 0 | 0 | 0 | 8 |
| [[Token Button]] | 12 | 1 | 0 | 7 | 4 |
| [[Toolbar]] | 13 | 1 | 0 | 6 | 6 |
| [[Tooltip]] | 23 | 0 | 5 | 11 | 7 |
| [[Top App Bar]] | 11 | 2 | 1 | 4 | 4 |
| [[Tree Node]] | 14 | 3 | 0 | 6 | 5 |
| [[Tree]] | 18 | 3 | 0 | 3 | 12 |
| [[Video Player]] | 14 | 0 | 3 | 8 | 3 |
| [[Volume OSD]] | 15 | 0 | 0 | 0 | 15 |
| [[Window]] | 14 | 3 | 0 | 3 | 8 |
| [[Drag and Drop Pattern]] | 14 | 3 | 0 | 3 | 8 |
| [[Empty States]] | 9 | 0 | 0 | 3 | 6 |
| [[Error States]] | 10 | 0 | 2 | 3 | 5 |
| [[Forms and Settings]] | 16 | 0 | 8 | 3 | 5 |
| [[Keyboard Navigation]] | 17 | 1 | 4 | 3 | 9 |
| [[Loading States]] | 11 | 0 | 3 | 3 | 5 |
| [[Notifications]] | 12 | 0 | 0 | 6 | 6 |
| [[Selection]] | 14 | 0 | 2 | 5 | 7 |
| [[Validation]] | 12 | 3 | 2 | 3 | 4 |
| Total (101 notes) | 1298 | 108 | 125 | 460 | 605 |

## Questions for the tess-ui bot

1. Does origin/main contain a two-way `ScrollView` (branch `feat/scrollview-two-way`)? If it merged, TUI-020 changes to a config-app change only.
2. Which origin/main test covers AC-TIP-11 or AC-SWI-5 (the background of tooltip text after a switch click, F9)? Can the demo be reproduced headless with `window.simulate`?
3. Does the toolkit tree keep a 16 plus 24 per level default on purpose, or can the density tokens replace it (TUI-002, TUI-003)?
4. Is a tooltip on a container intended anywhere beyond the config `label_box`, and can the toolkit reject it?
5. Does any route or window open set focus to a first control or announce the screen title that `app.py` does not show (TUI-051, TUI-052)?
6. Is the list of unused components (Pagination, Top App Bar, Video Player, Node Graph) still true after the latest merges?
7. Can the project add AC ids to test names so the next audit reads results from the runs ([[17 Conformance]], harness)?
8. Is a density setting planned, and at which level (project, container) will it be declared ([[ADR-0002 Desktop density levels and target sizes]])?
