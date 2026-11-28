---
title: Menu Bar
type: component
status: draft
owner: phil
created: 2026-11-28
updated: 2026-11-28
tags: [component, menu, keyboard, desktop]
related: ["[[Menu]]", "[[Menu Item]]", "[[Popup]]", "[[Toolbar]]", "[[Top App Bar]]", "[[Title Bar]]", "[[Application Window]]", "[[Tooltip]]", "[[Keyboard Navigation]]", "[[Focus Ring]]", "[[State Layers]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Typography]]", "[[Spacing and Density]]", "[[11 Interaction]]", "[[12 Overlays]]", "[[Config App Layout]]", "[[UXREQ-004 Accessibility roles]]", "[[UXREQ-011 Menubar role]]", "[[ADR-0029 Desktop density and type scale]]"]
depends_on: ["[[Menu]]", "[[ADR-0029 Desktop density and type scale]]"]
---

# Menu Bar

> [!info] Summary
> The desktop application menu bar: a horizontal row of menu titles (File, Edit, View, ...) at the top of a window, each opening a [[Menu]] of commands with shortcuts shown beside them. Material Design 3 has no counterpart (it targets touch and has the [[Top App Bar]]); the baseline is the WAI-ARIA Authoring Practices menubar pattern and the desktop convention of Windows, KDE and GTK. Status in code: absent in every project.

## Purpose

Give a desktop application one complete, always-findable list of its commands, grouped under a few titles, each with its keyboard shortcut and mnemonic, so a user can discover a command, see its shortcut and run it by pointer or keyboard without a toolbar button for it. The [[Toolbar]] holds the few frequent commands as icons; the menu bar holds all of them.

## When to use and not

- Use when: a desktop application has more than about six commands, or its commands should show shortcuts; the config app ([[Config App Layout]]).
- Do not use when: a touch or compact-width window (use the [[Top App Bar]] with an overflow [[Menu]]); one menu of a few commands (a [[Menu]] from a button); a shell panel (the shell [[Bar]] is a panel of modules, not a menu bar); commands that belong to one object (a context menu, [[Menu]]).

## Anatomy

1. Bar: the container, full window width, directly under the [[Title Bar]] and above the [[Toolbar]]. Role `menubar`.
2. Bar item: one title with an optional mnemonic letter (underlined while shown). Role `menuitem` with a popup.
3. Menu: a [[Menu]] opened under its item.
4. Overflow item: a trailing item that holds the titles that do not fit.
5. Entries inside a menu are [[Menu Item]]s: plain, check, radio, submenu, with the shortcut right-aligned and a divider between groups.

## Variants

| Variant | Use | Differences |
|---|---|---|
| In-window bar | Default on every platform | Drawn by the toolkit inside the window |
| Hidden bar | A project may hide the bar and show it on Alt | Shown while Alt or F10 is active; a hidden bar is shown by a View menu entry too |

A global (system) menu is out of scope: the bar is always inside the window ([[Application Window]]).

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Title `on_surface` on the bar container | container `surface` |
| Hover | State layer `on_surface` on the item | 8 percent ([[ADR-0009 State layer percentages]]) |
| Focus (keyboard) | Focus ring on the item and state layer | 10 percent; ring per [[Focus Ring]] |
| Open (menu shown) | State layer on the item for as long as its menu is open | 10 percent |
| Pressed | State layer | 10 percent |
| Disabled | Title at 38 percent of `on_surface`; no state layer; skipped by Left and Right and by mnemonics | 38 percent |

Mnemonics: the mnemonic letter of a title is underlined while the bar is active by keyboard (Alt pressed, F10 pressed, or the bar has focus) and the project setting `Mnemonics: on_alt` holds; with `always` it is underlined at rest ([[Typography]]: an underline is a decoration, not a role).

## Tokens used

Container `surface`; title `on_surface`; state layers `on_surface` ([[State Layers]], [[ADR-0009 State layer percentages]]); item shape `shape.extra_small`; bar has no elevation, a 1 dp divider `outline_variant` under it only when no [[Toolbar]] follows ([[Colour Roles]], [[Shape]], [[Elevation]]). Type: `label_large` at default and compact, `title_dense` at dense ([[Typography]], [[ADR-0029 Desktop density and type scale]]). The menus use the tokens of [[Menu]].

