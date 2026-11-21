---
title: MD3 Verification Status
type: research
status: research
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [research, needs-verification]
related: ["[[Open Questions]]", "[[Existing Tokens]]"]
depends_on: []
---

# MD3 Verification Status

How Material Design 3 values were checked in Phase 1 (closes OQ-12 for the slice notes, with the exceptions below).

> [!info] Method
> The official pages at m3.material.io are rendered by script and return no text to the tools used. Values were verified against the Material Web token sources (`tokens/versions/latest` and `v0_192`), the Material Components Android guides, Compose Material 3, WCAG 2.2 and the WAI-ARIA Authoring Practices; each note lists its sources. Where the only source is the m3.material.io page, the claim stays `#needs-verification`.

## Verified (examples)

- State layers: hover 8, focus 10, pressed 10, dragged 16 percent in the latest token set. The older set `v0_192` has focus and pressed at 12 percent; ADR-0009 and [[ADR-0013 Focus and pressed state layer 10 percent]] follow the latest.
- Focus ring 3 px, 2 px offset, `secondary`; ripple timings 450, 105, 225, 375 ms and hover fade 15 ms.
- Scrim opacity 0.32; dialog width 280 to 560 dp; menu item height 48 dp; switch 52 by 32 dp; button height 40 dp; elevation shadows equal tess-ui's formulas (this corrects the Phase 0 remark in [[Existing Tokens]] that called them a legacy formula).
- WCAG 2.5.8 (24 by 24 CSS px) and window size classes (600, 840, 1200, 1600 wide).

## Still unverified

