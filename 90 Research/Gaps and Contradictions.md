---
title: Gaps and Contradictions
type: research
status: research
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [research, inventory, gaps]
related: ["[[Inventory]]", "[[Existing Tokens]]", "[[Plan]]", "[[Open Questions]]"]
depends_on: []
---

# Gaps and Contradictions

What Phase 0 found between the Tesserae projects: missing elements, drift between docs and code, contradictions between projects. The evidence sections below are the unedited findings of the five readers, with source paths; the summary comes first. Each item feeds a rule in the specifications or a request to a project (through the Orchestrator).

## Summary: the ones that shape the specifications

1. Tooltips: tess-ui shows them after 500 ms and immediately on keyboard focus; the engine has no tooltip primitive, timers or placement policy; the shell has a `Tooltip` key and a Popup flag; the config app puts a tooltip on whole rows. Owner feedback (2026-11-20): tooltips on whole rows and not closing. Needs one rule for trigger area, delay, dismissal (Escape, scroll, pointer leave) and keyboard access.
2. Tree and list density: tess-ui has no density scale, only `Compact` on `Tree` (40 px rows against 56); the shell has none; the config app uses `Compact` trees and the owner reported indentation and chevron gaps. The virtual list scrolls by wheel only and has no key navigation in the engine docs.
3. Scrollbars: tess-ui styles colour only, the engine draws a 4 px thumb with no track and no auto-hide, the shell has no scrollbar and a long list has no scroll affordance. Owner feedback: missing horizontal scrollbars.
4. Dark theme: tess-ui follows the OS but flashes (starts dark, flips on the first frame when the OS is light); the config app relies on roles and sets three rules; the shell defaults to dark and has an empty Dark block. Owner feedback: dark theme ignored.
5. Text overflow: text inputs show ellipsis only until focused; unsized text hugs its text plus 2 px; owner feedback of text without ellipsis and top-aligned single-line text. Needs a rule for ellipsis, vertical centring and minimum widths.
6. Two token systems (tess-ui MD3 roles against shell flat roles) and a tess-ui theme path that reads sizes from two places (`Components` block for Python widgets, stylesheets for views).
7. State feedback and disabled look: MD3 percentages in tess-ui, literals in the shell, none in the engine; disabled is an accessibility flag only in the engine.
8. Missing common patterns in every project: empty, loading and error states, validation, notifications, multi-select, drag and drop of content, modal scrim use.
9. Shell design intent not built: Bar auto-hide and visibility, Popup animation and attach, Frame elevation and shadows, Panel open-with-target, Grid, Square, Ellipse, Triangle, Hexagon, Terminal, Canvas blocks; no dialog or notification element.
10. Documentation drift: `COMPONENT_LIST.md` in tess-ui marks ten components "Python only" that ship as views or nodes; the shell design note calls the token system "not started" although it ships; two vault notes contradict on whether Tooltip is a module.
11. Accessibility: no run with a real screen reader in any project (Orca not installed on the owner's machine); active descendant unreleased in the engine; high contrast and reduced motion are headless-tested only; the contrast script required by the shell vault does not exist.
12. Icons: the engine draws paths only, tess-icons holds Material Design Icons (Pictogrammers) and Line MD, not Material Symbols; tess-ui carries two sets with different view boxes.


## Evidence: tess-ui components


Evidence paths are relative to the tess-ui project root (`tess-ui:`).

### Doc-vs-doc and doc-vs-code drift

- `tess-ui:COMPONENT_LIST.md` still labels Carousel, Pagination, Segmented buttons, Time input, Splitter, Window, Title bar, Dock, Dock panel and Routed views "Python only" / "(Python Only)". Shipped TDL views exist for Carousel, Pagination, SegmentedButton, TimeInput (`tess-ui:src/tess_ui/views/*_View.tdl`); Splitter, Window, TitleBar, Dock, DockPanel are primitive node kinds declared in `tess-ui:src/tess_ui/spec/builtin_widgets.py`. Only Routed views has no view of its own (it is a call with `Route:`, `tess-ui:docs/components/routed-views.md`).
- `tess-ui:COMPONENT_LIST.md` has typos: "Sugmented buttons", "ToolbaarFloating". Its header says 122 entries; it lists Tooltip, TabsItem, MenuItem, TreeNodeBranch/Leaf, Fab variants as separate entries although code has one view each (Fab, Tabs, Menu, Tree/TreeNode).
- `tess-ui:COMPONENT_LIST.md` lists Toolbar as ToolbarDocked and ToolbarFloating; code has one `Toolbar` view with `Variant: docked|floating` (`tess-ui:docs/components/toolbars.md`).
- `tess-ui:docs/components/index.md` says Extended FABs are "the fabs view"; there is no separate extended-FAB view, only `Fab` with an extended form (`tess-ui:src/tess_ui/views/Fab_View.tdl`).
- Tooltip is not a component view: it is the `Tooltip:` node property (plain and rich) plus `Tooltip` overlay in `tess-ui:src/tess_ui/overlays.py` (`tess-ui:docs/components/tooltips.md`). `tess-ui:docs/components/index.md` says "see the page".
- `tess-ui:docs/schema/tess-ui-widget-schema.json` is titled "Tesserae view node (0.5.0)" while the package is 0.6.3 (`tess-ui:pyproject.toml`) and views declare `Tesserae: "0.6"`.
- `tess-ui:docs/guide/widget-catalog.md` describes Python factories (`widgets/*.py`) and TDL views as separate definitions of the same widget; a `Button_View.tdl` of a project changes only the TDL one. Two sources of look for one element (design intent in `tess-ui:design/factories-on-tdl-views.md` is to unify them; whether that is finished is not stated in the docs read).
- `tess-ui:docs/stylesheets/` has 36 per-component folders but only `buttons` was checked to hold a page (`button.md`); not every one of the 58 component pages has a stylesheet page (for example dock, window, splitter, node graph, tooltips have none).

### Documented but "Not built" (each page says so)

- Buttons, icon buttons: 12% container colour for disabled filled (`tess-ui:docs/components/buttons.md`, `icon-buttons.md`).
- Button group: pressed button widening, neighbours giving way, overflow button.
- Split button: toggle form.
- FAB and extended FAB: eased collapse and extend.
- Cards: drag, swipe, dragged state. Lists: swipe actions, drag reorder.
- Snackbar: swipe to dismiss, lift above FAB or bottom bar; dialog and snackbar text one line (`tess-ui:docs/guide/overlays.md`, "Not yet covered").
- Dialog: focusing a default action. Side sheet: detached sheet. Navigation drawer: modal drawer slide-in.
- Tooltip: reach rich-tooltip actions by keyboard (accessibility gap).
- Menu: submenus (chevron only), right-click opener in a view, exposed dropdown under a text field.
- Tabs: scrolling tab bar. Toolbar: slide away (fades only). Top app bar: contextual action mode.
- Text field: arrow-key movement into suggestions, input-method UI. Spin box: accelerating hold, vertical arrangement. Date picker: range picker. Time picker: 24-hour inner ring.
- Tree: lazy children, multi-select, drag reorder, context menu. Accordion: eased height. Carousel: size change while scrolling.
- Node graph: ports and connecting, edge labels, multi-select, minimap, undo. Video: decoder, fullscreen, speed, volume, poster.
- Colour picker: HSL, OKLCH, eyedropper. Icon picker: categories. Font list: sample sentence, favourites. Key chord field: multiple chords, two-step chords, conflict list, keypad and media keys. List editor: drag or Alt+arrow row move, mixed or nested items. Token button: tree by dotted name, alias tokens. File dialog: places sidebar, preview, drag and drop, rename, delete.
- Window: native menu bar. Title bar: Windows 11 snap layout. Dock: floating panels, panels found by title only (duplicate titles clash), tab reorder, dragging a half's own content (`tess-ui:docs/guide/docking.md`, `tess-ui:docs/components/dock-panel.md`). Routed views: push/pop stack.
- Status bar: items draggable or hidden on narrow windows. Pagination: items per page, total count, jump-to. Image: clip to any shape except circle through the `avatar` class.

### Foundations missing or thin

- Density: no density scale. Only `Tree` has `Compact` (40 px rows instead of 56, `tess-ui:src/tess_ui/views/Tree_View.tdl` line 15); the config app uses it (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, Files and Structure trees). Maintainer feedback on tree density (config-app demo, 2026-11-20, recorded in the UX vault `AGENTS.md`) has no counterpart in tess-ui docs.
- Scrollbar: only colour is set (theme `outline`, `tess-ui:src/tess_ui/spec/build.py` around line 693; `tess-ui:docs/guide/layout.md` line 472); no width, track, hover or auto-hide specification. Maintainer feedback on scrollbars (same demo) has no doc.
- Tooltips: maintainer feedback on tooltips (same demo) vs. docs: delay 500 ms default, rich actions not keyboard reachable (`tess-ui:docs/components/tooltips.md`). The config app puts the key's doc line in a tooltip on each choice (`Main_View.tdl` line 435).
- Dark theme: maintainer feedback on dark theme (same demo); tess-ui follows OS light and dark (`tess-ui:src/tess_ui/follow.py`); the config app stylesheet sets only three rules (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_Stylesheet.tdl`) and relies on roles. No quoted tess-ui source for the feedback itself was found in LOG.md, PLAN.md, CHANGELOG.md or the app README.
- Empty, loading and error states: no common pattern. Only SearchView has `Empty` text; Button has `Loading`; TextField has `Error`; Checkbox and RadioButton have `error`.
- Validation: per component only; the config app refuses out-of-range numbers and shows the range in a `row_error` text (README "The form" table). No form-level pattern.
- Notifications: Snackbar only; there is no system or persistent banner, and the config app hand-builds a disk-change banner (`Main_View.tdl` lines 974-1000).
- Multi-select: absent from Tree, NodeGraph, List.
- Disabled: `tre` `disabled` is announce-only; Tesserae makes it behave (`tess-ui:src/tess_ui/a11y.py`). Disabled look is a whole-widget fade (38% on pickers) not MD3's per-part 12% and 38% scheme.
- State layer, ripple and focus ring apply to plain nodes only for `Rect` and `Container` (`tess-ui:docs/guide/interaction.md`, "Not yet covered"); a resized focused node keeps its old ring.
- Easing is not settable on `Transition` (`tess-ui:docs/components/text-fields.md` line 38). Motion tokens: see the token fragment owner.
- Typography has per-role tracking 0 as drawn by the engine; `MD3_TRACKING` exists but is not the default (`tess-ui:src/tess_ui/tokens.py` lines 259-291).
- Window size classes exist (`tokens.py` line 207) but no guide page states a layout spec per class beyond the Dialog fullscreen advice.

### Config app (`tess-ui:apps/shell_config`) coverage notes

- Hand-built instead of shipped views: toolbar (Container of Buttons, not `Toolbar`), status line (Container, not `StatusBar`), form group headers (Container + chevron Icon, not `Accordion`), disk-change banner, problems list (ScrollView of rows), pane headings. These are candidates for specs or for migration onto the shipped views.
- Shipped views used: Button, IconButton, TextInput, Switch, Tree, Dialog (2), Menu, ScrollView, TokenButton, ListEditor, KeyChordField, IconPicker, FontList, FileDialog, ColourPicker (`Main_View.tdl`). Not used by any app or example: Badge, ButtonGroup, Card, Carousel, Chip, DatePicker, Divider, Fab, NavigationDrawer, Pagination, SearchBar, SideSheet, Snackbar, SplitButton, SegmentedButton, Tabs, TimePicker, TopAppBar, VideoPlayer, NodeGraph, Link, ListItem, Accordion (examples only use Button, IconButton, Checkbox, TextInput, TextField, NavigationRailScreens, StatusBar, Window, Dock, DockPanel, TitleBar, Tree, ScrollView). Their status is "exists, covered by unit tests", not by a real app.
- Form widgets by schema kind (Python `WidgetRegistry` in `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py`, lines 738-779): switch, choice (a button opening a list), number (suffix unit, range refusal, Up/Down step), length (field plus unit button), sides (one or four fields, Linked/Separate), colour (ColourPicker), text, path (with Browse), icon, font, key chord, list, block (Add/Open/Reset), tooltip, expression (TDL text fallback). Fallbacks to the generic text field: 13 no-kind keys, 14 block, 35 list, 11 shadows, 4 font, 12 tooltip, 5 icon per `LOG.md`.
- Layout (`Main_View.tdl`): toolbar on top; panes Files, Structure, Form side by side; Text pane, errors list, Problems pane, status bar; overlays picker, prompt, structure menu. Keyboard map in `tess-ui:apps/shell_config/README.md` (F6 cycles areas, Ctrl+Shift+N/D/M structure actions).
- Component pages in `tess-ui:docs/components/` for List editor, Colour picker, Icon picker, Font list, Key chord field and Token button describe elements that exist only in tess-ui (no MD3 counterpart), driven by the config app.

### Undocumented behaviour found in code only

- Gradient focus ring option (`tess-ui:src/tess_ui/focusring.py`, `App(focus_ring="gradient")`) and single-shader ripple (`tess-ui:src/tess_ui/ripple.py`, `App(ripple="shader")`): behaviour options on the foundation, not described in `tess-ui:docs/components/` pages.
- Typing and caret effects (`tess-ui:src/tess_ui/typing_effects.py`) are a text input feature outside MD3.
- No owner-feedback statements on real behaviour were found in tess-ui sources; the only pointer is the vault `AGENTS.md` (config-app demo 2026-11-20: tooltips, tree density, scrollbars, dark theme).


## Evidence: tess-ui tokens and foundations


- Emphasized easing drift: `tess-ui:src/tess_ui/theme.py:47` `emphasized` = (0.2, 0, 0, 1) but `tess-ui:src/tess_ui/spec/transition.py:36` `emphasized` = (0.3, 0, 0, 1). The Theme API and a `Transition` block give different curves for the same name; screen transitions use the transition.py one. theme.py docstring says tess_re's emphasized is two segments one bezier cannot express.
- Duplicated motion constants: `PRESS_GROW_MS`, `PRESS_FADE_IN_MS`, `MINIMUM_PRESS_MS`, `RELEASE_FADE_MS`, `INITIAL_SCALE` appear in both `tess-ui:src/tess_ui/interaction.py:45-55` and `tess-ui:src/tess_ui/ripple.py:26-31` (one source of truth needed).
- Ripple timing is Material Web's, not an MD3 token; ripple, hover (15 ms) and stylesheet transitions (150/200 ms literals in `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl:13`, `Card_Stylesheet.tdl:14`) do not use the duration tokens in `tess-ui:src/tess_ui/theme.py`.
- Type tracking: `tess-ui:src/tess_ui/tokens.py` `TYPE_SCALE` tracking is 0 for every role; MD3's tracking values exist only as `MD3_TRACKING` and are not applied. Differs from MD3 for display_large, title, body, label roles.
- Type scale values compared to MD3 line heights: line heights are ratios rounded to 2 decimals (e.g. 1.12 x 57 = 63.84, MD3 64), so rendered line height differs by up to about 0.2 px.
- Tooltip text uses literal Roboto 12 and 14/500 (`tess-ui:src/tess_ui/composed.py:813-819`), not `body_small`/`label_large` lookups; a theme `Typography` override does not reach tooltips. Tooltip radii (4, 12) and padding (8x4, 16x12) are literals in composed.py, while `Tooltip { Corner_Radius: 4 }` exists in `tess-ui:src/tess_ui/spec/default_theme.tdl:76` and is not read by this code path.
- No density tokens or setting anywhere in `tess-ui:src/tess_ui`; desktop density (a Tesserae departure from MD3 recorded in the vault rules) is unspecified in code.
- No spacing tokens; literals everywhere in `tess-ui:src/tess_ui/views/*_Stylesheet.tdl`. One off-grid value: Snackbar text padding 14 (`Snackbar_Stylesheet.tdl:25`).
- Scrollbar: only colour (`outline`, `tess-ui:src/tess_ui/spec/build.py:697`, `tess-ui:docs/guide/layout.md:472`) is styled; width, thumb shape, hover/fade behaviour, minimum thumb are engine-owned and undocumented in tess-ui. No scrollbar stylesheet or token.
- Scrim: docs say Dialog and SideSheetModal scrims put transparency in the colour so `Colors { Scrim }` does not reach them (`tess-ui:docs/themes/index.md`); `Dialog_Stylesheet.tdl:7` says the scrim is the modal Overlay's. The `scrim` role exists (`tokens.py` ROLES) but is effectively unused by the shipped dialogs; value not located in the stylesheet.
- Elevation: no surface-tint overlay; `surface_tint` role generated but not applied by level. Shadow geometry (`tokens.py` `elevation_shadows`) is tess_re's legacy formula, not MD3's published shadow values; ambient shadow spread is non-zero (spread 1..6), unlike MD3.
- Shape scale lacks MD3 Expressive tokens (large increased, extra large increased, extra extra large); Button sheet hard-codes 12/16/28 (`Button_Stylesheet.tdl:37,43,55`). `default_theme.tdl:89-91` gives the navigation rail indicator radius 16, while MD3 indicator is a full pill #needs-verification.
- Button icon size for size `s` is 18 (`Button_Stylesheet.tdl:162`) while IconButton `s` icon is 24 (`IconButton_Stylesheet.tdl:52`); MD3 Expressive small button icon is 20 #needs-verification.
- Icons: static paths, no Material Symbols weight/fill/grade/optical size axes (`tess-ui:src/tess_ui/icons.py`). Two sets with different view boxes (Symbols 0 -960 960 960, MDI 0 0 24 24).
- Focus ring colour is `secondary` in code and docs (`tess-ui:docs/guide/interaction.md:31`); focus ring is shown only on keyboard focus, clicking never shows it (undocumented consequence: pointer users get no focus indication).
- Gradient focus ring and shader ripple are optional App flags (`App(focus_ring="gradient")`, `App(ripple="shader")`) with no MD3 counterpart; default off.
- Dark/light following: on macOS and Windows the app starts dark and flips on the first frame if the OS is light (`tess-ui:docs/themes/index.md`), a visible flash; headless starts dark. Not an MD3 matter but a UX defect to specify.
- High contrast: only contrast 0 or 1 is produced (`App(high_contrast="system")`); MD3 defines standard/medium/high levels and the scheme accepts -1..1 but the app never uses the middle values.
- Default theme has no seed (`tess-ui:src/tess_ui/spec/default_theme.tdl`); the no-theme baseline `BASELINE` (24 roles) overlays the #6750A4-generated scheme and differs from it (e.g. primary #6750A4 vs generated #65558F), so a themeless widget and a seed-#6750A4 app show different primaries.
- Four light `on_*_container` roles use tone 10 where newer material-color-utilities uses tone 30 (`tokens.py` `_TONE_10_LIGHT`); deliberate parity with tre, deviates from current MD3 #needs-verification.
- Tooltip delay 500 ms is claimed as "Material 3" in a code comment (`tess-ui:src/tess_ui/composed.py:729`) with no source; #needs-verification.
- Docs vs code: the docs state the `Components` block is read only by widgets built in Python, not by views (`tess-ui:docs/themes/index.md`); views read their own `*_Stylesheet.tdl`. Two parallel shape/elevation sources exist (default_theme.tdl `Components` vs the sheets) with values that must be kept in sync by hand (e.g. Snackbar 4/3, Dialog 28/3, Menu is absent from `Components` yet 4/2 in `Menu_Stylesheet.tdl`).
- Two token vocabularies: tess-ui uses MD3 role names; the shell_config fixture theme (`tess-ui:apps/shell_config/tests/fixtures/shipped/Themes/Default_Theme.tdl`) uses Color/Type/Shape/Space/Elevation/Motion/Modes with different names (Surface_Raised, On_Surface_Muted, Warning, Success, Accent; Shape Full 999; Duration 100/200/400). No mapping between them is documented in tess-ui. Warning and Success have no MD3 role.
- Shell fixture type scale (Caption 12/16, Label 13/18, Body 14/20, Title 18/24, Display 28/36) does not match MD3 sizes (13 and 18 are off-scale).
- Window size classes use only width and height thresholds; MD3 pane/layout recommendations for each class are not encoded.
- Empty, loading and error screen patterns are not tokens or widgets in tess-ui; only per-widget `loading` (Button) and a11y `busy`.
- No owner feedback on real behaviour was found in tess-ui LOG.md, PLAN.md or CHANGELOG.md by keyword search (owner, feedback, "user said" returned only process notes such as the 0.6.0 release instruction at `tess-ui:LOG.md:3186`).


## Evidence: tess-shell


Run note: `tesserae-shell schema --json` failed with the project venv as installed (engine tesserae-engine 0.6.7 in the venv, source requires >=0.6.9: `unknown node property "tab_navigates"`, `tess-shell:src/tess_shell/binder/tables.py:413`; `tess_utils` also missing from the venv). The schema was produced by prepending the tre working tree's built `python/` package and tess-utils `src` to PYTHONPATH with DISPLAY unset. Result: schema_version 4, 27 kinds, 25 roots, 13 blocks, 31 modules, 8 settings sections, 19 events, 5 actions, 6 token groups. [INFERENCE] the venv and `uv.lock` are stale against `tess-shell:pyproject.toml:22` (`tesserae-engine>=0.6.9,<0.7`).

### Doc versus code drift

- The design note says tokens, components, iconography and motion are "not started": `tess-shell:docs/design/50 Design System/50 Design System.md` (last line). Code has a full six-group token set and shipped theme: `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`; guide `tess-shell:docs/guide/styling.md#tokens`.
- `Style, Theme and Stylesheet Files` calls the Theme and Stylesheet files "Not yet Designed" (`tess-shell:docs/design/41 TDL Reference/Style, Theme and Stylesheet Files.md:74,91`), yet both ship and are in the guide.
- Building Blocks decides blocks Grid, Square, Triangle, Hexagon, Ellipse, Terminal, Canvas (`tess-shell:docs/design/50 Design System/Building Blocks.md`, table "The Blocks"). The schema has 13 blocks and none of these (`sh-schema.json` blocks: Box, FlexBox, Text, Rectangle, ScrollBox, Spacer, SVG, Bitmap, Circle, Ring, Path, Marquee, TextField). Spacer is a block in code and a module in the docs.
- Standard Modules lists a Tooltip module (`tess-shell:docs/design/50 Design System/Standard Modules.md:265`); code has no Tooltip module: tooltips are the `Tooltip` key, an inline `Tooltip` root and `Popup { Tooltip: true }` (`tess-shell:src/tess_shell/schema/blocks.py`). Six modules repeat the same tooltip card literals (Clock, Audio, Media, Network, Battery, Tray_Item: Gap 4, Corner_Radius 8, Elevation 20%, Padding [12,8,12,8]) instead of one shared style.
- Bar spec decides Auto_Hide and vertical-bar behaviour (`tess-shell:docs/design/40 Specifications/Surfaces/Bar.md:85`); the loader reads but does not build Exclusive_Zone, Input_Region, Auto_Hide, Auto_Hide_Delay, Visible, Attach_To, Meld, Animation, Text_Rotation, Padding, Class (`tess-shell:src/tess_shell/schema/blocks.py:419`; guide `tess-shell:docs/guide/surfaces.md:262,274`). A Bar cannot be hidden.
- Popup: Attach_To and Animation not built (`tess-shell:src/tess_shell/schema/blocks.py:692`). Frame: Children, Border_Tile, Meld, Exclusive_Zone, Input_Region error as not built and Class warns (`blocks.py:471-478`); Frame Elevation, Shadows, Shadow_Bleed not built (`blocks.py:500`). Panel: Open_With_Target, Exclusive_Zone error; Margin, Padding, Class warn (`blocks.py:610-629`).
- A melded Panel ignores Movable, Keyboard, Input_Region, Shortcut_Mode and the style keys Background, Fill, Opacity, Elevation, Shadows, Shadow_Bleed (`blocks.py:617-625`): it is drawn in the Frame's colour, so a dock has no surface of its own.
- Fallback shadow differs from the theme: `DEFAULT_MAX` is #00000040 (`tess-shell:src/tess_shell/binder/shadow.py:30`), the shipped theme's `$elevation.max` is #00000066 (`Default_Theme.tdl:58`). A theme with no Elevation.Max gets a lighter shadow than the default theme.
- Focus ring fallback is #5B97C9 and 2 px (`tess-shell:src/tess_shell/model/look.py:140-141`): equals default primary and step_1 only while the defaults hold.
- Styling guide's generated style-key table lists theme token groups for Font_Family as "color, motion" and for Border_Width and Opacity as "type, shape, space, elevation, motion" (`tess-shell:docs/guide/styling.md:283-312`); these look like generator artefacts, not real token links.
- Guide says the `Default` Dark mode block is empty; `Default_Theme.tdl` has `Dark { }` and `Reduced_Motion { }` both empty, so reduced motion works only through code (`model/look.py:_motion`), not theme values.
- Accessibility note says shipped themes are checked by a contrast script (rule 9, `tess-shell:docs/design/60 Quality/Accessibility.md`); no script result is recorded in the note, and acceptance boxes are unchecked.

### Missing UX elements (absent in code)

- No state-layer or ripple system: states change Background, Border_Color or Opacity in `Default_Stylesheet.tdl` (hover 0.85, pressed 0.7, disabled 0.5 are literals; hovered Button changes only the border).
- No density setting; control heights are literals (Button 32, MenuItem 28, Toggle 40x22, Checkbox 18, Slider 160x20, ProgressBar 160x8).
- Modules use pixel literals, not `$space.*` or `$shape.*` tokens, except the stylesheet rules (shape tokens) and Badge/Slider corner radii.
- No scrollbar styling or visible scrollbar key on ScrollBox; No scrim use: `$color.scrim` is defined but no surface or module references it (modal surfaces do not exist).
- No dialog, snackbar/toast, notification centre or notification server (outside v1: `tess-shell:docs/design/10 Vision/V1 Scope.md:84`); only OSD (Volume_OSD) and a Panel pattern.
- No wallpaper or BACKGROUND layer (Layer enum is BOTTOM, TOP, OVERLAY; Bar and Frame accept TOP only).
- No indeterminate/circular progress, no slider value bubble, no checkbox indeterminate, no text-field error, helper or label states, no tabs, chips, cards, dividers (MenuItem has a rule part only), search field chrome.
- No content drag and drop; Movable is the only drag of a surface, and not for melded Panels.
- No palette generation or tonal roles; no letter spacing in the type scale; only one button variant.
- `Reveal_Key` removed from Bar (`blocks.py` BAR_REMOVED): no key reveals a Bar.

### Owner feedback on real behaviour

- Frame look failed the owner's test on KWin (2026-11-06): join shows a 90 degree angle then a chamfer, join edge slightly pixelated, dock overlays the right edge button while opening, text not centred in buttons and panels, no peek. Source: `tess-shell:docs/design/40 Specifications/Surfaces/Frame.md:214`. Five join implementations were then built behind `Debug { Frame_Join }` (`tess-shell:src/tess_shell/surfaces/join*.py`); retests 2026-11-07 and the choice are in Frame.md:242. Status of the default join is not stated in code docs.
- Peek triggers and handles pass on KWin (2026-11-08): "Everything implemented looks good"; owner asked for adjustable handle brightness (`Handle_Opacity`, default 0.6) and content fade on slide (`Content_Fade`, default true), both accepted (`Frame.md:353-366`). Frame peek `Size` and a button inside a panel body were untested for lack of a demo knob.
- Popup faults found on KWin (2026-11-06): top-Bar popup sits 4 px below the button not the Bar and is misaligned, shadowed popup stays ~30 px from the edge, Escape does not close a popup, shadow margin takes clicks (`tess-shell:docs/design/40 Specifications/Surfaces/Popup.md:239-250`). Shadow click-through fixed by tre 0.6.5 `input_region` ("shadows have click through now and works well", 2026-11-07). The Escape fault has no recorded fix in that note while the guide says Escape closes (`tess-shell:docs/guide/surfaces.md:653`): contradiction to verify.
- Frame 1080p measurements: first window costs ~77 MiB RSS; 4K not measured (`Frame.md:190`).
- Orca not installed on the owner's machine; screen-reader behaviour of the Launcher and announcements is untested: `tess-shell:docs/design/00 Home/Hand Checks.md` (M7g kit) and `Accessibility.md` notes. Announcements go through a single window (Frame, else Bar) by owner decision 2026-11-19; whether Orca reads an unfocused window is untested.
- High contrast is tested headless only: the owner's desktop has no such setting (`Accessibility.md` rule 10).
- Active-descendant for the Launcher list is unreleased in tre (TRE-REQ-023); until then selection is announced with polite messages.
- Never physically hot-plug monitors (owner, 2026-11-17): hotplug tested only on virtual outputs.

### Other contradictions and open points

- Panel layer enum in code is BOTTOM, TOP, OVERLAY; Bar and Frame TOP only (`blocks.py`), but the layer-shell protocol and Surface Types doc name BACKGROUND (`tess-shell:docs/design/40 Specifications/Surfaces/Surface Types.md:98`).
- Panel Alignment default is CENTER, Popup Alignment default START: the same word has different defaults per surface (`sh-schema.json`).
- `Dock` is not a code kind: it exists only as a pattern (melded Panel plus Peek, or a floating Bar with Gap) in `tess-shell:docs/guide/surfaces.md`.
- Three Tray_Menu popups are hard-wired for submenu depth (Tray_Menu, _2, _3): deeper tray submenus are not supported (`tess-shell:src/tess_shell/schema/default_popups.py`).
- Role enum has 24 ARIA-like roles (BUTTON to SEPARATOR); `DIALOG` and `ALERT` roles exist with no dialog or alert element.
- Shell and tess-ui share no tokens or code by decision (ADR-0006); parity with MD3 roles is therefore not guaranteed and the two token sets must be reconciled in the design-system vault (see sh-tokens.md, section Differences).


## Evidence: Shell vault against code


Vault paths are prefixed `shell-vault:`; code paths `tess-shell:`. The vault is design intent plus code-session reports ("not run in the vault"); code was checked only by quick reads of tess-shell sources (version 0.2.0 tree).

### Vault intent against code

- **Auto-hide is specified on by default, but is not built.** Vault: "On by default; the user opts out with `Auto_Hide: false`", delay 1000 ms (`shell-vault:40 Specifications/Surfaces/Bar.md` Auto-hide). Code: `Auto_Hide`, `Auto_Hide_Delay` marked "Not built" and `Reveal_Key` deletion advised because "a Bar is always shown" (`tess-shell:src/tess_shell/schema/docs.py` lines 189 and 190; `tess-shell:src/tess_shell/schema/blocks.py` line 433). The vault Bar accessibility text about a keyboard-only user unable to reveal a hidden Bar is moot until it is built.
- **Bar keys the vault specifies and the code lists as "Not built":** `Visible`, `Input_Region`, `Meld`, `Padding`, `Class`, `Attach_To`, `Animation`, `Exclusive_Zone`, `Text_Rotation` (`tess-shell:src/tess_shell/schema/docs.py` lines 188 to 275). Frame: `Children`, `Meld`, `Exclusive_Zone`, `Input_Region`, `Class`, `Elevation`, `Shadows`, `Shadow_Bleed` (lines 329 to 340); Frame shadows are the design's main stated advantage ("no oversize surface needed", `shell-vault:40 Specifications/Surfaces/Frame.md` Shadows) and are not built. Panel: `Margin`, `Padding`, `Class`, `Exclusive_Zone` (lines 297 to 300), although the vault Panel spec lists `Margin` and `Padding` as core and Frame Melding uses a Panel `Margin` to stop a meld. Popup: `Animation`, `Attach_To` (lines 319 and 320) although Popup reduced motion text says "fade is off".
- **Grid is a v1 block in the vault but absent in code.** R11 lists Grid in the v1 block set (`shell-vault:41 TDL Reference/Block Reference.md` Decisions of 2026-11-01); V1 Widgets says "Grid, Terminal and Canvas are blocks with no v1 use yet". No Grid, Square, Ellipse, Triangle, Hexagon, Terminal, Canvas or VirtualList in `tess-shell:src/tess_shell/schema/blocks.py` or any binder file. Square, Ellipse, Triangle and Hexagon are decided in `shell-vault:50 Design System/Building Blocks.md` but have no row in code and no v1 consumer.
- **Elevation: the vault dropped `Reach`, code keeps it, and the shadow strength differs.** Style Schema D35 "Reach is dropped from Elevation" (`shell-vault:41 TDL Reference/Style Schema.md` line 123); `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` still sets `Reach: 64`. D33 in `shell-vault:00 Home/M3 Build Log.md` records the shipped shadow as "25 % black"; the file has `#00000066` (40 percent). The Style Schema example uses `#00000040` (25 percent), so the vault is internally consistent and the code is the outlier.
- **Fallback icon name differs between vault and code, and inside the vault.** Standard Modules Icon says a missing icon shows `image-missing`; the run-time paragraph of Block Reference says `image-broken-variant`; code uses `mdi:image-broken-variant` (`tess-shell:src/tess_shell/model/icons.py` line 19). `image-missing` is a freedesktop name and is not in the mdi set the shell ships.
- **Contrast acceptance is unmet.** Accessibility rule 9 (4.5 to 1 text, 3 to 1 for large text, icons and widget edges) requires "a script over the shipped themes" in M4 and the acceptance box is unchecked (`shell-vault:60 Quality/Accessibility.md`). No such script exists in `tess-shell:tools` or `tess-shell:tests` (the only luminance code is in the sRGB edge-blend repro tests). The shipped Light theme in particular has not been shown to pass (for example `On_Surface_Muted #4A5967` on `Surface #F4F7FA`, `Outline #7A8896` edges).
- **Disabled and state looks are code-chosen, not specified.** The vault says only "more than colour" (Accessibility rule 8). The Default stylesheet sets disabled `Opacity: 0.5`, hover `0.85`, press `0.7` and 2 px borders (`tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl`). No vault page gives these values, and 0.5 opacity on text is likely below 4.5 to 1 contrast.
- **Focus ring colour and width are unspecified in the vault.** Vault: "non-blurred shadow with spread so it does not shift layout" (`shell-vault:41 TDL Reference/Block Reference.md` Accessibility Defaults; `shell-vault:40 Specifications/Integration/Focus and Keyboard.md`). Code fixes it to `color.primary`, `space.step_1` (2 px) (`tess-shell:src/tess_shell/model/look.py` lines 139 to 156). The ring's contrast against surface is therefore unchecked (3 to 1 rule 9). A Text or Bitmap that takes focus (`Selectable`) has no ring (`tess-shell:src/tess_shell/binder/focus.py`); the vault resolved this by making selectable text no Tab stop (2026-11-16).
- **Default stylesheet applies only Body.** Vault defines five type roles; the Default stylesheet uses only `type.body.font_size` for `Text` (`tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl`). No standard module or class uses Caption, Label, Title or Display, so the scale is mostly unused.
- **Button has one look.** The vault defines Button states but no variants; code ships a single bordered surface-raised button. An icon-only button, a text button, a toggle button and a filled or tonal emphasis button are all absent as named variants.
- **Hand checks outstanding against the vault claim "built":** Orca (screen reader) announcements untested (`shell-vault:60 Quality/Accessibility.md`); high contrast and reduced motion tested headless only; Volume OSD real-KWin placement and layer unchecked (`shell-vault:40 Specifications/Modules/Volume OSD Module.md` Questions After Testing); Panel content-size resize not seen on KWin (`shell-vault:40 Specifications/Surfaces/Panel.md` As Built in PR 116); input method on a real compositor never tested (maintainer: "not performing and do not care", `shell-vault:00 Home/M4 Build Log.md`).
- **`Elevation` percentage curve and 64 px reach are provisional.** "The 64 px comes from tests on a different renderer, so the curve and the numbers are provisional" (`shell-vault:41 TDL Reference/Style Schema.md` Shadow Keys, D88 and D90). The design system note that should own the values (`50 Design System`) never took them over.

### Contradictions and stale text inside the vault

- **Tooltip as a module.** V1 Widgets and Building Blocks list Tooltip as a standard module (and the Standard Modules summary lists it); Standard Modules later says "there is no separate Tooltip module file. A tooltip is the `Tooltip` key" (2026-11-13). Code has no Tooltip module directory (`tess-shell:src/tess_shell/shipped`). The element should be treated as a key and a Popup mode, not a module.
- **TextEditor wrap.** Standard Modules says `Wrap: WORD` is accepted with one warning and no effect until TRE-REQ-016; V1 Widgets (Questions After Testing 2) says tre 0.6.6 supports it and the maintainer's KWin check passed; the code has working `Wrap` (`tess-shell:src/tess_shell/shipped/TextEditor/TextEditor_Module.tdl` lines 8, 28, 40).
- **TextInput `Read_Only`, `Max_Length`, `Password`.** Block Reference TextField says "the shell does not offer them as keys yet"; Standard Modules (decided 2026-11-10) offers them; code ships `Password` (grep of `TextInput_Module.tdl`).
- **`Visible: false` on a Bar and Panel hidden state.** Panel spec D44 amended twice (no-window route, then kept surface); the tre fault explaining it (a property set in one window during another window's callback) is a wake workaround, not a design decision, and its cost (7 MiB per reload cycle, SHELL-REQ-001) is open.
- **Auto-hide delay** is "1000 ms proposed" in Bar and "open" in Performance Budgets row 9 (`shell-vault:60 Quality/Performance Budgets.md`, item listed as an inconsistency).
- **Duration tokens have values only in Performance Budgets** (100, 200, 400 ms); Style Schema names them with no values; the easing curves `standard` and `emphasized` have no definition anywhere in the vault (no cubic-bezier or spring numbers). Panel slide uses a hard-coded 24 px (D49) and 200 ms.
- **Style Schema status `review`**, while the sibling design notes are `accepted`; Building Blocks carries `needs-verification` although marked accepted; Standard Modules ends with all open boxes unchecked (gallery looks, role/state setup, 0 frames at idle, reduced motion, `Enabled: false`), even though M4 checklists passed (`shell-vault:00 Home/M4 Build Log.md`). The acceptance boxes were never ticked.
- **Frame position and layer.** Frame text first says melded Panels are drawn "on the overlay layer", then that melds are hosted in the painter (decided 2026-10-27); the Melding section and Failure Modes ("A Panel joined to the Frame on the same layer: the Panel uses overlay") still describe the older layer solution.
- **Handle opacity example.** The dots rest at 0.6 opacity, which the maintainer says is "more than visible", but there is no contrast target for the handle (3 to 1 rule 9 would apply to a control edge).
- **Role list.** Block Reference lists roles but says tre's page "lists more"; `PROGRESSBAR` and `GROUP` are used by Standard Modules and Volume OSD ("labelled group with a named progress bar") but not listed; flagged `needs-verification` in the vault and never closed.

### Undocumented UX behaviour and missing design

- **No density system.** No compact, default or comfortable scale; no minimum target size (24 px WCAG 2.2, 44 px touch). Button, List row and tray icon sizes are set per module in TDL and by stylesheet padding (`[10, 6, 10, 6]` list item) with no vault rule.
- **No state-layer scale or ripple.** The vault uses discrete stylesheet states with fixed opacity values; it has no hover, focus, press and drag overlay percentages and no ripple. The MD3 counterpart is therefore only approximate.
- **No scrollbar design.** ScrollBox scrolls by wheel only (`Scroll_Snap`, `On_Scroll` not built); no scrollbar, scroll indicator, or overscroll behaviour is specified, and a long List or Tray menu (60 percent cap) has no visible scroll affordance.
- **No dialog, modal, snackbar, notification or toast element.** A Notification window is a reserved but unbuilt surface (`shell-vault:40 Specifications/Surfaces/Surface Types.md` Special Cases). `Role` list includes `DIALOG` but no dialog surface exists; `Scrim` token has no consumer.
- **No drag and drop.** Only pointer capture for Slider, Panel move and peek drag. The configuration app excludes a drag-and-drop canvas in v1.
- **No loading or progress pattern** except Image `Placeholder`; ProgressBar indeterminate not in v1; no skeleton or busy state for the Launcher while the application index builds.
- **Empty and error states are scattered**: module hide when a service is absent (Audio, Battery, Network), "No results" announcement in the Launcher, error image, missing icon; there is no common rule or visual for them, and "No results" has no visible text specified (announced only).
- **Validation UX.** Load errors are `file:line:column` messages with nearest names; the app shows a problems list with icon and text. No in-shell visual error indicator exists (the shell has no UI to show a config error on screen).
- **Peek keyboard way in.** Hover peek has no keyboard path until shortcut mode (M6); Show, Hide and Toggle actions are the only non-pointer path ("Tab and Enter did nothing", `shell-vault:40 Specifications/Surfaces/Frame.md` Peek on KWin).
- **Handle accessibility.** Handle "should be a focusable button named Expand dock" (`shell-vault:40 Specifications/Surfaces/Frame.md`), but the handle is part of the painter and not a target of its own; unresolved.
- **Light mode and desktop accent are unverified visually.** No vault entry shows a looked-at Light theme; only D33 notes the values. The dark theme was seen on KWin ("Themed Bar", `shell-vault:00 Home/M3 Build Log.md`).
- **Text rotation** on vertical Bars and Frame side strips is deferred (no rotated text in v1) so side-strip labels cannot exist yet.
- **Animated icons** (mli) are not shipped; the vault depends on tre drawing SMIL (TRE-REQ-008, status review) and on the maintainer's tess-icons repository; the tray and task icons from the desktop theme come through a separate lookup with no hover or animation rules.
- **Fonts.** The shell ships no font; the Default theme falls back to Roboto (tre's bundled font) and desktop `font-name` family only (no size); a "UI scale" setting is not specified, nor fractional scaling behaviour beyond a "150 percent" join test.
- **Multi-monitor look differences** (per-monitor scale, a Frame on one monitor only) are noted as behaviour, not as visual rules.

### Owner (maintainer) feedback on real behaviour found in the vault

- Popup on KWin (2026-11-06): four faults, placement off by 4 px, stops about 30 px from the edge, Escape does nothing, shadow margin takes clicks; click-through fixed after TRE-REQ-014 ("shadows have click through now and works well", 2026-11-07) (`shell-vault:40 Specifications/Surfaces/Popup.md`). Escape-to-close after the fix is not recorded.
- Frame join on KWin (2026-11-07): ranked PARAM, SMIL, STRUCTURE, SHADER, CONCAVE; "It looks good, much better"; one fault: "The border looks slightly thinner during the rounding than the straight portions" (measured 1.70 against 2.00 linear-light; TRE-REQ-015) (`shell-vault:40 Specifications/Surfaces/Frame.md`).
- Frame peek (2026-11-07): "It looks very similar" to the Fabric version; missing click to open, drag, handle icons, corner choice; all added; "Everything implemented looks good" (2026-11-08); the dots at 60 percent are "more than visible" so `Handle_Opacity` was added.
- Fabric reference: content fading in and out is "what made the Frame, peek and sliding feel polished" (basis of `Content_Fade`).
- M4 widgets on KWin (2026-11-11): all three checklists passed except the input-method row (not performed); disabled Marquee tooltip failed then passed.
- M7k Launcher on KWin (2026-11-20): FAILED, could not type into the field, clicks off the field closed it; cause open (click catcher popup grab takes the keyboard) (`shell-vault:00 Home/M7 Build Log.md`).
- Workspaces mark (M5b, 2026-11-13): did not follow a desktop change; fixed (`shell-vault:00 Home/M5 Build Log.md`).
- Input methods on layer surfaces: "not performing and do not care about this part" (2026-11-11), so composition on a real compositor is untested.
- Retained surface for a hidden Panel "looked stale or late on KWin" (2026-11-05), the cause being the cross-window wake fault (D44).
- Maintainer decisions with visual consequence: dark `Default` theme with steel blue primary (D33, 2026-11-05); handle dots, not bars (2026-11-07); Hover handle 24 by 8 px; checkbox separate from switch (2026-10-27); Expander must have (2026-10-26); shapes hit-test on painted area (2026-10-27).


## Evidence: tre and the other libraries

- No tooltip primitive: no hover delay, no timer-driven show/hide, no auto placement policy beyond layer flip. A tooltip is `show_layer(dismissible=False)` driven by the app's `pointer_enter`/`pointer_leave` and `window.after`. Delays, dismissal on Escape/scroll and focus-triggered tooltips must be specified by UX and built in tess-ui. Evidence: tre:docs/guide/layers.md (Tooltips and snackbars).
- Layers are clipped to their host window. In a `LayerWindow` (a bar) a layer is clipped to the bar surface, so tooltips or menus that must extend past the bar need a `PopupWindow` (compositor-placed, Wayland layer-shell only) or the overlay `LayerWindow` route (~210 MB base plus ~16 B per output pixel, one per output). Evidence: tre:docs/reference/layer-window.md; tre:docs/guide/menus-from-a-bar.md (What it costs, What it does not do).
- `PopupWindow` size is fixed for its life, needs an open `LayerWindow` or `PopupWindow` parent, and has no X11, GNOME, Windows or macOS fallback (`UnsupportedPlatform`). A tooltip in an ordinary application `Window` is only a `show_layer`. Evidence: tre:docs/reference/layer-window.md (PopupWindow, Errors).
- The overlay route and the popup route differ in how the outside click is handled: popup dismissal consumes the click (user clicks again); tre has no `outside_press` event by design (TRE-REQ-024). Specs for "click outside closes" must state this. Evidence: tre:docs/reference/layer-window.md (Knowing the keyboard left).
- KWin behaviour of the grab-popup dismissal trick is not verified; sway accepted it. Evidence: tre:docs/reference/layer-window.md.
- Menus: no menu node, no item model, no arrow-key or typeahead navigation, no submenu hover timing; only `role="menu"`/`menuitem`, `dismiss` and layers. All menu keyboard behaviour is framework code. Evidence: tre:docs/reference/layers.md; tre:docs/reference/node.md (role).
- No scrim: a modal layer blocks input but draws nothing; scrim colour, opacity and animation are app-defined. Evidence: tre:docs/reference/layers.md (Tesserae Engine draws no scrim).
- Focus ring: the engine draws none; it only supplies `focus_visible` on the `focus` event and a recipe (zero-blur spread shadow, which does not shift layout). A UX rule for ring colour, width (e.g. 3 px) and offset has no engine default to override. A spread shadow is clipped by `clip_children` parents and by scroll views, so a ring on a node at a scroll view edge can be cut off. [INFERENCE] from shadow painting inside clipped parents; not verified in tre docs. Evidence: tre:docs/guide/painting.md; tre:docs/guide/events-and-input.md.
- State layers (hover/focus/press/drag), ripple and disabled styling: absent by design since engine-md3 removal (0.3.5, M99). Specs must define them as framework behaviour; `pointer_enter` fires per subtree, `hit_testable=False` makes a node transparent. Evidence: tre:ARCHITECTURE.md section 7; tre:docs/guide/painting.md (What Tesserae Engine leaves to you).
- `disabled` is an accessibility flag only: it does not block focus, click or keys. A disabled widget spec must say the widget suppresses them. Evidence: tre:docs/guide/accessibility.md (Role, name, and state).
- Scroll bar limits: thumb only (4 px, 2 px margin, 32 px min length, 6 px grab slop), no track, no arrow buttons, no hover widening, no auto-hide or fade, shown whenever content overflows, fixed 2 px thumb radius. `scrollbar_width` changes thickness (painted and grabbed) and `scrollbar_fill` the colour; thumb colour default is outline_variant at 55 percent (the code comment says MD3 has no scrollbar spec, values taken from pyCopper). Maintainer feedback from the 2026-11-20 config-app demo about scrollbars is recorded in the UX vault AGENTS.md; this engine default is the likely cause of the 4 px complaint. Evidence: tre:crates/engine-core/src/node.rs:518-525; tre:crates/engine-render/src/lib.rs:1984,2010.
- Virtual list: wheel scroll and thumb only; Home/End/Page/arrow keys, `scroll_into_view`, snap and sticky do not apply to `virtual_list` per docs ("a virtual_list scrolls by wheel only"). Large trees or lists therefore need app-implemented keyboard navigation and reveal (aligns with the tree density and keyboard concerns). Evidence: tre:docs/guide/nodes-and-layout.md (Keyboard scrolling); tre:docs/guide/nodes-and-layout.md (Snapping).
- Doc drift: tre:docs/guide/nodes-and-layout.md says a `virtual_list` scrolls by wheel only, while tre:crates/engine-render/src/lib.rs (paint of "a real VirtualList's own real scrollbar thumb", M47) paints a thumb for it. Whether the virtual-list thumb can be dragged was not verified. [INFERENCE]
- No overscroll or rubber band; touch fling coasts, but wheel and trackpad inertia comes from the OS; keyboard scrolling jumps with no easing. Snap is mandatory only (no proximity). Evidence: tre:docs/guide/events-and-input.md (Touch and gestures); tre:docs/guide/nodes-and-layout.md.
- Text clipping and ellipsis: `text` supports `overflow="ellipsis"` with `max_lines`; `text_input` single-line `overflow="ellipsis"` shows the ellipsis only until focused. A multiline text without `wrap` set on `text_input` keeps a monospace-based scroll (1.35 line height, 0.6 char width assumptions) that is a few pixels off in proportional fonts. Evidence: tre:docs/guide/text.md (Long lines in a text input); tre:crates/engine-core/src/tree/mod.rs:1254,1267.
- Unsized text node is as wide as its text plus 2 px (since 0.6.2); before that it was 0 wide. A width computed from `measure_text` plus rounding up avoids wrapping. Spec for button hugging must use `measure_text`. Evidence: tre:docs/guide/text.md.
- Typography: no type scale, no variable-font axes beyond weight (1-1000, depends on face), bundled faces limited to Roboto Regular and Medium (so weights other than 400 and 500 are synthesised or nearest [INFERENCE]), Noto Sans Arabic and Hack Nerd Font Mono. No CJK, Hebrew, Indic, Thai or emoji unless `set_system_fonts(True)` (machine-dependent output) or registered fonts. No LCD text (declined). `font_size` cannot animate. Evidence: tre:crates/engine-render/src/text.rs:32-50; tre:docs/guide/text.md; tre:docs/design/gaps.md (7).
- Icon facility: engine only draws paths and SVG documents (24x24 viewBox via `view_box`); no icon font, no named icon lookup, no tinting API (`currentColor` in tess-icons bodies must be mapped by the consumer), no size tokens. The set in tess-icons is Pictogrammers Material Design Icons (7447, Apache-2.0) plus Line MD (1218, MIT), not Google Material Symbols, so Material Symbols variants (weight, fill, grade, optical size) do not exist in the stack. SVG node drops all filters except one blur or drop shadow, so complex SVG icons may render differently. Evidence: tess-icons:icon-sets/Material-Design-Icons/material-design-icons.json; tre:docs/reference/paint.md (SVG documents).
- Accessibility bridge: AccessKit tree is built every frame; AT-SPI on Linux verified against AccessKit's own consumer and a private-bus test; never tried with Orca, NVDA or VoiceOver. Layer surfaces and popups publish their own adapter but under Wayland the reader gets no screen position for a layer surface (magnifier and touch exploration cannot locate it). Text runs assume left-to-right. Evidence: tre:docs/guide/accessibility.md (Text, selection and links, Announcing); tre:docs/reference/layer-window.md (Accessibility).
- `window.announce` requires a connected screen reader to be audible; messages are queued (16, newest kept), one per accessibility update, about 100 ms for six messages at 60 Hz. Evidence: tre:docs/guide/accessibility.md.
- Active descendant (TRE-REQ-023) is unreleased in the docs; on Linux it moves the AT-SPI focused state to the row (no `ActiveDescendantChanged`). Specs for comboboxes and search-and-list patterns should add the polite `announce` fallback. Evidence: tre:docs/guide/accessibility.md (Active descendant).
- Reduced motion and increased contrast are signals only; only the Linux read is checked on real hardware, Windows and macOS announce no change until the window regains focus. The UX spec must make the framework shorten durations and swap palettes. Evidence: tre:docs/reference/events.md (Window properties).
- Colour: 8-bit sRGB only, no HDR or wide gamut (declined until vello_gpu supports it); `tess_utils.parse_color` clips wide-gamut input into sRGB. Evidence: tre:docs/design/gaps.md (8); tess-utils:docs/reference.md (Colour).
- Elevation: engine offers a shadow list only; MD3 tonal elevation (surface tint) has no engine support. Shadows inside a popup need a transparent margin (`geometry`) and `input_region="geometry"` so margin clicks pass through. Evidence: tre:docs/reference/layer-window.md (PopupWindow); tre:ARCHITECTURE.md section 7.
- Motion: layout animations re-run layout each frame (cost grows with tree size); `to` must be a pixel number (no auto or percentage targets); interrupted spring retarget carries velocity only for numeric properties (not colours or shadows); `font_size` is not animatable. No duration or easing tokens exist in the engine. Evidence: tre:docs/guide/animation.md.
- Density and touch targets: engine has no density concept; `touch_target_slop` defaults to 0 and touch handling is tested with simulated touches only. Evidence: tre:docs/guide/events-and-input.md.
- Drag and drop: OS file drop is unavailable on Wayland (winit 0.30), has no drag-source support, and on X11 the position can be missing; docking draws no handle or highlight; in-app drag is manual pointer capture. Evidence: tre:docs/guide/events-and-input.md (Files dragged from the OS); tre:docs/guide/docking.md.
- Window features unavailable or partial per platform: window icon only on Windows and X11; `blur_behind` only Wayland (KDE blur protocol) and macOS; `always_on_top` hint ignored by some WMs; layer windows need Wayland layer-shell. Evidence: tre:docs/reference/window.md; tre:docs/design/gaps.md (2).
- Pointer: middle button and mouse side buttons deliver `pointer_down` only (no click); no long-press-to-context-menu on mouse; no hover timing primitive. Evidence: tre:docs/guide/events-and-input.md (Pointer).
- Text input: `input_mode` is stored but unused on desktop; `read_only` still submits on Enter; multiline Tab inserts a tab unless `tab_navigates=True`, which is a keyboard-trap risk for forms. No built-in field background, label or error visual, so text field variants (filled, outlined, floating label) are entirely framework. Evidence: tre:docs/guide/text.md (Text input).
- Empty, loading and error states have no engine support beyond `busy`, `invalid`, `description` and `live` flags. Evidence: tre:docs/reference/node.md.
- Terminal default palette is a dark-style ANSI set with a dark foreground and transparent background, which only reads on light backgrounds; strikethrough is not rendered (vt100 limit). Evidence: tre:crates/engine-core/src/node.rs (TerminalPalette::default).
- Caret blink: `caret_blink` is optional; the Rust state initialises `caret_blink_ms` to 0 and no default blink period was found. Verify before specifying a blink rate. [INFERENCE] Evidence: tre:crates/engine-core/src/node.rs:705,923.
- Default text input font size differs between the creation code (16) and engine-core test constructors and docs (14). Spec should state explicit sizes. Evidence: tre:crates/engine-py/src/window_events.rs:314; tre:crates/engine-core/src/node.rs:1917.
- Docs version note: PLAN says main is at 0.6.7 while some references mention 0.6.10 (`window.announce` 0.6.9, `connection_lost` 0.6.10); plan header lags the feature docs. Evidence: tre:PLAN.md (Where we are); tre:docs/guide/accessibility.md.
- tess-dl and tess-el carry no visual or style schema: TDL is structure-only ("it does not know what a bar, a monitor or a colour is"); keys, units, colours and slots belong to the consumer schema (tess-shell `tesserae-shell schema`, tess-ui). A bare `#fff` colour is an error (`tdl-bare-hash`); colours must be quoted. Evidence: tess-dl:docs/language.md; tess-el:docs/language.md.
- tess-utils colour parse covers CSS Color 4 forms, matching tre bytes, but nothing defines Tesserae colour roles or theme tokens; role tokens live in tess-ui and the shell vault. Evidence: tess-utils:docs/reference.md.
- Owner feedback on real behaviour: none stated in tre sources. The UX vault AGENTS.md cites the 2026-11-20 config-app demo (tooltips, tree density, scrollbars, dark theme); engine constraints relevant to it are the tooltip, virtual list keyboard, 4 px scroll thumb and absent dark/density items above.


Back to [[90 Research]].