## Sizing and density

| Measure | default | compact | dense |
|---|---|---|---|
| Bar height (the item height) | 40 | 32 | 28 |
| Item horizontal padding | 12 | 8 | 8 |
| Gap between items | 0 | 0 | 0 |
| Title type | `label_large` 14/20 | `label_large` 14/20 | `title_dense` 13/18 |

- The hit area of an item is the whole item, at least 24 by 24 dp at every density; the bar height is the item height so the hit area reaches the window edge.
- Menu rows follow [[Menu]] and [[Menu Item]] (40, 32, 28 dp) at the density of the bar: a menu takes the density of its opener ([[Spacing and Density]], Density is a property of every element).
- The config app uses `compact`: a 32 dp bar ([[Config App Layout]]).

## Dimensions and defaults

Compact and dense values follow the density tokens; the bar is a Tesserae element with no MD3 value, so every size is a design choice of this note #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| bar | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]]; design choice, [[ADR-0029 Desktop density and type scale]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| bar | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| bar | padding | `space.0` | 0 8 0 8 | 0 4 0 4 | 0 4 0 4 | design choice, [[ADR-0029 Desktop density and type scale]] (items start 4 to 8 dp from the window edge) | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| bar | margin | - | N/A: the window lays the bar out full width under the title bar | N/A: as in Default | N/A: as in Default | [[Application Window]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| bar | gap | `space.0` | 0 | 0 | 0 | design choice, [[ADR-0029 Desktop density and type scale]] (items abut so the hit areas leave no gaps) | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| bar | border width | - | 1 (bottom, only without a toolbar) | 1 (bottom, only without a toolbar) | 1 (bottom, only without a toolbar) | design choice, [[ADR-0029 Desktop density and type scale]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| bar | border color | `outline_variant` | `outline_variant` | `outline_variant` | `outline_variant` | [[Colour Roles]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| bar | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| bar | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| item | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| item | padding | `density.field_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 8 0 8 | [[Spacing and Density]]; design choice, [[ADR-0029 Desktop density and type scale]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| item | margin | - | N/A: items abut; the bar padding sets the outer space | N/A: as in Default | N/A: as in Default | [[Spacing and Density]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| item | gap | - | N/A: an item holds one text; the icon of an overflow item has no label | N/A: as in Default | N/A: as in Default | [[Spacing and Density]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| item | border width | - | 0 | 0 | 0 | [[Spacing and Density]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| item | border color | - | N/A: an item has no border; the focus ring is the outline | N/A: as in Default | N/A: as in Default | [[Focus Ring]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| item | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| item | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 13/18/500/0.1 | [[Typography]], [[ADR-0029 Desktop density and type scale]] (dense is `title_dense`) | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| item | icon size | `density.icon_button_icon` | 24 | 20 | 18 | [[Iconography]], [[Spacing and Density]] (the overflow item only) | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| item | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

## Layout and overflow

- Items lie left to right in the order of the menu list, start-aligned (right-aligned in right-to-left). The bar never wraps and never scrolls.
- When the window is too narrow the titles that do not fit move, from the end, into a trailing overflow item (a "More" item with the icon `more_horiz`); its menu lists those titles as submenu items in order. A title is never truncated; the bar shows whole titles or none.
- A title is one line; a menu label with a mnemonic shows the letter underlined and keeps the full text as its accessible name.
- Menu placement: a menu opens under its item, start-aligned with the item's start edge, 0 dp gap, its top edge on the bar's bottom edge; it flips above when there is no room below and more above, then slides to stay at least 8 dp inside the window (the popup edge margin of the shell, see [[Popup]]). A submenu opens at its item's end edge and flips to the start side when it does not fit ([[Menu]]).

## Behaviour

