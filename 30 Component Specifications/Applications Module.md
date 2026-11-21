---
title: Applications Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, launcher, search, keyboard]
related: ["[[Launcher]]", "[[Text Field]]", "[[List]]", "[[List Item]]", "[[Search]]", "[[Panel and Surface]]", "[[Selection]]", "[[Accessibility Announcements]]", "[[Empty and Error States]]", "[[Scrollbar and Scroll Container]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Applications Module

> [!info] Summary
> The Applications Module is the launcher content: a [[Text Field]] over a list of installed applications that narrows as the user types, held by the shell's Launcher panel. The Material Design 3 counterpart is [search](https://m3.material.io/components/search/overview) with a results list. Source of truth in code: see the last section.

## Purpose

Start an application by typing a few letters and pressing Enter, without leaving the keyboard.

## When to use and not

- Use when: a panel offers a type-to-filter application list (the [[Launcher]]).
- Do not use when: the user needs a full application grid, recent files or web search (not in v1); for a general filterable list use [[List]] with a [[Text Field]].

## Anatomy

1. Root: a vertical box, role `GROUP`, name `Applications`, padding 12.
2. Query field: single-line [[Text Field]] (`TextInput`), placeholder `Search applications`, keeps the keyboard focus.
3. Results list: a [[List]] named `Results` of up to `max_results` rows (8). Each row is a [[List Item]]: application icon (24 dp), name (`Text`, ellipsis), comment (`Text`, 12 px, `on_surface_muted`, ellipsis).
4. Message line: `No results`, `No applications found` or `Could not start <name>` in `on_surface_muted`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| With comments | Default | `show_comment` true: two-line rows |
| Names only | Compact launcher | `show_comment` false: one-line rows |

## States

| State | Visual change | Token values |
|---|---|---|
| Empty query | The first `max_results` applications are listed (the list is built from the cache) | not applicable |
| Typing | The list narrows; the first row is selected | [[Selection]] |
| Row hover | Background `surface_raised` (code); spec: state layer 8 percent ([[State Layers]]) | [[List Item]] |
| Row selected | `surface_raised` fill and a 2 px `primary` border (shape, not colour alone) | primary on surface: 5.76:1 dark, 5.29:1 light |
| Loading | Before the application list is built (`ready` false) the field shows and the list is empty; the message line is empty (spec: show `Loading applications` as a `status` message, absent in code) | [[Empty and Error States]] |
| No results | The message line reads `No results`; the list is removed | `on_surface_muted` |
| Error | `Could not start <name>` on the message line and announced | `on_surface_muted` |
| Hidden | Not applicable: the module shows whenever its Panel shows | not applicable |

## Tokens used

Roles: `on_surface` (name), `on_surface_muted` (comment, message); type `body_medium` for the name, `body_small` for the comment; row shape `small` 4 dp; no elevation. Components follow [[Text Field]], [[List]], [[List Item]].

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Query field height | 40 | 32 | 28 | [[Text Field]]; code: [[Text Field]] default |
| Row height, one line | 40 | 32 | 24 | [[List Item]]; code: 40 |
| Row height, two lines | 60 | 48 | 40 | [[List Item]]; code: 40 (a name and a comment do not fit 36 dp of text in 40 dp with the 6 dp padding at compact) |
| Row icon | 24 | 20 | 16 | [[Iconography]]; code: 24 at all |
| Row horizontal padding | 12 | 8 | 4 | `density.row_padding_x`; code: 10 |
| Icon-to-text gap | 8 | 8 | 4 | code: 10 |
| Content width | 456 | 456 | 456 | fixed by the Panel; code: literal 456 |
| Panel padding | 12 | 8 | 4 | [[Panel and Surface]]; code: 12 |

## Layout and overflow

Name and comment are single lines with an ellipsis (`Overflow: ELLIPSIS`, `Wrap: NONE`); a cut name or comment shows the full text in a tooltip on that text node only when it is cut (a label-level tooltip, allowed by ADR-0004). Vertical centring of icon and text block in the row. At most `max_results` rows: no scrollbar is needed in the default; a larger `max_results` scrolls the list ([[Scrollbar and Scroll Container]]).

## Behaviour

- Pointer: click a row to start it; the panel closes on a start.
- Keyboard: the query field keeps focus. Down, Up, Page Down, Page Up move the selection from the field; Enter starts the selected application; Escape clears the field and, with the field empty, hides the Panel. When the Panel shows, the field takes focus and its text is selected. Open the Panel with the shortcut `Meta+Space` (user binding).
- Touch: tap a row.

## Tooltip and overlay behaviour

No tooltip on a row or on the list (ADR-0004: a row is not a trigger). The only tooltips are on a cut name or comment text, showing the full text. The module opens no overlay itself; it lives in a Panel.

## Motion

The list narrows in one frame. No animation. Reduced motion: none to remove.

## Accessibility

- Roles: query field `TEXTBOX` named by its placeholder (`Search applications`); list `LIST` named `Results`; row `LISTITEM` with state `selected`, named by the application name and the comment (`Firefox, Web Browser`).
- Keys: as Behaviour; the list is one Tab stop in the pattern of [[List]], but selection moves from the field, so the field remains the only focus.
- Announcements: through `ctx.announce`, politely: the selected row (name and comment), `No results`, `Could not start <name>`; selection moves are said after the key repeat settles ([[Accessibility Announcements]]).
- An active descendant pattern would be the right route for the field-with-list; the engine has no `aria-activedescendant` and the module announces instead (candidate request).

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `max_results` | 8 |
| `show_comment` | true |
| `icon_size` | 24 |
| `placeholder` | `Search applications` |

## Acceptance criteria

- [ ] AC-MOD-APP-1 (AT tree assertion): the query field has role `TEXTBOX` and a non-empty name; the list has role `LIST` named `Results`; each row has role `LISTITEM` and a name `<name>, <comment>`; exactly one row has `selected`.
- [ ] AC-MOD-APP-2 (scripted input): type `fire`: the list narrows to rows whose name or comment matches, first row selected; Down moves the selection one row; Enter starts the selected application once.
- [ ] AC-MOD-APP-3 (scripted input): Escape with text clears the field; Escape with an empty field hides the Panel; showing the Panel puts focus in the field with the text selected.
- [ ] AC-MOD-APP-4 (scripted input): a query with no match shows `No results` and removes the list; a failed start shows `Could not start <name>` and queues one polite announcement.
- [ ] AC-MOD-APP-5 (geometry check): one-line rows are 40, 32, 24 dp and two-line rows 60, 48, 40 dp at default, compact and dense; icon 24, 20, 16 dp; query field 40, 32, 28 dp.
- [ ] AC-MOD-APP-6 (geometry check): row horizontal padding is 12, 8, 4 dp and icon-to-text gap 8, 8, 4 dp.
- [ ] AC-MOD-APP-7 (pixel check): a name wider than the row ends with an ellipsis and does not paint past the row; vertical centring within 1 px.
- [ ] AC-MOD-APP-8 (scripted pointer): hover the cut name for 500 ms: one tooltip with the full name; hover a row where nothing is cut: 0 tooltips.
- [ ] AC-MOD-APP-9 (pixel check): the selected row is distinguishable from an unselected row in a greyscale render (border plus fill).
- [ ] AC-MOD-APP-10 (contrast script): name, comment, message text against the panel surface at least 4.5:1 in Light, Dark and High_Contrast.

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Applications/Applications_Module.tdl`, `Applications_Style.tdl`, `Applications_Module.py` | partly meets: field, list, keys, messages, selected row with border and fill, announcements (meets AC-MOD-APP-1 by reading, -2, -3, -4, -9); two-line rows are 40 dp, padding 10, widths 456 literal (fails AC-MOD-APP-5, -6); no tooltip for cut text (fails AC-MOD-APP-8); no density setting |
| shell-vault | `shell-vault:40 Specifications/Modules/Applications Module.md`, `shell-vault:40 Specifications/Surfaces/Panel.md` | exists |
| tess-ui | none | not applicable: no launcher |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Search is a type-to-filter list inside a panel, not an MD3 search bar and view | launcher pattern; the MD3 search bar is 56 dp high with a full shape, the field here follows [[Text Field]] densities | [[ADR-0002 Desktop density levels and target sizes]] |
| Row density 40, 32, 24 and two-line 60, 48, 40 | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
- WAI-ARIA Authoring Practices, listbox pattern: https://www.w3.org/WAI/ARIA/apg/patterns/listbox/ (selection moves with arrows, Enter activates).
- Material Web search bar tokens (container height 56 px, shape full): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-search-bar.scss
