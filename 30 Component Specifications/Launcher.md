---
title: Launcher
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, shell, launcher, panel, owner-feedback]
related: ["[[Panel and Surface]]", "[[Popup]]", "[[Dialog]]", "[[Applications Module]]", "[[Text Field]]", "[[List]]", "[[List Item]]", "[[Search]]", "[[Dismissal]]", "[[Global Shortcuts]]", "[[Keyboard Navigation]]", "[[Accessibility Announcements]]", "[[Bar]]", "[[Volume OSD]]", "[[Layer Window]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Owner Feedback 2026-11-20]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[Spacing and Density]]", "[[Theme Following the System]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# Launcher

> [!info] Summary
> The Launcher is a Panel on the overlay layer with exclusive keyboard that holds the Applications module: a text field over a list of installed applications that narrows as you type, operated from the keyboard alone. Tesserae-only surface; the nearest Material Design 3 pattern is the [Search view](https://m3.material.io/components/search/overview) (a search bar that expands into a list of results), and for focus and dismissal the [Dialog](https://m3.material.io/components/dialogs/overview) pattern, without its scrim. Source of truth in code: see Status in code.

The Launcher is not an MD3 element. It is a Panel ([[Panel and Surface]]) with a fixed module. The Search view gives the shape (field on top, results below, one selected result); a dialog gives the rule that focus goes in on open and returns on close. Unlike a dialog it dims nothing and does not block the pointer.

## Purpose

Find an installed application by typing and start it, from the keyboard alone or with the pointer, from anywhere in the desktop, in under a second.

## When to use and not

- Use when: the user opens a global search-and-start surface by a key (`Toggle_Launcher`, for example `Meta+Space`) or a button (`On_Click { Action: Toggle, Target: Launcher }`).
- Do not use when: the content is a menu anchored to a control ([[Popup]], [[Menu]]); the content is a message that needs an answer ([[Dialog]]); the content shows for a moment ([[Volume OSD]]).
- A launcher opened by a global key or an IPC command is a Panel on the overlay layer with exclusive keyboard, not a focused popup: it has no user-action serial for a popup keyboard grab ([[Popup]], AC-POP-16).

## Anatomy

1. Panel: floating, centred by the compositor, layer `OVERLAY`, `Keyboard: EXCLUSIVE`, 480 dp wide, height follows the content up to 400 dp.
2. Container: fill `surface_container` (shell `$color.surface_raised`), corner radius 12 dp, shadow, padding 12 dp.
3. Text field: placeholder "Search applications", 456 dp wide.
4. Result list: at most `max_results` rows (8), each a 40 dp row with a 24 dp icon, the application name, and the generic name or comment in a smaller muted line.
5. Message line: "No results", "No applications found" or "Could not start <name>"; empty otherwise.
6. Click-away layer: a transparent output-sized window on layer `TOP`, keyboard `none`, under the Panel, present while the Launcher is shown.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Shipped `Launcher` Panel | one line in `settings.tdl` gives it | added to the main shell's first Monitor when named and not written; 480 wide, `Height: AUTO`, `Max_Height: 400` |
| Custom `Launcher` Panel | a Panel written with that name replaces the shipped one whole | any size, place, style and module params |
| `show_comment: false` | a tighter list | one line per row |

## States

| State | Visual change | Token values |
|---|---|---|
| Hidden | the surface is kept mapped and draws nothing; no click-away layer | not applicable |
| Open, empty query | the most started applications first, then the rest by name | container `surface_container` |
| Open, typing | the list narrows at once; first result selected | selected row: 2 dp `primary` border, fill `surface_container` |
| Row hovered | row fill `surface_container` (the same as the card: no visible change today, see Status) | spec: state layer `on_surface` 8 percent ([[State Layers]]) |
| No results / error | message line in `on_surface_variant` | text 14 dp |
| Starting | the application starts detached; the Launcher hides and the field clears | not applicable |

Item states follow [[List Item]]; the text field follows [[Text Field]].

## Tokens used

| Part | Role or token |
|---|---|
| Container | `surface_container` (shell `$color.surface_raised`) |
| Shape | `medium` 12 dp (shell literal `Corner_Radius: 12`; the shell's own `$shape.medium` is 8 dp, so the value is a literal) |
| Elevation | level 2 (shell `Elevation: 20%` of the maximum shadow) |
| Application name | `on_surface`, 14 dp ([[Typography]] `body-medium`) |
| Comment and message | `on_surface_variant`, 12 dp (`body-small`) |
| Selected row | border `primary` 2 dp |
| Scrim | none: the Launcher is not modal |
| Motion | none by default: shown and hidden at once |

Roles and shell mapping: [[Colour Roles]]. The 12 dp radius is the MD3 `medium` step ([[Shape]]).

## Sizing and density

| Item | default | compact | dense |
|---|---|---|---|
| Container padding | 12 | 8 | 4 |
| Gap between field and list | 8 | 8 | 4 |
| Row height, single line | 40 | 32 | 24 |
| Row height, two lines (name and comment) | 40 | 40 | 40 |
| Row horizontal padding | 12 | 8 | 4 |
| Icon-to-label gap | 8 | 8 | 4 |
| Icon size | 24 | 20 | 20 |

Values from [[Spacing and Density]]. Today the module writes padding 12, gap 8, row height 40, icon-to-label gap 10 and a row padding `[10, 6, 10, 6]` from the default stylesheet; no density setting exists. The two-line row stays 40 dp because two text lines of 20 dp and 16 dp need 36 dp. The panel is 480 dp wide at every level, the field and list are 456 dp (480 minus twice the padding at default); the panel and the content scale with the scale factor, not with density.

## Layout and overflow

- Height: the Panel follows its content (`Height: AUTO`, up to `Max_Height: 400`); a short result list leaves no empty space. A content taller than the maximum is clipped, so the list never has more rows than fit: `max_results` is the limit, not a scroll.
- Application names and comments are single line and end in an ellipsis at the row's text width (456 minus icon minus padding); they never wrap and never paint outside the container ([[10 Layout Overflow and Scrolling]]).
- Single-line text is vertically centred in its row ([[Spacing and Density]], AC-DEN-9).
- The Panel sits where the compositor centres a floating layer surface on the shell's first Monitor; which monitor it opens on in a multi-monitor shell is open (candidate decision).

## Behaviour

- Opening: `Toggle_Launcher`, `Show_Launcher` or `Toggle` of `Launcher` shows the Panel. The text field takes the keyboard focus and its text is selected, so typing starts a new search. Keyboard is `EXCLUSIVE` because that works on the owner's KWin at once; `ON_DEMAND` gives no keys without a click.
- Typing narrows the list at once. Every word must match, without case or accents. Rank, best first: start of the name; start of a word of the name; anywhere in the name; start of a word of the generic name or a keyword; anywhere in the generic name, a keyword or the comment. Equal ranks sort by how often the application was started, then by name. An empty query lists the most started first.
- Keys: Down and Up move the selection and wrap; Page Down and Page Up move by the rows shown and stop at the ends; Enter starts the selected row; Escape clears the field, and with the field empty hides the Panel; the shortcut key toggles it. Focus stays in the text field; the list's selection moves from the field.
- Pointer: a click on a row starts it; hover does not change the selection (a resting pointer must not fight the keys). A click outside the Panel closes it (owner feedback S2, see below). A click on or around the field does not close it.
- Starting: the application starts detached from the shell, in a transient user scope `app-<id>-<random>.scope` when `systemd-run --user --scope` works. The shell asks the compositor for an activation token inside the Enter or click so the new window can take focus. The field clears and the Panel hides after a start.
- Touch: rows are at least 40 dp high; no touch-specific behaviour is specified.
- Multi-monitor: the shipped Launcher belongs to the first Monitor.

### Owner feedback S1: readable with no stylesheet

The shell Launcher was unreadable on a throwaway config: black text on a dark background, because the empty `Stylesheets` list left the text field and list with the engine's black default ([[Owner Feedback 2026-11-20]] S1). Shell ADR-0022 (accepted 2026-11-21) makes an absent `Appearance.Stylesheets` key mean `[Default]`; an explicit `[]` still means none, and `check` then emits a note when a text field or list is in use. The specification rule: a surface with no project stylesheet still shows a readable look and follows light and dark ([[Theme Following the System]], [[02 Colour and Theming]]).

### Owner feedback S2: click-away and keyboard grab

The first build of click-away closing used a popup grab (`PopupWindow(grab=True)`); on KWin that grab takes the keyboard from an exclusive layer surface, so nothing could be typed (hand check 2026-11-20, reverted). The accepted build is a transparent output-sized window on layer `TOP`, keyboard `none`, below the Panel, present while the Panel is shown. A press on it closes the Launcher and is swallowed (the user clicks again to use what lies below). The `active` event closes the Launcher only when another surface of the shell gains the keyboard after the Launcher had it; a keyboard that is only lost, with nothing gaining it, closes nothing (a seat's last keyboard device going away does that). Scope: a Panel with `Keyboard: EXCLUSIVE`, `Layer: OVERLAY` holding a use of the Applications module. Verified by the owner on real KWin on 2026-11-21 (via the Orchestrator): typing works, a click outside closes, a row click closes, Escape closes, a click on or around the field does not close it. The rules for dismissal in general are in [[Popup]] and [[Dismissal]].

## Tooltip and overlay behaviour

The Launcher carries no tooltip; rows are the controls and the row's accessible name carries the name and comment ([[Tooltip]], [[ADR-0004 Tooltip rule]]). The Launcher is an overlay: it sits on layer `OVERLAY`, above windows and above the Bar, takes no scrim, and traps no focus beyond holding the keyboard while shown ([[12 Overlays]]). It is not a dialog: a click outside closes it and does not activate what is below.

## Motion

- No animation by default: the Panel appears and hides at once. A custom Launcher may add `Animation { Type: SLIDE or FADE, Duration: 200 }` ([[Surface Animation]]); reduced motion makes that instant.
- The selection moves without animation.

## Accessibility

- Names: the text field's name is its placeholder ("Search applications"); the list is named "Results"; each row is a list item named "<name>, <comment>" with the state `selected`; the root is a group named "Applications".
- Announcements: the module says aloud, politely, the selected row, "No results" and "Could not start <name>" through one window of the shell ([[Accessibility Announcements]]). Whether Orca reads them is untested (Orca is not installed on the owner's machine). The text field exposes the selected row as its active descendant (shell ADR-0023, on origin/main) so a screen reader can follow it.
- Keys: Down, Up, Page Down, Page Up, Enter, Escape as above; the global key opens it ([[Keyboard Navigation]]). Every action is reachable by keyboard.
- Focus: on open, focus is in the text field; on close, the compositor returns the keyboard to the window that had it.
- Contrast: `on_surface` on the container 13.23 (dark), 16.46 (light); `on_surface_variant` 7.08 and 7.20; both at least 4.5 to 1. The selected row's border `primary` on the container is at least 3 to 1 in light and dark (the shell pairs against `surface` are 5.76 and 5.29).
- Selection is shown by shape (a border), not by colour alone.
- Target sizes: rows are 40 dp high at default (24 dp at dense, which meets the 24 dp minimum).

## Dark and light

The container and text resolve from the scheme; the shipped theme's `surface_raised` is `#1B222B` in dark and `#FFFFFF` in light ([[Colour Roles]]). The Default stylesheet carries text and list colours so a shell with no stylesheet key is still readable in both.

## Defaults

| Setting | Default |
|---|---|
| Layer, keyboard | `OVERLAY`, `EXCLUSIVE` |
| Size | `Width: 480`, `Height: AUTO`, `Max_Height: 400` |
| Visible | `false` (hidden until shown) |
| Style | `Background: $color.surface_raised`, `Corner_Radius: 12`, `Elevation: 20%` |
| `max_results`, `show_comment`, `icon_size` | 8, `true`, 24 |
| `placeholder` | "Search applications" |
| `Appearance.Stylesheets` absent | `[Default]` |

## Acceptance criteria

Check types follow [[Test Method]]. Hand checks on KWin follow the shell's hand-check kit and are recorded as "hand check, not automated".

- [ ] AC-LNC-1 (token test, shipped Panel): the shipped `Launcher` Panel has `Layer: OVERLAY`, `Keyboard: EXCLUSIVE`, `Width: 480`, `Height: AUTO`, `Max_Height: 400`, `Visible: false`, `Background` a role, `Corner_Radius: 12`, `Elevation: 20%` and holds one Applications use. Pass: 9 of 9 equal in the typed Panel definition.
- [ ] AC-LNC-2 (scripted input, open and focus): `Toggle_Launcher` shows the Panel within 1 frame of the action; the text field has focus, its text is selected, and typing "abc" within 50 ms replaces any previous text; the keyboard-lost event count in the 500 ms after show is 0. Pass: focus node is the field; field text "abc"; lost count 0 (see AC-POP-6 and AC-POP-7 in [[Popup]]).
- [ ] AC-LNC-3 (scripted input, ranking): with fixture entries "Firefox" (name starts with the word), "Pro Fire Tool" (a word of the name starts with it), "Wildfire Viewer" (inside a name word), "Flame" (keyword "fire torch"), "Notes" (comment "takes fire notes"), the query "fire" lists in this order: Firefox, Pro Fire Tool, Wildfire Viewer, Flame, Notes. Pass: order equal on this fixture; the query "FIRE" and "fíre" give the same list; with the query "fire tool" only "Pro Fire Tool" remains (every word must match); two entries of equal rank list the one started more often first. Pass: 4 of 4 checks.
- [ ] AC-LNC-4 (scripted input, keys): with 10 results and 8 shown, Down from the last wraps to the first; Up from the first wraps to the last; Page Down moves by the rows shown and stops at the last; Enter starts the selected application once; Escape with text clears it and keeps the Panel; Escape with an empty field hides it. Pass: selected index and Panel state after each key as stated.
- [ ] AC-LNC-5 (scripted input, hover does not select): moving the pointer over row 5 while row 1 is selected leaves row 1 selected. Pass: selected id unchanged after 500 ms.
- [ ] AC-LNC-6 (scripted input, row click): a click on a row starts that application once and hides the Panel with the field cleared. Pass: start count 1 with that id; Panel hidden; field text "".
- [ ] AC-LNC-7 (scripted input, click-away, S2): with the Launcher shown, a press on the click-away layer hides it and the press does not reach the window below; a press on or around the text field (within the container) does not hide it. Pass: Panel hidden after the first press, handler count of the window below 0; Panel shown after the second press.
- [ ] AC-LNC-8 (scripted input, keyboard stays, S2): with the click-away layer present, its keyboard mode is `none`, and after show the first keystrokes arrive in the field (AC-LNC-2). When another shell surface gains the keyboard after the Launcher had it, the Launcher hides; when the keyboard is lost with nothing gaining it, it stays. Pass: layer keyboard `none`; hide on gain; stay on loss.
- [ ] AC-LNC-9 (pixel check, click-away layer): the click-away layer's pixels are fully transparent (alpha 0 everywhere) and it dims nothing; its size equals the output. Pass: 0 non-transparent pixels in a 100-point sample; size equals the output (±0).
- [ ] AC-LNC-10 (scripted input, hand check on KWin): on a real KWin 6 session with a window focused beforehand: open by the shortcut, type, press Escape twice; typing works at once, the closing returns the keyboard to the previous window within 300 ms, and a click on a desktop area closes it. Pass: all five observations true (recorded by the checker with date; the owner did this on 2026-11-21 with the fixed-height Launcher).
- [ ] AC-LNC-11 (scripted input, start): the start runs the entry's `Exec` with field codes removed (`%f %F %u %U` removed, `%i` as `--icon <Icon>`, `%c` the name, `%k` the path, `%%` a percent sign), detached from the shell, as `app-<id>-<random>.scope` when `systemd-run --user --scope` is on the path, with an activation token requested inside the Enter or click event. Pass: command line, scope name pattern and token request count (1) as stated, in a test with a fake process starter (the shell never starts a process in its tests).
- [ ] AC-LNC-12 (geometry check, layout): at scale 1.0, 1.25 and 2.0 the container is 480 dp wide, content 456 dp wide, padding 12 dp, row height 40 dp, icon 24 dp, rows at most 8; a result list of 3 rows gives a Panel height of 12 + field height + 8 + 3 x 40 + 12 dp (field height as measured) with no empty space. Pass: widths and heights equal to the dp.
- [ ] AC-LNC-13 (geometry check, density): at the density levels the row height is 40, 32, 24 dp (single line) and the icon-to-label gap 8, 8, 4 dp, the row padding 12, 8, 4 dp. Pass: equal to the dp; today the gap is 10 and the row padding `[10, 6, 10, 6]` (fails AC-DEN-1 and AC-DEN-6).
- [ ] AC-LNC-14 (geometry check, overflow): an application with a 200-character name and comment shows a name that ends in an ellipsis within the text width; no glyph pixel lies outside the container; the row stays 40 dp. Pass: ellipsis present; 0 pixels outside; height equal.
- [ ] AC-LNC-15 (contrast script, S1): `on_surface` and `on_surface_variant` on `surface_container` reach 4.5 to 1 in dark, light and high contrast; the selected border `primary` on the container reaches 3 to 1 in each. Pass: 9 of 9 pairs.
- [ ] AC-LNC-16 (token test, no stylesheet, S1): a shell started with no `Appearance.Stylesheets` key resolves the stylesheet list to `[Default]`; with `Stylesheets: []` it is empty and `check` emits the note `appearance-no-stylesheet` when a text field or list is in use. Pass: list values as stated; note count 1.
- [ ] AC-LNC-17 (contrast script, no stylesheet, S1): with no `Appearance.Stylesheets` key the Launcher's text field text, placeholder, row text and comment text each reach 4.5 to 1 against their background in dark and light. Pass: 8 of 8 pairs. This is the pixel-level form of owner feedback S1.
- [ ] AC-LNC-18 (pixel check, hover, state layer): a hovered row differs from the container colour by a state layer of `on_surface` at 8 percent (a pixel check reads a colour distance of at least 3 in each channel from the container). Pass: distance at least 3. Fails today: the hover fill equals the container.
- [ ] AC-LNC-19 (AT tree assertion): the root is a group named "Applications"; the field has a non-empty name and exposes the selected row as active descendant; the list is named "Results"; each row has role list item, state `selected` on exactly one row, and a name of the form "<name>, <comment>"; the icon is hidden. Pass: all properties equal.
- [ ] AC-LNC-20 (scripted input, announcements): selecting a row sends one polite announcement with the row's name; an empty result list sends "No results"; a failed start sends "Could not start <name>". Pass: announcement count 1 each, politeness polite. Not yet heard with Orca.
- [ ] AC-LNC-21 (scripted input, reduced motion and animation): the shipped Launcher has no `Animation` and appears in one frame; a custom `Animation { Type: SLIDE }` is instant under reduced motion. Pass: end state on frame 1 in both cases.
- [ ] AC-LNC-22 (review, not a popup): the Launcher is a Panel on the overlay layer with exclusive keyboard, takes no scrim, and is not a focused popup ([[Popup]] AC-POP-16). Pass: reviewer finds the surface type as stated.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/default_panels.py` (shipped Panel), `tess-shell:src/tess_shell/shipped/Applications/Applications_Module.tdl` and `Applications_Style.tdl`, `tess-shell:src/tess_shell/surfaces/manager.py` (click-away layer, M7k), `tess-shell:src/tess_shell/config/settings.py` (stylesheets default), `tess-shell:docs/guide/keyboard.md#the-launcher` (origin/main, 2026-11-21) | Partly meets. Meets AC-LNC-1, AC-LNC-16 (default `Default`, check note), AC-LNC-7 to AC-LNC-9 (catcher on `TOP`, keyboard none, fill alpha 0, swallows the press; owner's KWin check passed 2026-11-21), AC-LNC-2 to AC-LNC-6, AC-LNC-11, AC-LNC-19 in design (unit tests reported, not run here). Fails AC-LNC-13 (row padding `[10, 6, 10, 6]`, gap 10; no density setting), AC-LNC-18 (hover fill `surface_raised` equals the card). AC-LNC-15 and AC-LNC-17 have no recorded contrast script result (the shell's measured pairs support them). AC-LNC-10 hand check and AC-LNC-20 (Orca) not run. Opening monitor: the first Monitor of the main shell only. |
| shell vault | `shell-vault:40 Specifications/Modules/Applications Module.md`, `shell-vault:40 Specifications/Surfaces/Panel.md`, `shell-vault:30 Decisions/ADR-0022 Default Stylesheet.md` | Source design. The owner's decisions: exclusive keyboard (2026-11-16), fixed 480 by 400 then content-sized (2026-11-17), click-away closing (verified 2026-11-21). |
| tess-ui | not applicable | tess-ui has a [[Search]] bar and view for application windows; no launcher. |
| tre | `tre:docs/reference/layer-window.md` | Mechanism only: `LayerWindow` with `keyboard="exclusive"`, `activation token`, `input_region`. A request exists for an outside-press on layer surfaces (TRE-REQ-024); the shell does not rely on its popup-grab recipe on KWin. |

Risk noted, not a finding: the click-away layer is an output-sized window; an output-sized transparent surface cost 177 MiB at 4K in an early tre measurement (shell vault, before later changes) and has not been re-measured.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A desktop launcher surface with exclusive keyboard, no scrim (MD3 Search view is a modal full-screen view on phone) | global search-and-start on a desktop; the owner chose no dimming | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| A click outside closes it and the click is swallowed | Wayland shows no outside press to a client; the click-away layer takes it | none (compositor limit) |
| Container `surface_container` at level 2 with a 12 dp radius and 20 percent shadow | shell flat roles and one scalable shadow | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Rows 40 dp single and two-line (MD3 list one line 56 dp #needs-verification) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- Search bar and search view as a pattern (full-screen modal search view, docked variants): https://github.com/material-components/material-components-android/blob/master/docs/components/Search.md (no numeric height read for a docked view; #needs-verification) and https://m3.material.io/components/search/overview (script-rendered, not readable).
- Dialog container `surface_container_high`, level 3, scrim opacity 0.32 (for the contrast with the Launcher, which uses neither): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-dialog.scss and `_md-comp-scrim.scss`.
- Shape `medium` 12 dp: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-shape.scss.
- WCAG 2.2 SC 1.4.3, 1.4.11, 2.1.1, 2.4.3: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html , https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html , https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html , https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html.
- Desktop Entry Specification (Exec field codes, `NoDisplay`, `OnlyShowIn`): https://specifications.freedesktop.org/desktop-entry-spec/latest/.
- Shell: `shell-vault:40 Specifications/Modules/Applications Module.md`, `shell-vault:40 Specifications/Surfaces/Panel.md`, `shell-vault:30 Decisions/ADR-0022 Default Stylesheet.md`; `tess-shell:docs/guide/keyboard.md#the-launcher`, `tess-shell:src/tess_shell/surfaces/manager.py`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` (origin/main, 2026-11-21).