- Pointer: press on a title opens its menu (the press toggles: a press on the open title closes it). Hover on a title only highlights it, until one menu is open; while a menu of the bar is open, hover on another title opens that one at once and closes the first (no delay). Moving to a menu item and onward follows [[Menu]]. A press outside the bar and its menus closes the menu and is consumed.
- Keyboard, bar active and no menu open:
  - Alt pressed and released alone, or F10: focus moves to the first title and the bar is active (mnemonics shown); Alt or F10 again, or Escape, returns focus to the element that had it.
  - Left Arrow, Right Arrow: previous or next enabled title, wrapping (mirrored in right-to-left).
  - Down Arrow, Enter, Space: open the title's menu and highlight its first enabled item. Up Arrow: open and highlight the last enabled item.
  - Home, End: first and last enabled title.
  - A printable character: move to the next enabled title whose label starts with it (case-insensitive, wrapping).
  - Tab, Shift+Tab: leave the bar to the next or previous focus stop; the bar is one Tab stop and a roving group ([[Keyboard Navigation]]).
  - Alt+letter (the mnemonic) from anywhere in the window opens the title with that mnemonic and highlights its first enabled item; when the bar has focus, the letter alone does it.
- Keyboard, a menu open: the keys of [[Menu]] apply inside it. In addition: Left Arrow in a first-level menu (no submenu open) opens the previous title's menu, Right Arrow on an item without a submenu opens the next title's menu (both wrap; the highlight lands on the first enabled item); Escape closes the menu and returns focus to its title, and a second Escape deactivates the bar; Tab closes the menu and leaves the bar; Alt or F10 closes the menu and returns focus to the previous element.
- A command runs when its item is activated (Enter, Space or click); the menu closes (not for a check or radio item when the project sets "keep open") and focus returns to the element that had focus before the bar was activated, unless the command moves focus itself.
- Shortcuts: the shortcut of a command is shown right-aligned in its item (the text of the chord, `Ctrl+S`), is bound once at the window level and works with the bar and menus closed; the menu shows it and does not bind it. A disabled command's shortcut does nothing.
- Mnemonics are unique among the titles of one bar and among the entries of one menu (a conflict is a design-time error); a title without a mnemonic works by arrows and type-ahead only.
- Touch: not specified; use [[Top App Bar]].

## Tooltip and overlay behaviour

Titles show no tooltip. The menus are non-modal [[Popup]]s: one popup chain at a time, no scrim, focus returns to the title on close ([[12 Overlays]], [[Menu]]). Menu items follow the tooltip rule of [[Menu]].

## Motion

The bar has no animation. A menu opens and closes as [[Menu]] says; switching from one title to another by hover or Left and Right is instant, with no fade between the two menus. With reduced motion on, nothing animates.

## Accessibility

- Role `menubar` for the bar with the name "Menu bar" (a project may name it by the application); each title `menuitem` with the popup flag and `expanded` true while its menu is open; menus `menu` and entries `menuitem`, `menuitemcheckbox` with `checked`, `menuitemradio` ([[Menu]]); disabled entries expose `disabled`; the shortcut is exposed as the key shortcut of the entry (`aria-keyshortcuts` form, for example `Control+S`) and the accessible name excludes it.
- Keys: WAI-ARIA Authoring Practices menubar pattern (Sources): one Tab stop, Left and Right between titles, Down, Up, Enter and Space open, Escape closes, Home, End and printable characters move.
- Active descendant: the bar is a roving group; the focused title carries the focus. Inside a menu the highlighted item is the active item ([[Menu]]); a project either gives the item node focus or keeps focus on the menu and sets `active_descendant` of the menu node to the item (tre has the property, [[UXREQ-011 Menubar role]]); both give the same AT result as far as the tree goes, and neither is checked with a screen reader ([[Behavior Standard Inventory]]).
- Contrast: `on_surface` on `surface` at least 4.5:1; the state layer must not reduce the title below 4.5:1; the focus ring at least 3:1 against the bar ([[Focus Ring]]).
- Target size: every title at least 24 by 24 dp.
- No keyboard trap: Escape, Tab and Alt leave the bar (WCAG 2.2 SC 2.1.2).
- Mnemonic underline is not the only cue of the access key: the accessible name keeps the label and the key is exposed as the entry's access key.

## Dark and light

All roles come from the scheme ([[Theme Following the System]]); the bar and the menus use the same roles in both.

## Defaults

