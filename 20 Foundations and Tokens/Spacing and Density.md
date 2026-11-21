---
title: Spacing and Density
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, spacing, density, tokens]
related: ["[[07 Spacing and Density Rules]]", "[[10 Layout Overflow and Scrolling]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[Existing Tokens]]", "[[Tree]]", "[[Tree Node]]", "[[Text Field]]", "[[Icon Button]]", "[[Button]]", "[[Menu]]", "[[List]]", "[[Switch]]", "[[Iconography]]", "[[Typography]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]"]
---

# Spacing and Density

> [!info] Summary
> The canonical spacing steps, the three density levels (`default`, `compact`, `dense`) with every size they set, and the minimum target sizes. Material Design 3 (MD3) has no spacing tokens and no desktop density; this note records the Tesserae scale and the MD3 value each number departs from. Rules for choosing a level live in [[07 Spacing and Density Rules]].

Decision: [[ADR-0002 Desktop density levels and target sizes]]. Evidence: [[Owner Feedback 2026-11-20]] items F3 (tree indentation gaps), F4 (gap between the root chevron and the container edge), F7 (text top-aligned in single-line fields).

Unit: 1 dp = 1 px at scale factor 1.0. Projects write px and scale by the window scale factor (`tess-ui:src/tess_ui/app.py` `scale_factor`; `tre:docs/reference/window.md` `dpi_scaling`).

## Spacing steps

The grid is 4 dp. Every padding, margin and gap in a stylesheet is one of these nine steps.

| Step | dp | Use |
|---|---|---|
| `space.0` | 0 | no gap |
| `space.1` | 2 | half step: gap between a glyph and a badge, border-adjacent insets, ring offset. The only step off the 4 dp grid |
| `space.2` | 4 | dense padding, gap inside a dense control |
| `space.3` | 8 | compact padding, icon-to-label gap, gap between related controls |
| `space.4` | 12 | default row padding, text-field padding at default |
| `space.5` | 16 | gap between controls, panel padding |
| `space.6` | 24 | gap between groups |
| `space.7` | 32 | gap between sections |
| `space.8` | 48 | largest step, page margins |