| Note | Claim | Why |
|---|---|---|
| Spacing and Density | MD3 specification page gives 56 dp for a one-line list item | m3.material.io is a JavaScript app, no text returned; Material Web menu item token (48) used instead |
| Spacing and Density | MD3 states a 4 dp spacing grid | m3.material.io page unreadable by tools |
| State Layers | State precedence dragged > pressed > focused > hovered is MD3 guidance | Tesserae rule; m3.material.io unreadable |
| State Layers | Reduced motion hides the ripple as MD3 guidance | only Material Web forced-colors rule seen |
| State Layers | WCAG 1.4.3 exempts inactive components | recalled, page not opened |
| Focus Ring | text-input pointer focus indicator follows :focus-visible heuristic of Material Web | Tesserae rule; focus-ring.ts heuristic not inspected |
| Focus Ring | baseline secondary and surface hex values (contrast about 6:1 light, 10.9:1 dark) | hex from memory, only a computed example |
| Focus Ring | WCAG 2.4.11 wording | title seen, text not quoted |
| Iconography | MDI keeps 2 units padding in the 24 grid live area | Pictogrammers docs page not readable |
| Iconography | status bar inline icon 16 dp has an MD3 counterpart | no MD3 value found |
| Iconography | MDI licence: Apache 2.0 (shell vault) vs Pictogrammers Free License (LICENSE file) | sources disagree |
| 07 Spacing and Density Rules | page margins compact 16 / medium 24 dp follow MD3 layout guidance | m3 layout pages unreadable |
| 10 Layout Overflow and Scrolling | MD3 canonical layouts (list-detail, supporting pane, feed) and pane counts per class | m3 pages unreadable; widths 320 and 840 are Tesserae design choices |
| 10 Layout Overflow and Scrolling | scroll chaining delay 200 ms | Tesserae design choice, no source |
| Colour Roles | Numeric contrast-level values (0.5 medium, 1.0 high) and mapping of the OS contrast preference to medium | m3.material.io not readable by the fetch tool; medium/high hex taken from Material Web latest token files |
| Colour Roles | shell `accent` maps to the seed colour then `primary` | design choice, no MD3 role for a desktop accent |
| Theme Following the System | 200 ms re-theme budget | design choice (equals short4); no MD3 or platform source |
| Theme Following the System | pending surface colour #141218 when a frame must be shown before the scheme is known | design choice |
| Theme Following the System | mapping of OS contrast preference to the medium level | no source; only high is used by the projects |
| Elevation | surface container role for levels 4 and 5 (surface_container_highest) | no component token file read uses level 4 or 5; design choice |
| Elevation | Popup at level 2 with surface_container | MD3 has no popup; menu value reused, design choice |
| Elevation | official m3.material.io level-to-container table | page is script-rendered; levels 1 to 3 verified through Material Web component token files |
| Shape | Popup container radius extra_small | design choice; MD3 has no popup |
| Shape | navigation rail indicator radius (tess-ui 16 vs MD3 pill) | m3.material.io not readable |
| Motion | Popup and menu open/close durations (200 ms emphasized_decelerate / 100 ms emphasized_accelerate) | design choice; no MD3 source read |
| Motion | Conversion of MD3 spring damping/stiffness to tre bounce parameter | no documented mapping |
| Typography | Bold 700 face for the prominent label weight is not bundled in tre (Roboto Regular and Medium only) | tre docs read; Roboto variable font availability unchecked |
| Scrim | official m3.material.io scrim opacity page | not readable; 0.32 verified in Material Web md-comp-scrim token (contract marked 0.32 as unverified, now verified there) |
| Text Field | MD3 text field container height 56 dp and the label stack | m3.material.io is script-rendered and not fetchable; Material Web demo min-height 56 px is the only corroboration |
| Text Field | caret blink 530 ms on and off | MD3 gives no value; 530 ms is tess-ui Caret_Blink default; design choice |
| Text Field | multi-line default 3 lines and resize snapping | design choice, no MD3 value |
| Text Field | scale factor 1.25 and 2.0 geometry tests in tess-ui | not confirmed that the test window supports a scale factor |
| State Layers (cited in Text Field, Button, Icon Button, Switch) | focus 10 and pressed 10 percent | Material Web tokens v0_192 md-sys-state give focus 0.12 and pressed 0.12 (hover 0.08, dragged 0.16); contract says 10; conflict, needs the State Layers note and ADR-0009 sources |
| Switch | density scaling of the track at dense (46 by 28, handles 14, 21, 24) and 32 dp state layer at compact | design choice, MD3 gives one size |
| Icon Button | Expressive sizes xs to xl (32, 40, 56, 96, 136) and width kinds are Expressive | Expressive spec pages not fetched |
| Button | Expressive sizes, square shape, pressed squaring | Expressive spec pages not fetched |
| Button | paddings at compact and dense (16, 12 dp; icon 16 dp at dense) | design choice, MD3 gives 24 dp and 18 dp icon only |
| Button | reduced-motion behaviour of the loading spinner | design choice |
| 14 Accessibility Basics | WCAG 1.4.13 hoverable condition versus the tooltip rule | closed by [[ADR-0011 Tooltip hover grace for all tooltips]]: all tooltips get the 150 ms grace |
| 14 Accessibility Basics | high-contrast scheme thresholds 7 to 1 text and 4.5 to 1 non-text | Tesserae design choice, no MD3 value |
| 14 Accessibility Basics | scrollbar thumb rest alpha 38 percent may fail 3 to 1 contrast | needs contrast computation once Colour Roles values exist |
| Test Method | WCAG contrast ratio definition anchor and Accessibility Rules SC 1.1.1, 1.3.1, 3.3.1 | anchors not separately fetched |
| Scrollbar and Scroll Container | MD3 has no scrollbar component or guidance (checked only Material Web repo and engine comment) | m3.material.io is a JS app, not readable |
| Scrollbar and Scroll Container | thumb 8 dp, hit 12 dp, margin 2, min length 32, opacities 0.38/0.60/0.80, gutter 12 dp are Tesserae design choices | no MD3 values exist; contract marks them design choice |
| Scrollbar and Scroll Container | rest opacity 0.38 fails WCAG 1.4.11 3:1 (computed 2.57 dark, 1.94 light, baseline on_surface_variant over surface) | computed in the note, no shipped contrast script yet |
| Scrollbar and Scroll Container | 12 dp hit thickness vs WCAG 2.2 SC 2.5.8 24 dp: whether Spacing/Equivalent exception covers a scrollbar thumb | judgement, not confirmed |
| Scrollbar and Scroll Container | wheel notch 40 dp, track-click repeat 400/100 ms, gutter reserved by the framework | design choices; engine moves 20 dp per notch |
| Scrollbar and Scroll Container | whether to expose a scrollbar role with value to AT | tre/AccessKit support not verified |
| Tree Node | label type body_large at default and body_medium at compact/dense; icon 24/20/20; inset focus ring in rows | design choices derived from the density table |
| Tree | selection does not follow focus; Page keys; empty-state default text | design choices, APG leaves selection model to authors |
| List Item | two-line 60/48/40 and three-line 80/64/56 dp, avatar 40/32/24, image 56/48/40; formula sum of line heights + padding 16/12/4 | contract fixes only single-line heights |
| List Item | selected container secondary_container; vertical alignment of leading/trailing in three-line items | MD3 list tokens define no selected container; m3 page not read |
| List Item | MD3 disabled label opacity 0.30 vs Tesserae 0.38 | Material Web token read, m3 page not read |
| List | m3.material.io Lists guidance on selection, dividers, grouping | JS app not readable |
| Accordion | header 40/32/24, padding, content padding, title types; open 250 ms emphasized-decelerate, close 200 ms standard-accelerate; error dot | MD3 has no accordion, design choices |
| Form Row | label column width 160/120/96 dp, row gap 8/4/2, stacked layout below 400 dp, click on label focuses control | MD3 has no form row, design choices |
| Form Row | MD3 guidance on forms | m3.material.io not readable |
| Tooltip | Plain tooltip min height 24 dp, min width 40 dp, padding 8 by 4 dp, max width 200 dp; rich max width 320 dp, horizontal padding 16 dp, action min height 36 dp, gap to anchor 4 dp | Verified only in the Compose Material 3 source (Tooltip.kt); m3.material.io specs page is script-rendered and unreadable |
| Tooltip | Rich tooltip vertical metrics (28 dp to subhead, 24 dp subhead to text, 16 dp below text, 8 dp below actions) | Compose constants only, not the MD3 spec page |
| Tooltip | Hover delay 500 ms | MD3 sources read give no desktop hover delay (Flutter wait 0 ms, Compose long press); 500 ms is the accepted Tesserae rule (ADR-0004), so a design choice not an MD3 value |
| Tooltip | Touch long press shows the tooltip and it auto-dismisses at 1500 ms | 1500 ms is the Compose and Flutter non-persistent duration; official MD3 duration unreadable |
| Tooltip | Enter and exit animation bound of 100 ms (short2) | design choice, MD3 gives no tooltip duration in sources read |
| Popup | Fade of 100 ms and instant under reduced motion for popups | design choice, no MD3 duration read |
| Menu | Menu maximum width 280 dp | tess-ui bound; 112 dp minimum is verified in Material Web menu.scss, the 280 dp maximum is not |
| Menu | Container vertical padding 8 dp default, 4 dp compact and dense | MD3 token not read; the 4 dp values are a design choice |
| Menu | Typeahead prefix buffer 500 ms | design choice; Material Web default is 200 ms |
| Menu | Submenu hover open 250 ms and close 300 ms | shell vault values (built); Material Web uses 400 ms and 400 ms; no MD3 spec value read |
| Menu | Item horizontal padding 12 dp as an MD3 value | density table is the binding ADR-0002 set; MD3 menu item leading and trailing space not read |
| Menu | Open animation of short3 to short4 and 3 dp outline on forced colours | design choices, no MD3 value read |
| Dialog | Default width 312 dp | tess-ui default; MD3 spec page unreadable (min 280 and max 560 are verified in Material Web dialog scss) |
| Dialog | Full-screen form when the window is narrower than 328 dp | design choice derived from min width 280 plus 48 dp inset |
| Dialog | Action order dismissive then confirming, stacked order | from Material Web sample markup and Compose practice, spec page unreadable; stacked-action order not asserted |
| Dialog | Content beneath a modal dialog is hidden from the accessibility tree | not verified in tre or tess-ui |
| Dialog | A second dialog is refused while one is open | follows the Scrim note rule 7; MD3 guidance on stacked dialogs not read |
| Dialog | Dialog motion durations (500 ms open, 150 ms close, scrim 500 and 150) | Material Web implementation, not an MD3 spec value |
| Panel and Surface | Mapping of uses to container roles (window surface, pane surface_container_low, card surface_container) | MD3 defines the roles but a fixed mapping of uses was not read; follows tess-ui config app |
| Panel and Surface | Pane padding 12 dp default, 8 dp compact, 4 dp dense | design choice, not in the ADR-0002 binding numbers |
| Panel and Surface | Scheme change repaint with 300 ms animation | design choice |
| 12 Overlays | Z-order ranks (content, sheets, snackbar, popup, modal, tooltip) | Tesserae design choice, not an MD3 or tre rule (tre stacks by order of opening) |
| 12 Overlays | Window focus loss closes tooltips and non-modal popups but not dialogs | design choice, aligned with xdg_popup explicit grab semantics for popups |
| 12 Overlays | Opening a popup hides tooltips, opening a modal closes popups | design choice, derived from shell behaviour (a tooltip never opens over a focused popup) |