| Setting | Default |
|---|---|
| Density | the application density; compact in the config app |
| Mnemonics | `on_alt` |
| Menu open on hover | only after one menu of the bar is open |
| Overflow | trailing "More" item |
| Menu placement | below the title, start-aligned, flip, slide, 8 dp window margin |
| Alt activation | on |

## Acceptance criteria

- [ ] AC-MBR-1 (geometry check, density): the bar is 40, 32 and 28 dp high at default, compact and dense (±0.5); each title's hit area is the whole item, at least 24 by 24 dp; the title line box is centred in the bar within 1 dp (AC-TYP-4).
- [ ] AC-MBR-2 (AT tree assertion): the bar has role `menubar` and a name; each title has role `menuitem`, the popup flag, and `expanded` equal to whether its menu is open; each menu has role `menu`; entries have the roles of [[Menu]] AC-MEN-17; a command's shortcut is its exposed key shortcut. Pass: property equality for a bar of three titles.
- [ ] AC-MBR-3 (scripted input, one Tab stop): Tab from the control before the bar focuses the first title (or the last one used), a second Tab leaves the bar to the next stop; Shift+Tab goes back; the bar is one stop whatever the number of titles. Pass: focus order equals.
- [ ] AC-MBR-4 (scripted input, arrows): with titles File, Edit (disabled), View and focus on File, Right Arrow focuses View, Right wraps to File, Left wraps to View; Home focuses File and End View. Pass: focused title after each key.
- [ ] AC-MBR-5 (scripted input, open): Down Arrow, Enter and Space on a title open its menu with the first enabled item highlighted; Up Arrow opens it with the last enabled item highlighted; focus is inside the menu within one frame. Pass: highlighted id and `expanded` equal.
- [ ] AC-MBR-6 (scripted input, between menus): with the File menu open on a first-level item, Right Arrow on an item without a submenu opens the View menu (Edit is disabled and skipped) with its first enabled item highlighted and closes File; Left Arrow on a first-level item opens the previous title's menu; both wrap. In a submenu, Left closes only the submenu. Pass: open menu id after each key.
- [ ] AC-MBR-7 (scripted input, Escape): Escape in a first-level menu closes it and focus is its title; a second Escape deactivates the bar and focus is the element that had it before activation; Escape inside a submenu closes only the submenu. Pass: focus owner after each key.
- [ ] AC-MBR-8 (scripted input, Alt and F10): with focus in a text field, Alt pressed and released alone focuses the first title and shows the mnemonics; a second Alt returns focus to the text field with its caret unchanged; F10 does the same as Alt; Alt held with another key (Alt+Tab, Alt+Left) does not activate the bar. Pass: focus owner and mnemonic underlines equal.
- [ ] AC-MBR-9 (scripted input, mnemonics): with titles `&File`, `&Edit`, `&View`: Alt+F opens File with the first enabled item highlighted from anywhere in the window including a multi-line text field; Alt+E and Alt+V likewise; with a menu open, the mnemonic of an entry runs that entry; a mnemonic letter that duplicates another in the same bar or menu fails the build or the load. Pass: open menu and run command equal.
- [ ] AC-MBR-10 (scripted input, type-ahead): focus on a title, typing "v" moves to View; typing "e" moves to Edit; typing "z" changes nothing; inside a menu type-ahead is [[Menu]] AC-MEN-9. Pass: focused title after each key.
- [ ] AC-MBR-11 (scripted input, pointer): a press on File opens its menu, a second press closes it; with File open, hover on View closes File and opens View in the same frame, with no delay; hover on a title with no menu open only highlights it; a press outside closes the menu and the outside press is consumed. Pass: open menu and layer count after each step.
- [ ] AC-MBR-12 (scripted input, activation): Enter on an item runs the command once, closes the menu and returns focus to the element that had it before the bar was activated; Space on a check item flips `checked` once. Pass: action count and focus owner equal.
- [ ] AC-MBR-13 (scripted input, shortcuts): with a menu closed, Ctrl+S runs Save once; with Save disabled it runs nothing and the item shows disabled; the menu text shows the shortcut right-aligned and the accessible name of the item excludes it. Pass: counts and strings equal.
- [ ] AC-MBR-14 (geometry check, placement): a menu opens with its start edge on its title's start edge and its top on the bar's bottom edge; in a window 200 dp high with the bar at the top and a 400 dp menu the menu clamps with a scrollbar ([[Menu]] AC-MEN-16); the menu rectangle is at least 8 dp inside the window on every side. Pass: rectangles equal.
- [ ] AC-MBR-15 (geometry check, overflow): at a window width where the last title does not fit, it moves into the trailing "More" item, in order, and no title is truncated or clipped; widening the window brings it back. Pass: item rectangles inside the bar at every width from 200 to 1200 dp.
- [ ] AC-MBR-16 (pixel check, states): the title pixel under hover is `on_surface` at 8 percent over the bar; focus and open 10 percent (±1 per channel); the focus ring is visible on a keyboard-focused title and absent after pointer activation.
- [ ] AC-MBR-17 (contrast script): `on_surface` on `surface`, the same with the 10 percent layer, and the focus ring against the bar, in light and dark. Pass: at least 4.5, 4.5 and 3 to 1.
- [ ] AC-MBR-18 (scripted input, density and density cascade): a bar inside a `dense` pane is 28 dp high and its menus open at the dense item height (28 dp); a bar with `Density: default` is 40 dp high ([[Spacing and Density]] AC-DEN-12).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | none (text search of `src`, `apps` and `docs` on `origin/main` for menubar or menu bar finds no component); the config app has a `toolbar` container of text buttons in `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`; the [[Menu]] overlay exists (`tess-ui:src/tess_ui/overlays.py`) and can open under a title | absent. Everything above is new: a bar view, Alt and F10 activation, mnemonics, roving, the hover switch between menus. Read at `origin/main`, nothing run |
| tess-shell | none; the shell `Bar` is a panel of modules (see [[Bar]]) and the Menu and MenuItem modules exist (`tess-shell:src/tess_shell/shipped/Menu/Menu_Module.tdl`) | absent; the shell has no application window to hold a menu bar, so it is not applicable until an application surface exists |
| tre | `tre:docs/reference/node.md` (role list), `tre:crates/engine-py/src/node_props.rs` | the role `menubar` is not in the role list (0.6.11 adds `toolbar` but not `menubar`); `menu` and `menuitem` exist. A tre hook: the role `menubar` ([[UXREQ-011 Menubar role]]); until then the bar can use role `group` named "Menu bar", a deviation recorded below. The engine has a settable `active_descendant` on any node (TRE-REQ-023, `tre:LOG.md`, read at `origin/main`): the highlighted item can be exposed with it; the screen reader result (AccessKit sends the focused state moving, not `ActiveDescendantChanged`) is not checked with Orca |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A desktop menu bar, which MD3 does not have | The owner asked for a top menu (File, Edit, View) in the config app; the commands of a desktop application belong in menus with shortcuts | [[ADR-0029 Desktop density and type scale]] |
| Bar height 40, 32 and 28 dp and item padding 12, 8 and 8 dp | Desktop density levels; a 32 dp bar keeps a compact toolkit window uncluttered | [[ADR-0029 Desktop density and type scale]] |
| Hover on a title opens its menu at once while another menu of the bar is open | Desktop menu bar convention (Windows, KDE, GTK) and the APG pattern; MD3 menus open from one button | [[ADR-0029 Desktop density and type scale]] |

## Sources

- WAI-ARIA Authoring Practices, menubar pattern (one Tab stop, Left and Right between titles, Down, Up, Enter, Space open, Escape closes, Home, End, printable character): `https://www.w3.org/WAI/ARIA/apg/patterns/menubar/`; navigation menubar example and the menu button pattern: `https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/`.
- WCAG 2.2 SC 2.1.2 No Keyboard Trap, SC 2.5.8 Target Size (Minimum).
- Desktop conventions (Alt and F10 activation, Alt+letter mnemonics, underline shown on Alt, hover switching between open menus, shortcuts right-aligned in the item) are those of Windows, KDE and GTK applications and are stated from common desktop practice #needs-verification; per-platform sources were not fetched for this note.
- Menu behaviour, placement, timing and tokens: [[Menu]], [[Menu Item]]. Shell popup edge margin: [[Popup]].
- Mnemonic and shortcut text forms: `Ctrl+S` style chords are written as in [[11 Interaction]].