Mapping: the shell tokens `$space.step_1` to `$space.step_8` hold 2, 4, 8, 12, 16, 24, 32, 48 (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` lines 46 to 53), so `step_n` equals `space.n` for n from 1 to 8; `space.0` has no shell token and is the literal 0. tess-ui has no spacing tokens; its stylesheets use literals and one off-grid value 14 (`tess-ui:src/tess_ui/views/Snackbar_Stylesheet.tdl` line 25), which fails [[#Acceptance criteria|AC-DEN-1]].

MD3 counterpart: MD3 defines no named spacing tokens; it uses a 4 dp grid and per-component values. Material Web component tokens use 4, 8, 12, 16 and 24 px (for example filled button `leading-space` 24 px and list item `top-space` 12 px in `tokens/versions/v0_192`, text field `leading-space` 16 px). Sources in the Sources section.

## Density levels

A density level sets the sizes below as one set. Levels are `default`, `compact` and `dense`. The level for a project or a container is set by a project ADR or a container property, not here ([[07 Spacing and Density Rules]]). Config-style tools use `compact`.

### Control and row heights

| Element | default | compact | dense | MD3 value | Reason for the difference |
|---|---|---|---|---|---|
| Button container height | 40 | 32 | 28 | 40 (`md.comp.filled-button.container.height`) | default equals MD3; compact and dense serve pointer use at desktop information density |
| Text field container height (single line) | 40 | 32 | 28 | 56 (`md.comp.filled-text-field.container.height`, latest tokens) | MD3 56 dp is a touch height with a floating label; desktop forms need more rows per screen. The 56 dp field stays available as the touch variant ([[Text Field]]) |
| Switch row (label plus switch) | 40 | 32 | 28 | track 32, state layer 40, touch target 48 (`md.comp.switch`) | the row equals the control height so rows align with buttons and fields; the painted track is smaller than the row |
| List row, single line | 40 | 32 | 24 | 48 for a list item inside a menu in Material Web (`$list-item-container-height` in `_md-comp-menu-item.scss`); the MD3 specification page gives 56 for one line #needs-verification | desktop rows hold one line of 14 dp text; 24 dp is the smallest row that still meets 24 dp target size |
| Tree row, single line | 40 | 32 | 24 | no MD3 counterpart | MD3 has no tree; the row follows the list row |
| Menu item | 40 | 32 | 28 | 48 (`$list-item-container-height` in `_md-comp-menu-item.scss`, Material Web) | desktop menus are dense; 28 dp keeps pointer targets above 24 dp |
| Icon button container | 40 | 32 | 28 | 40 (`md.comp.icon-button.container.height`) | same reason as button |
| Icon button icon size | 24 | 20 | 20 | 24 (`md.comp.icon-button.icon.size`) | at compact and dense the container shrinks by 8 to 12 dp and the 20 dp icon keeps 6 dp of margin |

Single-line text sits in the row with vertical centring by construction: the text line box (the line height of the [[Typography]] role, 20 dp for `body-medium`) is centred in the control height at every density, so the padding above and below differs by at most 1 px (see [[10 Layout Overflow and Scrolling]]).

### Horizontal sizes

| Element | default | compact | dense | MD3 value | Reason for the difference |
|---|---|---|---|---|---|
| Row horizontal padding (list row, tree row, menu item) | 12 | 8 | 4 | 16 (list item, text field `leading-space` 16 px, `tokens/versions/v0_192`) | desktop widths are narrow in side panels; 16 dp pads cost a quarter of a 240 dp panel |
| Icon-to-label gap | 8 | 8 | 4 | 16 (list item) | desktop icons are 20 dp or less, so 8 dp reads as a pair |
| Text field horizontal padding | 12 | 8 | 8 | 16 | same as row padding; dense keeps 8 so a caret is not at the border |
| Tree indent per level | 20 | 16 | 12 | no MD3 counterpart | the indent is smaller than the chevron box plus gap so levels nest without wide gutters (F3) |
| Tree chevron box (width and height) | 24 | 20 | 16 | no MD3 counterpart | box equals the 24 dp minimum target at default; at compact and dense the hit area extends beyond the box (see Target sizes) |
| Gap between a root chevron box and the container edge | equals the row horizontal padding: 12 | 8 | 4 | no MD3 counterpart | no extra margin on top of the row padding (F4) |
| Leaf spacer (a leaf row aligns its label with a sibling that has a chevron) | 24 | 20 | 16 | no MD3 counterpart | equals the chevron box |

Derived rule for a tree row at depth d (root is 0): the chevron box left edge is at `row_padding + d * indent`; the label left edge is at `row_padding + d * indent + chevron_box + icon_label_gap`. At default and depth 0 the label starts at 12 + 24 + 8 = 44 dp from the container edge; at dense and depth 0 it starts at 4 + 16 + 4 = 24 dp.

### Fixed values at all levels

| Item | dp | MD3 value |
|---|---|---|
| Spacing grid | 4 | 4 dp grid (applies to layout; see Sources) |
| Minimum pointer target (hit area), desktop | 24 | none (MD3 states 48 dp for touch) |
| Minimum pointer target (hit area), touch context | 48 | 48 (`md.comp.switch.touch-target-size`) |
| Scrollbar and focus ring sizes | see [[Focus Ring]] and [[Scrollbar and Scroll Container]] | not applicable |

## Target sizes

Sources: WCAG 2.2 SC 2.5.8 Target Size (Minimum), Level AA: the target for pointer input is at least 24 by 24 CSS pixels, with exceptions for spacing, equivalent controls, inline text and user-agent controls (see Sources).

- The hit area (the region that activates the control) is at least 24 by 24 dp at every density. The painted size may be smaller than the hit area; the hit area never is smaller than the painted size.
- In a touch context the hit area is at least 48 by 48 dp. A touch context is a window or container whose primary input is touch, set by the project. The level stays `default`; only hit areas grow, not painted sizes (a 40 dp button gets a 48 dp hit area).
- Adjacent hit areas do not overlap. Two targets closer than their hit areas allow are separated by `space.1` (2 dp) at least only when each has a 24 dp hit area.
- Chevron hit area in a tree: 24 dp wide and the full row height, extending into the row padding and the icon-to-label gap. At dense that is 4 dp padding + 16 dp box + 4 dp gap = 24 dp; the dense row height is 24 dp, which meets the minimum exactly.
- Painted icon at compact and dense (20 dp) sits in a container of 32 or 28 dp; the container is the hit area.

## Window size classes

Window size classes are taken from MD3 and have the same breakpoints in tess-ui (`tess-ui:src/tess_ui/tokens.py` `WIDTH_CLASSES`, `HEIGHT_CLASSES`). The rules that use them are in [[10 Layout Overflow and Scrolling]].

| Width class | Width in dp | Height class | Height in dp |
|---|---|---|---|
| compact | below 600 | compact | below 480 |
| medium | 600 to 839 | medium | 480 to 899 |
| expanded | 840 to 1199 | expanded | 900 and above |
| large | 1200 to 1599 | | |
| extra-large | 1600 and above | | |

A boundary value belongs to the larger class (width 600 is `medium`). Density is independent of the window size class: a compact-width window can use any density level.

## Tokens

| Token | Value |
|---|---|
| `space.0` to `space.8` | 0, 2, 4, 8, 12, 16, 24, 32, 48 dp |
| `density.control_height` | 40, 32, 28 |
| `density.row_height` | 40, 32, 24 |
| `density.menu_item_height` | 40, 32, 28 |
| `density.icon_button_container` | 40, 32, 28 |
| `density.icon_button_icon` | 24, 20, 20 |
| `density.row_padding_x` | 12, 8, 4 |
| `density.icon_label_gap` | 8, 8, 4 |
| `density.field_padding_x` | 12, 8, 8 |
| `density.tree_indent` | 20, 16, 12 |
| `density.chevron_box` | 24, 20, 16 |
| `target.min` | 24 |
| `target.touch` | 48 |

Each `density.*` token holds three values in the order default, compact, dense. Token names are the specification vocabulary; a project maps them to its own names ([[ADR-0001 MD3 role names are the specification vocabulary]]).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/*_Stylesheet.tdl`, `tess-ui:src/tess_ui/controls.py` | absent: no density token or setting. Tree rows are 56 px, `Compact` 40 px, with padding left 16 plus 24 per level, right 16, gap 8, chevron box 24 by 24, leaf spacer 24 (`TreeNode_Stylesheet.tdl`, `TreeNode_View.tdl`, `Tree_View.tdl`). Fails AC-DEN-2, AC-DEN-4, AC-DEN-5 at the library defaults. The config app overrides left 4 plus 16 per level, right 4, gap 4 (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_Stylesheet.tdl`), close to compact/dense but not equal |
| tess-ui | single-line TextInput in the config app: 32 px high, 7 px top and bottom, 8 px left and right | partly meets: AC-DEN-2 at compact passes for height; text is centred by padding, not by an engine property |
| tess-ui | touch target | partly meets: `TARGET_SIZE` 48 (`tess-ui:src/tess_ui/controls.py` line 45) is the touch minimum; no 24 dp desktop rule |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | partly meets: spacing steps match `space.1` to `space.8` (AC-DEN-1); no density setting; Button 32, MenuItem 28, list rows 40 are literals; checkbox box 18 and toggle 40 by 22 are below 24 dp hit area unless the row is the target |
| tre | `tre:ARCHITECTURE.md` section 7 | not applicable: the engine has no spacing scale or density; `touch_target_slop` default 0 |

Evidence: [[Owner Feedback 2026-11-20]] F3, F4, F7.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Three density levels (default, compact, dense) | MD3 specifies touch-first sizes; desktop forms and trees need more rows per screen | [[ADR-0002 Desktop density levels and target sizes]] |
| Desktop minimum target 24 dp (touch 48 dp) | WCAG 2.2 SC 2.5.8 gives 24 CSS px as the AA minimum; MD3 states 48 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Text field 40 dp high at default (MD3 56 dp) | row economy on desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Menu item 40 dp at default (Material Web 48 px) | same | [[ADR-0002 Desktop density levels and target sizes]] |
| Row padding 12, 8, 4 (MD3 16) and icon gap 8, 8, 4 (MD3 16) | narrow side panels | [[ADR-0002 Desktop density levels and target sizes]] |
| Project deviation, declared 2026-11-21: tess-ui toolkit default density is the legacy Material sizing (for example 56 px tree rows) until an App asks for a level; the spec level `default` (40 dp rows) applies when an App asks `density='default'`; the config app asks `compact` | migration without a visual change to existing apps | [[ADR-0002 Desktop density levels and target sizes]]; review: make `default` the toolkit default in a later major version once the apps are migrated ([[Adoption tess-ui]], TUI-002 to TUI-006) |
| Spacing token set with a 2 dp half step | the shell already ships a 2 dp step; focus ring offset is 2 dp | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Acceptance criteria

- [ ] AC-DEN-1 (token test): the spacing token set is exactly {0, 2, 4, 8, 12, 16, 24, 32, 48}. A lint script over every stylesheet and theme file of the project finds no padding, margin or gap literal outside this set. Pass: zero violations; the shell `step_*` tokens map to `space.1` to `space.8`.
- [ ] AC-DEN-2 (geometry check): at each density level, a laid-out Button, single-line Text Field, Switch row, Icon Button container and Menu item has the height in the tables above (40/32/28 for button, field, switch row, icon button container and menu item) exactly, at scale factor 1.0 and 2.0 (2.0 gives twice the px).
- [ ] AC-DEN-3 (geometry check): at each level, a single-line List row and Tree row has height 40, 32 and 24 exactly; a two-line row is at least the single-line height.
- [ ] AC-DEN-4 (geometry check): at each level a Tree Node at depth 0 has its chevron box left edge at 12, 8 and 4 dp from the container's inner left edge, and the chevron box is 24, 20 and 16 dp square. Pass: equals to the dp, no extra margin (owner feedback F4).
- [ ] AC-DEN-5 (geometry check): at each level, the left edge of the chevron box at depth d+1 is exactly 20, 16 and 12 dp to the right of the chevron box at depth d (owner feedback F3). Pass: equal to the dp for d from 0 to 5.
- [ ] AC-DEN-6 (geometry check): the horizontal padding of List rows, Tree rows and Menu items is 12, 8 and 4 dp; the icon-to-label gap is 8, 8 and 4 dp; Text Field horizontal padding is 12, 8 and 8 dp.
- [ ] AC-DEN-7 (geometry check): for every interactive element the hit area is at least 24 by 24 dp at every level, and at least 48 by 48 dp in a touch context. The hit area is read from the engine hit test (the set of points that activate the element), not from the painted box. The tree chevron's hit area is 24 dp wide and the full row height at all three levels.
- [ ] AC-DEN-8 (geometry check): no two hit areas overlap, except a child inside its parent's hit area (a chevron inside a row).
- [ ] AC-DEN-9 (geometry check): in a Text Field and any single-line control, the line box of the text is centred in the control height: the space above differs from the space below by at most 1 px at each level (also AC-LAY-2).
- [ ] AC-DEN-10 (token test): `width_class(w)` returns compact for 0 to 599, medium for 600 to 839, expanded for 840 to 1199, large for 1200 to 1599 and extra-large for 1600 and up; `height_class(h)` returns compact for 0 to 479, medium for 480 to 899 and expanded for 900 and up.
- [ ] AC-DEN-11 (review): a density level is declared once per project and per container in a project ADR or a container property; no element sets a height outside the three-value sets above. Pass: reviewer finds no height literal in a stylesheet that is not a density token.

## Sources

- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (24 by 24 CSS pixels; exceptions spacing, equivalent, inline, user-agent control, essential). Verified 2026-11-21.
- Window size classes (breakpoints 600, 840, 1200, 1600 width; 480, 900 height): https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes (verified). The MD3 page https://m3.material.io/foundations/layout/applying-layout/window-size-classes is a JavaScript app that returns no text; the Android page quotes the same Material breakpoints.
- Material Web tokens (button container height 40, icon button container 40 and icon 24, text field container 56, switch track 32 and state layer 40, menu item container 48, list item vertical space 12): https://github.com/material-components/material-web/tree/main/tokens/versions/latest/sass and https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192 (leading space 16, button leading space 24, switch touch target 48). Verified 2026-11-21.
- tess-ui window classes: `tess-ui:src/tess_ui/tokens.py`. Existing values: [[Existing Tokens]].
- Not verified: the MD3 specification page value of 56 dp for a one-line list item #needs-verification; MD3 4 dp grid statement (m3.material.io is not readable by tools) #needs-verification.
