---
title: Toolbar
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, navigation, toolbar, owner-feedback]
related: ["[[Top App Bar]]", "[[Tabs]]", "[[Status Bar]]", "[[Pagination]]", "[[Icon Button]]", "[[Button]]", "[[Floating Action Button]]", "[[Menu]]", "[[Switch]]", "[[Tooltip]]", "[[Divider]]", "[[Scrollbar and Scroll Container]]", "[[Keyboard Navigation]]", "[[Owner Feedback 2026-11-20]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Icon Button]]", "[[Menu]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]"]
---

# Toolbar

> [!info] Summary
> A row (or column) of actions for the content next to it, docked to an edge or floating over content, with an overflow menu for what does not fit. Material Design 3 counterpart: [Toolbars](https://m3.material.io/components/toolbars/overview). Source of truth in code: see Status in code. The config application builds its own toolbar of buttons by hand; that is the evidence for the labelled-button content option below.

## Purpose

Groups the commands that act on the content around it (format text, save, undo, check) in one place the user finds by keyboard with one Tab stop and by pointer without searching menus.

## When to use and not

- Use when: three or more commands apply to one region and are used often enough to deserve a fixed place.
- Do not use when: one primary action leads the screen (use [[Floating Action Button]]); the bar holds a title and navigation (use [[Top App Bar]]); the choices switch views (use [[Tabs]]); the bar reports state (use [[Status Bar]]); the commands are rare (use a [[Menu]]).
- A toolbar holds buttons, icon buttons, toggles and at most one [[Switch]]. It holds no text field or slider (they need the arrow keys that move focus in a toolbar, [WAI-ARIA toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/)).

## Anatomy

1. Container (role: group today, `toolbar` in the specification; name required).
2. Items: [[Icon Button]]s, each with a name (and tooltip), or labelled [[Button]]s.
3. Group dividers (optional, [[Divider]], vertical 1 dp).
4. Trailing slot: author content after the items (a title, a [[Switch]], the action button).
5. Action button (optional): a small [[Floating Action Button]] at the end.
6. More button: an [[Icon Button]] (`dots_horizontal`, `dots_vertical` in a vertical toolbar), shown when items overflow, with the overflow [[Menu]].

## Variants

| Variant | Use | Differences |
|---|---|---|
| Docked | fixed to a window or panel edge, full width | square, `surface_container`, no shadow |
| Floating | a pill over content | shape `full`, elevation level 3 (tess-ui `Elevation: 3`), as long as its items, `Max_Length` for overflow |
| Vertical (floating only) | an edge rail of tools | a column, thickness equal to the docked height |
| Vibrant | emphasis | container `primary_container`, icons `on_primary_container` |
| Labelled (Tesserae) | commands whose names must be visible (a config tool: Save, Undo, Check) | items are [[Button]]s with text; same keyboard, overflow and density rules |

Docked and floating, vibrant and standard are the MD3 forms; the MD3 toolbar page is script-rendered and its token values could not be fetched #needs-verification (they are the Expressive toolbar, [[ADR-0006 MD3 baseline with named Expressive adoptions]]). The labelled variant has no MD3 counterpart; MD3 toolbars hold icon buttons.

## States

The toolbar itself has no state layer. Each item has the states of [[Icon Button]] or [[Button]] ([[State Layers]]: hover 8, focus 10, pressed 10 percent, disabled content 38 percent).

| State | Visual change | Token values |
|---|---|---|
| Rest | container per variant | `surface_container`, `primary_container` (vibrant) |
| Item disabled | the item at 38 percent, no focus, pointer or key; skipped by arrow keys | [[State Layers]] |
| All disabled (`Disabled`) | every item and the action button disabled | review |
| Hidden (`Hidden`) | faded out (opacity 0, 200 ms), items out of the Tab order and the accessibility tree | tess-ui |
| More open | the More button `expanded` true, the menu open | [[Menu]] |

## Tokens used

[[Colour Roles]]: `surface_container`, `primary_container`, `on_surface_variant` and `on_primary_container` for icons. [[Shape]]: docked `corner_none`, floating `corner_full`. [[Elevation]]: floating level 3. [[Spacing and Density]]: heights, padding, gaps. [[Motion]]: fade.

## Sizing and density

Item sizes come from [[Icon Button]] (container 40, 32, 28 dp; icon 24, 20, 20 dp) and [[Button]] (40, 32, 28 dp). The toolbar thickness is the item size plus a padding on each side (design choice; the default equals MD3 and tess-ui at 64 dp):

| Level | Thickness (docked, floating, vertical) | Item | Padding across | Padding along (docked) | Gap between items | Gap to action button |
|---|---|---|---|---|---|---|
| default | 64 dp | 40 dp | 12 dp | 16 dp | 4 dp | 8 dp |
| compact | 48 dp | 32 dp | 8 dp | 8 dp | 4 dp | 8 dp |
| dense | 36 dp | 28 dp | 4 dp | 8 dp | 2 dp | 4 dp |

- Floating padding along the length: 8 dp default, 4 dp compact and dense; the pill is as long as its items plus padding.
- Every item hit area is at least 24 dp by 24 dp; adjacent hit areas do not overlap; in a touch context 48 dp ([[Spacing and Density]]).
- Items centre vertically in a docked toolbar by construction ([[10 Layout Overflow and Scrolling]]); a trailing title text is centred on the same line.

## Layout and overflow

Overflow rule (chapter 10): a toolbar never scrolls, never clips an item and never wraps. Items that do not fit move into the overflow [[Menu]] under the More button, from the end of the item list backwards, in their order, with their icon, name and disabled state; a Menu row replaces the icon button. The More button's width is reserved before items are measured. Items are measured by their real width, not by a count times a constant (tess-ui assumes 44 px per item, which fails for compact, dense and labelled buttons).

- Priority: items keep the author's order; an author may pin an item before the overflow starts (not built; candidate request below).
- A docked toolbar measures its available width; a floating one uses `Max_Length`; a vertical one its available height.
- The More button is absent when everything fits and present, enabled, when any item moved. At least one item stays visible when the toolbar is wider than the More button plus one item; below that, only the More button shows.
- Trailing content (a title) shrinks first: single line, `Min_Width 0`, ellipsis ([[10 Layout Overflow and Scrolling]]); full text in a tooltip on that text. Then items overflow; the action button is last to move.
- Focus on an item that moves into the menu moves to the More button.
- A toolbar with a Switch moves the Switch into the menu as a toggle row only if the menu supports it; otherwise the Switch is pinned and never overflows (a project decides; the spec rule is that no control is lost).

Config app evidence (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, container `toolbar`): a horizontal Container with padding 8 and gap 8 holds six text Buttons (Save filled, Undo and Redo tonal, Format file, Check, Reload shell outlined), a Switch "Apply as I edit" and a title Text with `Min_Width 0` and an ellipsis. It has no height token (40 dp buttons plus 16 dp padding make 56 dp), no `Focus_Group` (every button is a Tab stop, seven in all), no overflow rule (the title yields; nothing moves the buttons into a menu), a role `group` named "Actions" with a description. It is not the shipped `Toolbar` because that view takes icon items only and measures 44 px per item.

## Behaviour

- Pointer: as the items. The More button opens the Menu on press; a press elsewhere closes it.
- Keyboard ([WAI-ARIA toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/), [[Keyboard Navigation]]): the toolbar is one Tab stop (roving focus); Tab enters on the item that last had focus (the first on first entry); Left and Right (Up and Down in a vertical toolbar) move to the previous and next enabled item and wrap; Home and End go to the first and last; Enter or Space activates; Tab and Shift+Tab leave. Disabled items are skipped. The project documents a shortcut that moves focus to the toolbar from the content (APG recommends it where access is frequent). Escape in the open More menu closes it and returns focus to the More button.
- Touch: tap on 48 dp hit areas in a touch context; no swipe.
- Hidden toolbar: `Hidden` removes the items from the Tab order; a hidden toolbar takes no focus.

## Tooltip and overlay behaviour

Each icon item carries a tooltip with its name on the item itself ([[ADR-0004 Tooltip rule]], [[Tooltip]]): 500 ms hover, immediate on keyboard focus, dismissed on press. A labelled button needs one only when its label is truncated or it has a shortcut to show ("Save, Ctrl+S" in the description). The toolbar container has no tooltip. The only overlay is the overflow [[Menu]]; it opens below the More button (above for a bottom toolbar, to the side for a vertical one), takes focus on its first item and returns focus to the More button on close.

## Motion

Hide and show fade 200 ms (`short4`) in tess-ui; MD3 slides a floating toolbar out of the way with the scroll (not built; tess-ui fades only). State layers: `short3`. Reduced motion: the fade is immediate. Items moving to overflow on resize change at once without animation.

## Accessibility

- Role: `toolbar` ([WAI-ARIA toolbar](https://www.w3.org/TR/wai-aria-1.2/#toolbar)) with an accessible name ("Actions", "Text formatting") and an orientation. The engine has no `toolbar` role (`tre:docs/reference/node.md`), so the container is a `group` with the same name today (candidate request below).
- Items: role `button` (toggle items `pressed`), name from the visible label or the icon's name; descriptions carry shortcuts.
- More: name "More actions", `expanded` follows the menu.
- Keys: as in Behaviour; labelled and unlabelled items follow the same keys.
- Contrast: icons and labels at least 3 to 1 for icons, 4.5 to 1 for text against the container, in both schemes and for vibrant (WCAG 2.2 SC 1.4.3, 1.4.11).
- The focus ring of an item is not clipped by the toolbar ([[Focus Ring]]).
- A toolbar that changes content (items moved by resize) announces nothing; a disabled state change is read from the item.

## Dark and light

All roles follow the scheme; vibrant `primary_container` and `on_primary_container` invert with it ([[Theme Following the System]]).

## Defaults

Docked, standard (not vibrant), horizontal, `surface_container`, density per container (default 64 dp), no overflow menu until items do not fit, `Label` "Toolbar" in tess-ui (a project sets a real name).

## Acceptance criteria

- [ ] AC-TLB-1 (token test): thickness 64, 48, 36 dp at default, compact, dense; items 40, 32, 28 dp; paddings and gaps equal the Sizing table. Pass: values equal.
- [ ] AC-TLB-2 (geometry check): each item is vertically centred in a docked toolbar at each level (space above equals space below within 0.5 dp) and a trailing text line is centred on the same line. Pass: offsets within 0.5 dp.
- [ ] AC-TLB-3 (geometry check): item hit areas at least 24 dp by 24 dp (48 dp in a touch context) and do not overlap. Pass: bounds at or above limits, zero intersection.
- [ ] AC-TLB-4 (scripted input): the toolbar is exactly one Tab stop; Tab enters on the item that last had focus; Right, Left, Home, End (Down, Up, Home, End in a vertical toolbar) move to the next, previous (both wrapping), first and last enabled item; disabled items are skipped. Pass: focus owner equals after each key.
- [ ] AC-TLB-5 (scripted input): with the available width reduced one item at a time (resize), the item list shows a prefix of the author's order, every other item is a row of the overflow menu in the same order with the same icon, name and disabled state, the More button is present exactly when a row exists. Pass: visible plus menu items equal the full list at every width.
- [ ] AC-TLB-6 (geometry check): at every width no item or text pixel lies outside the toolbar, no two items overlap, and the toolbar paints the same count of visible items as it has non-overflowed items. Pass: zero pixels outside, zero overlap.
- [ ] AC-TLB-7 (scripted input): Enter on the More button opens the menu, focus lands on the first row, Escape closes it and focus returns to the More button; focus on an item that moves into the menu moves to the More button. Pass: focus owner equals at each step.
- [ ] AC-TLB-8 (AT tree assertion): the container has role `toolbar` (today `group`) and a non-empty name; each item has role `button` and a non-empty name; the More button has `expanded` equal to the menu state; a toggle has `pressed`. Pass: all equal.
- [ ] AC-TLB-9 (scripted input): hovering an icon item for 600 ms shows a tooltip equal to its name; keyboard focus shows it at once; press dismisses it; the container shows no tooltip. Pass: visibility and text equal.
- [ ] AC-TLB-10 (token test): docked container `surface_container`, vibrant `primary_container` with icons `on_primary_container`, floating shape `full` and elevation level 3; item state layers 8, 10, 10 percent. Pass: every colour is a role reference, values equal.
- [ ] AC-TLB-11 (contrast script): in light, dark and high contrast, item icons against the container at least 3 to 1, labels at least 4.5 to 1, for standard and vibrant. Pass: ratios at or above limits.
- [ ] AC-TLB-12 (scripted input): with `Hidden` true the items take no Tab stop and are absent from the accessibility tree; fade completes in 200 ms, within one frame with reduced motion simulated. Pass: tree walk and frame counts equal.
- [ ] AC-TLB-13 (geometry check): a labelled toolbar's text label that does not fit ends with an ellipsis and the full label is the accessible name. Pass: ellipsis present, zero pixels outside.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Toolbar_View.tdl`, `tess-ui:src/tess_ui/views/Toolbar_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py` | partly meets. Docked and floating, vertical, vibrant, icon items with name and tooltip, `Fit` overflow into a Menu, action button, `Hidden`, `Focus_Group: both` (one Tab stop, arrows wrap, Home and End); thickness 64 dp fixed (AC-TLB-1 partly: default only, no density); `Fit` assumes 44 px per item and 48 px for More, so it fails for compact, dense and labelled buttons (AC-TLB-5, AC-TLB-6); role `group` not `toolbar` (AC-TLB-8); no pinned items; slide-away not built; docked padding 16 and gap 8 (the group gap is 4); icons only, no labelled buttons (AC-TLB-13); focus return to More not read (AC-TLB-7 unmeasured) |
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (container `toolbar`) | partly meets: hand-built Container of seven controls; no `Focus_Group` so seven Tab stops (AC-TLB-4 fails); no overflow rule (AC-TLB-5, AC-TLB-6 fail at narrow widths); height 56 dp (AC-TLB-1 fails at compact); role `group` named "Actions" (AC-TLB-8 partly); title ellipsis meets AC-TLB-13; buttons have name and description |
| tess-shell | none (the shell has module bars, not toolbars; see [[Bar]]) | absent |
| tre | `tre:docs/reference/node.md` | not applicable: no toolbar primitive, no `toolbar` role |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Thickness 64, 48, 36 dp; items 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Labelled variant with text buttons and a Switch in the trailing slot | desktop commands need visible names; the config app already needs it | none (Tesserae-only variant) |
| Overflow always by menu, never scroll or wrap | no hidden or clipped command (chapter 10 rule 3) | none (chapter 10) |
| Roving focus with Home, End and wrap; one Tab stop | WAI-ARIA toolbar, desktop keyboard-first | none |
| Fade, not slide, to hide | engine has no scroll-linked slide | none (code limit) |

## Sources

- [Material Web top app bar tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-top-app-bar-small.scss) are not toolbar tokens; the MD3 toolbar has no Material Web token file ([listing of v0_192](https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192)) and the Android docs have no toolbar page at the tested path, so docked 64 dp, floating elevation and the vibrant colours rest on `tess-ui:docs/components/toolbars.md` #needs-verification.
- [WAI-ARIA Authoring Practices: toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/): one Tab stop, arrows, Home and End, optional wrap, name by label, avoid controls needing the arrow keys, shortcut to reach the toolbar.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.3, 1.4.11, 2.1.1, 2.5.8.
- Code: `tess-ui:docs/components/toolbars.md`, `tess-ui:src/tess_ui/views/Toolbar_View.tdl`, `tess-ui:docs/guide/view-language.md` (`Focus_Group`), `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, `tre:docs/reference/node.md`.
- Candidate requests: engine roles `toolbar` and `status` (tre); `Toolbar` accepting labelled buttons, pinned items and measured overflow (tess-ui); `Fit` using measured widths (tess-ui).