## Phase 2 unverified items

139 items collected while writing the Phase 2 notes. Most are Tesserae design choices with no MD3 source (compact and dense sizes, timings, chords) or MD3 pages that tools cannot read. Each is also tagged `#needs-verification` in its note.

| Note | Claim | Why |
|---|---|---|
| File Dialog | the 200 ms threshold for a loading indicator and Ctrl+L, Ctrl+D shortcuts | desktop conventions, no cited standard |
| Bar | MD3 top app bar small container height (the token md.comp.top-app-bar.small.container.height) | not resolved: m3.material.io unreadable, Android dimens reference m3_comp_app_bar_small_container_height without the value in the files read |
| Bar | proposed Bar thickness 48 / 40 / 36 dp at default / compact / dense (control height plus 8 dp) | Tesserae design choice, no MD3 or ADR source; shipped examples use 32 |
| Bar | order of two reserving zones on one edge with a Plasma panel on KWin | shell-vault Bar.md marks it needs-verification; no test |
| Frame | reserver 1 px and ring edge at fractional scale 1.5 | shell-vault Frame.md open question, not measured |
| Frame | threshold 95 percent for summed linear-light border brightness on a join curve against a straight | Tesserae proposal; the shell measured 1.70 against 2.00 (85 percent) only |
| Launcher | MD3 docked search view dimensions | Material Components Android Search.md gives no numeric height for a docked view; m3.material.io unreadable |
| Volume OSD | MD3 snackbar display durations in ms | Snackbar.md of Material Components Android names presets without numbers; 1500 ms is the shell value, not an MD3 value |
| Peek | handle contrast at Handle_Opacity below 0.5 | computed for the shell fallback colours on the Default theme fills only; a handle that takes the Frame border colour depends on the project's colours |
| Auto Hide | hover strip thickness and default delay 1000 ms | shell-vault Bar.md: delay proposed, thickness open, feature not built |
| Colour Picker | APG has no two-dimensional slider; the square follows code as one slider with two value texts | APG slider pages describe one value |
| Colour Picker | ratio truncated not rounded; AAA 7:1 (SC 1.4.6) | not stated on the Understanding page read |
| 03 Typography and Text Rules | role per element class for text field label, list/menu/tree item, section header, dialog title, card title | MD3 component token files for menu-item/list-item/text-field typography not re-read; m3.material.io unreadable |
| 04 Shape Rules | chip and text field container shapes | component token files not read |
| 05 Elevation Rules | tone for window regions at level 0 as a desktop rule | no MD3 page read on desktop regions |
| 06 Motion Rules | tooltip fade short2 and accordion duration | design choices, no MD3 token read |
| 08 Iconography Rules | 8 dp gap between button icon and label; WCAG 1.1.1 page | not read from token file; WCAG page not opened |
| 09 State Feedback Rules | warning state has no MD3 role; disabled-reason tooltip keyboard route; WCAG 1.4.1 and 1.4.3 text | not verified |
| Floating Action Button | lowered variant hover/pressed elevations; compact/dense FAB sizes and margins; disabled FAB look; narrow-region fallback; FAB menu | design choices or not read from tokens |
| Extended Floating Action Button | icon-label gap 8 dp; collapse motion medium2 300 ms; compact/dense heights and paddings | Material Web gap not found; m3.material.io unreadable |
| Split Button | trailing button width per size; inner corner 4 dp vs Android default; toggle form look; motion durations | Android docs give no value; m3.material.io unreadable |
| Button Group | standard gap 8 vs Android 12 dp; connected inner corner 4 (tess-ui) vs 8 (Android); pressed widening number in the spec; selected-change motion | sources disagree or unreachable |
| Segmented Button | segment padding; two to five segments rule; label-only check width reservation; Home/End keys; default selection; selection motion | not in Material Web tokens; m3.material.io unreadable |
| Token Button | row/swatch/padding per density; 100 ms open time; reduced motion; open-state layer; match count announcement | Tesserae-specific design choices |
| Font List | APG combobox pattern for search field plus owned list | not re-read |
| Choice Picker | Alt+Down opens the select button; Material Web select type-ahead 200 ms | convention, property documented only |
| List Editor | Alt+arrow reorder and Delete remove | convention, not an APG pattern |
| Icon Picker | dense 20 dp glyph in 32 dp cell | derived from icon button values |
| 11 Interaction | F6 and Shift+F6 as a cross-platform pane-cycling key | source is the config app README only; no platform or APG source fetched |
| 11 Interaction | Ctrl on Linux and Windows is Cmd on macOS | design choice, tess-ui macOS key mapping not read |
| 11 Interaction | double-click slop 4 dp, drag threshold 4 dp, touch_target_slop 10 px for touch UI, cursor shape table, shortcut vocabulary, Ctrl+A in multiple choice | Tesserae design choices, MD3 specifies none |
| 11 Interaction | platform double-click interval replacing 400 ms | tre does not expose it in the docs read |
| 15 Writing | Material Design 3 uses sentence case in component text | m3.material.io unreadable; Material Web demos not checked |
| 15 Writing | uppercase strings may be spelled by a screen reader | not verified with a reader |
| 15 Writing | length limits (tooltip 60, placeholder 40, helper 80, empty state 140, status 40), 30 percent growth rule, en dash for ranges | Tesserae design choices, not in the ux-writing skill |
| Card | selected-card styling (secondary_container, outlined border outline) matches MD3 | Material Web card tokens have no selected state; MD3 spec page unreadable |
| Card | headline, subhead and supporting text type roles (title_large, title_small, body_medium) | tess-ui values; Material Web card tokens carry no text roles; MD3 spec page unreadable |
| Carousel | item gap 8 dp and small item width 40 to 56 dp | MD3 carousel spec page is a script-rendered app; Android guide gives no values |
| Carousel | list role mapping and absence of role description property in tre | APG uses group with roledescription; tre has no such property |
| Side Sheet | maximum width 400 dp and default 360 dp, compact and medium behaviour | tess-ui values; MD3 spec page unreadable |
| Side Sheet | slide-in durations 400 ms in and 200 ms out | no published MD3 token for sheet slide; Tesserae choice |
| Side Sheet | engine accessibility tree hides content beneath a modal layer | not verified in tre |
| Spin Box | compact and dense field width 56 dp, accelerating hold rates (80 to 40 to 20 ms), Page Up and Page Down 10 steps, full-width digit handling | Tesserae design choices, no MD3 source; MD3 has no spin box |
| Time Input | MD3 time input field 96 by 72 dp, numeral display_medium, period selector shape | m3.material.io unreadable; values from tess-ui |
| Time Input | inline field widths 48/40/40 dp, Page Up/Down 10 minutes and 3 hours, auto-advance, A and P keys | Tesserae design choices |
| Search | MD3 search bar 56 dp height, elevation level 3, view panel 28 dp corner | m3.material.io unreadable; Android dimens reference m3_comp_search_* tokens without numbers; values from tess-ui |
| Search | compact and dense bar heights 40 and 32 dp, minimum width 240 dp, debounce 150 and 300 ms, panel motion 200 and 150 ms | Tesserae design choices |
| Key Chord Field | compact and dense button paddings 12 and 8 dp, fixed button width while recording, Tab behaviour while recording | Tesserae design choices; Tab while recording not documented in tess-ui |
| Text | role-by-use table (control labels, titles, dialog titles) | MD3 role-to-use mapping on m3.material.io unreadable |
| Text | content language exposure and WCAG 1.4.12 text-spacing support | tre accessibility page does not document a language property or user text spacing |
| Text | selectable text reachable by keyboard through owning control, copy action | design choice |
| Link | MD3 use of primary role for links; contrast between primary and on_surface | m3.material.io unreadable; contrast to be measured by the contrast script |
| Toolbar | MD3 toolbar values (docked 64 dp, floating pill, elevation level 3, vibrant colours) | m3.material.io unreadable; no Material Web token file or Android doc page for toolbars at the tested paths; rests on tess-ui docs |
| Top App Bar | contextual action mode and frosted variant have no verified MD3 source | m3.material.io unreadable |
| Top App Bar | frosted container text contrast measured against backdrop | design rule, no standard value |
| Status Bar | MD3 has no status bar | m3.material.io component list unreadable; rests on tess-ui docs statement |
| Status Bar | roving group threshold of five pressable items; one announcement per second coalescing; reduced-motion form of indeterminate progress | design choices, no source |
| Pagination | MD3 has no pagination; nearest patterns carousel indicator and buttons | m3.material.io unreadable |
| Pagination | outline_variant dots expected below 3 to 1 against surface | contrast not computed from the palette |
| Tabs | 100 ms threshold for manual activation | Tesserae choice; APG says only "noticeable latency" |
| Tabs | panel name by labelledby not exposed in tre docs | tre node docs list only describedby and controls |
| Navigation Drawer | pill padding start 16 and end 24, section heading spacing, slide durations | MD3 spec page unreadable; tess-ui values |
| Navigation Drawer | engine accessibility tree hides content beneath a modal layer | not verified in tre |
| Navigation Drawer | Scrim foundation says Android drawer scrim 60 percent; Material Web drawer token is 0.4 with colour neutral-variant20 | conflict between Scrim note and drawer token, owner to confirm one value 0.32 |
| Empty States | m3.material.io guidance on empty states | page unreadable by tools; MD3 has no empty-state component in Material Web or Android docs |
| Loading States | 200 ms show delay, 400 ms minimum display, 10 s and 30 s timeouts, skeleton rule, inline and region indicator sizes | design choices, no source |
| Error States | snackbar with action stays at least 10 s; 2 s repeat guard | design choices, no source |
| Validation | commit-time validation, 300 ms async idle, one-line error reserve, 16 dp error line | design choices, no source |
| Notifications | 4 s and 10 s snackbar durations, queue limit 5, 2 s merge; banner status in current MD3 | design choices; m3.material.io unreadable; Android Banner doc says not completed |
| Selection | Ctrl+Space and Shift+Space column and row selection in grids; start indicator bar 3 dp; 300 ms announce debounce; MD3 list selected colour | design choices; m3.material.io unreadable |
| Drag and Drop Pattern | 4 dp threshold (shared with 11 Interaction), 500 ms touch hold, 700 ms hover open, autoscroll band 24 dp and speeds, drop indicator sizes; MD3 gesture guidance | design choices; m3.material.io unreadable |
| Forms and Settings | no MD3 form or settings pattern; Cancel-first unsaved dialog | m3.material.io unreadable; design choice |
| Keyboard Navigation | F6 pane cycling as convention; trailing shortcut text token in menu item | not in APG; token not found in _md-comp-menu-item.scss |
| Navigation Rail | destination count three to seven | tess-ui documentation; MD3 spec page unreadable, Android guide gives no count |
| Navigation Rail | label colours of the expanded rail destination | Material Web horizontal item tokens carry no colours; tess-ui uses on_secondary_container |
| Navigation Rail | dot badge accessible reading | no source read |
| Badge | placement offsets (small badge 4 dp inside the host's right edge, large badge 12 dp inside and 4 dp above the top) | tess-ui values from the MD3 page; m3.material.io unreadable |
| Progress Indicator | MD3 indeterminate cycle times (1500, 1900, 1568, 666 ms) and the circular box 48 versus 40 dp | tess-ui code values; Material Web latest and Android give 40 dp; m3.material.io unreadable |
| Progress Indicator | baseline shape of linear and circular active indicators (corner-none in the linear and circular token files, corner-full in the progress-indicator file) | the two Material Web token sets disagree |
| Progress Indicator | compact and dense ring sizes 24 and 16 dp; delay-to-show 300 ms and minimum visible 500 ms; shell ProgressBar 8 dp | Tesserae design choices |
| Progress Indicator | role for a gauge (battery, volume) that is not progress | the engine role list was not read for a meter role |
| Snackbar | MD3 page statement of 4 to 10 s duration | m3.material.io unreadable; 4000 and 10000 ms verified from Compose SnackbarHost.kt (Short, Long) |
| Snackbar | max width 560 dp versus Compose 600 dp constant; long-action layout; lift above FAB | tess-ui value; MD3 page unreadable |
| Snackbar | keyboard path: last Tab stops and the chord Alt+Shift+N; focus ring role inverse_primary; moving the snackbar when it covers the focused control | Tesserae design choices, need the chapter 11 keyboard map |
| Banner | whether current MD3 retired the banner; one-at-a-time, queue by severity, Alt+Shift+B | MD3 page unreadable; Android Banner.md says not completed; Tesserae choices |
| Banner | compact and dense heights 44 and 36 dp | Tesserae design choice from button height plus padding |
| Divider | 16 dp inset values and 1 px painting at fractional scale factors | tess-ui docs quote the MD3 page; engine snapping not read |
| Image | default size in tess-ui, avatar and row sizes, 200 ms fade, 4096 px limit | Tesserae design choices; MD3 has no image component |
| SVG | shell default size from the document; non-scaling stroke; 2 MB and 10000 segment limits; whether the engine ignores script elements | not read in tre source; design choices |
| Video Player | click on picture toggles play, K F C keys, two-line captions, caption colour role | Tesserae choices following common players; no standard |
| Marquee Text | hover pause satisfies WCAG 2.2 SC 2.2.2 for a scroll longer than 5 seconds | the Understanding page lists pause, stop or hide; whether pause on hover alone is accepted was not decided from the page |
| Text Editor | height of a multi-line field from Lines: lines x line box + vertical space (112, 92, 88 dp at Lines 4) | Tesserae derivation from the Text Field density table, not an MD3 value |
| Box | MD3 layout page statement (container primitive absent) | m3.material.io is a JavaScript app; tools read nothing |
| Box | border inset mapping (shell adds border width to box space) | marked #needs-verification in shell vault Block Reference, not tested |
| FlexBox | engine defaults of align_items and justify_content | tre page does not state them |
| FlexBox | MD3 layout page | m3.material.io unreadable |
| Grid | MD3 gutters 16 or 24 dp for touch layouts | m3.material.io unreadable |
| Grid | MD3 layout grid page | m3.material.io unreadable |
| Rectangle Block | MD3 shape page | m3.material.io unreadable |
| Circle | MD3 badge sizes 6 and 16 dp | not read from Material Web tokens |
| Circle | MD3 shape page | m3.material.io unreadable |
| Ring Block | stroke centred on outline: outer size vs Diameter | not measured in the engine |
| Path Block | MD3 icons and progress pages | m3.material.io unreadable |
| Bitmap | cross-fade of changed artwork 200 ms | design choice, no source |
| Bitmap | MD3 shape page | m3.material.io unreadable |
| Terminal | palette role mapping, escape chord, cursor blink 530 ms, default size and scrollback | Tesserae design choices, engine defaults not stated |
| Node Graph | title truncation behaviour; node border contrast against viewport; MD3 has no node graph | not measured; m3 unreadable |
| Application Window | inactive opacity 0.6; floor 320 x 240; 6 dp resize border vs SC 2.5.8 equivalent exception; MD3 window size classes page | design choices; m3 unreadable |
| Layer Window | content-size feature released status (TRE-REQ-022); wlr-layer-shell protocol page | unreleased at reading; page not opened |
| Popup Window | shipped tooltip exit delay (200 ms vs 150 ms); xdg-shell page; MD3 menus page | not measured; not opened; m3 unreadable |
| Accessibility Tree | MD3 accessibility page | m3.material.io unreadable |
| Anchored Placement | tooltip and badge offsets; MD3 badges and menus pages | design choices; m3 unreadable |
| Active Descendant | wrap at list ends for launcher vs menu | design choice |
| Text Selection | role based selection colour; no MD3 selection token found | Material Web tokens read did not include one |
| Drag and Drop | 4 dp drag threshold; valid target highlight values; MD3 gestures page | design choices; m3 unreadable |
| Window | 6 dp resize border below 24 dp target minimum accepted as exception | WCAG 2.5.8 exceptions do not clearly cover an OS-frame-sized border; owner decision needed |
| Window | 12 dp touch resize border and 320 by 240 dp minimum window floor | Tesserae design choices, no MD3 or platform source |
| Window | AC-WIN-11 window accessible name equals Title | not known whether the engine tree exposes the OS window title; may need platform-side check |
| Title Bar | inactive opacity 0.6 and 3:1 contrast floor for the inactive bar | tess-ui value, no MD3 source; WCAG exempts inactive components only arguably |
| Title Bar | tooltip on a truncated title | design choice under ADR-0004 |
| Splitter | MD3 drag handle dp values (4 by 48) | Compose DragHandleSizes exists but dp values not readable from fetched pages; value is tess-ui's claim |
| Splitter | double-click collapse satisfies WCAG 2.5.7 as single-pointer alternative to drag resize | unclear whether collapse is an equivalent of resize |
| Splitter | collapse animation over medium2 and aria-controls support | design choice; engine has no controls relation |
| Dock | combined zone shrink rule, long press menu on touch, move announcement | Tesserae design choices |
| Dock Panel | compact 40 and dense 32 tab heights, 240 dp tab maximum, strip overflow, close button focus order | Tesserae design choices; Tabs note should align |
| Routed View | focus placement on screen change, screen title announcement, home fallback, default transition, unlimited history, edge swipe | Tesserae design choices; android navigation principles page gave no readable values |
| Audio Outputs | popup width 112 dp minimum and 280 dp maximum | inherited from the Menu note, itself unverified for the MD3 specification page |
| Network Module | name text maximum width 160 dp with ellipsis | Tesserae design choice, not in code or MD3 |
| Tasks Module | 100 ms fade-in of a new item | design choice, no MD3 value; none built |
| Checkbox | motion durations (mark draw 250 ms, colour 150 ms) | Material Web tokens publish no checkbox durations; values are tess-ui's |
| Chip | horizontal padding 16 dp and 8 dp beside an icon, gap 8 dp between parts | not found in Material Web chip tokens or internals; taken from tess-ui's chip stylesheet |
| Chip | Delete or Backspace removes a focused input chip | Material Web chip set defines Left, Right, Home, End only |
| Chip | suggestion chip label colour on_surface_variant (latest tokens) | v0_192 token set not compared |
| Slider | value label gap 8 dp above the handle; PageUp or PageDown 10 steps | baseline tokens give no gap; APG says larger step without a number |
| Slider | handle height of Expressive medium slider (tokens 44 dp vs tess-ui 52 dp) | m3.material.io unreadable; Material Web tokens read |
| Date Picker | MD3 modal grid row count (fixed six rows) and month change animation | m3.material.io unreadable |
| Time Picker | 24-hour dial layout (inner ring) | m3.material.io unreadable; only the 24h selector width token (114 dp) found |
| Time Picker | minute snapping on the dial (5 minutes vs 1 minute) and dial keyboard keys | no MD3 text readable; no APG time dial pattern |
| Radio Button | right-to-left arrow direction | APG does not state it |

Back to [[90 Research]].
