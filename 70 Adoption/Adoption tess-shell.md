---
title: Adoption tess-shell
type: adoption
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adoption, tess-shell, worklist]
related: ["[[70 Adoption]]", "[[Audit Template]]", "[[17 Conformance]]", "[[Open Questions]]", "[[Tooltip]]", "[[Bar]]", "[[Auto Hide]]", "[[State Layers]]", "[[Menu Item]]", "[[Clock Module]]", "[[Tray Module]]", "[[Keyboard Navigation]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
depends_on: ["[[Audit Template]]", "[[17 Conformance]]", "[[Test Method]]"]
---

# Adoption tess-shell

> [!info] Summary
> The severity-ordered worklist of what tess-shell must change to meet the specifications, built from the `Status in code` rows of every note that names tess-shell and checked against `tess-shell` at origin/main commit `42cdfb5` (committed 2026-11-20). It is not an audit: no test was run, no result below is `pass`, and the coverage counts are approximate. Two owner decisions are open: OQ-23 (state layers) and OQ-25 (Bar auto-hide against keyboard reachability).

## Method and header

| Item | Value |
|---|---|
| Project | tess-shell |
| Project commit read | `42cdfb5` on origin/main (2026-11-20) |
| Vault state | Phase 3, 2026-11-21 |
| Basis | the `Status in code` rows of the component, foundation, pattern and chapter notes; each key finding re-read in the code at the commit above |
| Dropped | findings the code no longer shows (none of the rows read was found fixed) |
| Severity | P0 blocks use; P1 breaks a rule of the specification; P2 polish |
| Not done | no test run, no screenshot, no screen reader; items marked unverified stay `not run` per [[17 Conformance]] |

Verified in code at `42cdfb5`:

| Fact | Evidence |
|---|---|
| Six literal tooltip cards (`Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`) in Audio, Battery, Clock, Media, Network and Tray_Item | `tess-shell:src/tess_shell/shipped/Audio/Audio_Module.tdl:52-58`, `Battery/Battery_Module.tdl:43-49`, `Clock/Clock_Module.tdl:26-32`, `Media/Media_Module.tdl:53-59`, `Network/Network_Module.tdl:42-48`, `Tray_Item/Tray_Item_Module.tdl:34-40` |
| Tooltips sit on `Role: GROUP` roots in Battery, Network and Media | `Battery_Module.tdl:38`, `Network_Module.tdl:37`, `Media_Module.tdl:47` |
| Tooltip exit delay default 200 ms (ADR-0011 asks 150 ms) | `tess-shell:src/tess_shell/schema/model.py:129`, `schema/shell.py:2076` |
| Bar keys `Auto_Hide`, `Auto_Hide_Delay`, `Visible`, `Animation`, `Input_Region`, `Meld`, `Padding`, `Class`, `Attach_To` documented "Not built"; `Reveal_Key` removed | `tess-shell:src/tess_shell/schema/docs.py:191-203,270-278`, `schema/blocks.py:438` |
| Frame `Children`, `Meld`, `Border_Tile` and others "Not built" | `schema/docs.py:236,339-340` |
| Tray item and spacing literals 18 and 6 | `Tray/Tray_Module.tdl:27,31`, `Tray_Item/Tray_Item_Module.tdl:16` |
| Menu item height 28, padding 10, icon 16 literals | `MenuItem/MenuItem_Module.tdl:37,40,52-53` |
| Menu item pressed fill is `primary`, hover is `outline`; no state layers | `Stylesheets/Default_Stylesheet.tdl:121-123` |
| Pressed menu item text `on_surface` on `primary` measures 2.58 to 1 in Dark (`#E4EAF1` on `#5B97C9`) and 2.89 to 1 in Light (`#16202B` on `#2F6B9A`) | `Themes/Default_Theme.tdl:15-20,72-76`; ratios computed from the hex values |
| Clock Face `Foreground: "#ffffff"` literal; against Light `surface` `#F4F7FA` it measures 1.08 to 1 | `Clock/Clock_Style.tdl:13`; ratio computed |
| `Tab_Index` is the ordering model (positive indices rank first) | `tess-shell:src/tess_shell/binder/build.py:643-657`, `binder/focus.py:71-72` |
| No `F6` anywhere in `src` | text search of origin/main `src` |
| Tasks closes a window on middle click only | `Tasks/Tasks_Module.tdl:61` |
| Audio changes volume on scroll through `On_Scroll` | `Audio/Audio_Module.tdl:50` |
| Tray has no key path to the menu | `Tray/Tray_Module.tdl`, `Tray_Item/Tray_Item_Module.tdl` (no key handler) |

## Worklist by theme

Rows are ordered by severity within each theme. Every AC id exists in the vault.

### Tooltips

Six tooltip cards repeat one literal block, and five of the six triggers are `GROUP` roots or boxes rather than the control the tooltip describes ([[Tooltip]], [[ADR-0011 Tooltip hover grace for all tooltips]]).

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-001 | P1 | Tooltip sits on the `GROUP` root of Battery and Network instead of on one control | AC-MOD-BAT-1, AC-MOD-BAT-5, AC-MOD-NET-1, AC-MOD-NET-4 | `tess-shell:src/tess_shell/shipped/Battery/Battery_Module.tdl:38-43`, `Network/Network_Module.tdl:37-42` | Move the `Tooltip` to the icon and keep the root a plain group | [[Battery Module]], [[Network Module]] |
| TSH-002 | P1 | Audio tooltip on the group root, not on the controls | AC-MOD-AUD-5, AC-MOD-AUD-6 | `tess-shell:src/tess_shell/shipped/Audio/Audio_Module.tdl:44-58` | One tooltip per control (mute button, slider) | [[Audio Module]] |
| TSH-003 | P1 | Media has a tooltip on the root and a second on the Marquee | AC-MOD-MED-5, AC-MOD-MED-6 | `tess-shell:src/tess_shell/shipped/Media/Media_Module.tdl:47-59`, `Marquee_Text/Marquee_Text_Module.tdl:32-33` | Keep only the Marquee cut-text tooltip, drop the root card | [[Media Module]] |
| TSH-004 | P1 | Six literal tooltip cards differ from the plain tooltip look | AC-TIP-13, AC-TIP-21, AC-MOD-AUD-10, AC-MOD-BAT-9, AC-MOD-CLK-5, AC-MOD-MED-10, AC-MOD-NET-8, AC-MOD-TRI-8 | the six paths listed under "Verified in code" | Replace the six blocks with one shipped tooltip card style read from tokens | [[Tooltip]] |
| TSH-005 | P1 | Tooltip exit delay 200 ms against the 150 ms grace; tooltip not hoverable | AC-TIP-4, AC-TIP-17, AC-PPW-6 | `tess-shell:src/tess_shell/schema/model.py:129`, `schema/shell.py:2076` | Default `Exit_Delay` 150 and keep the tooltip open under the pointer | [[Tooltip]], [[Popup Window]] |
| TSH-006 | P1 | Tooltip stays open on a press (decision D64); no Escape, scroll or press dismissal; hover only | AC-TIP-1 | `tess-shell:src/tess_shell/surfaces/popup.py` (`hover`, `_open_tooltip`, `_arm_exit`) | Dismiss on press, Escape and scroll; add the focus trigger | [[Tooltip]] |
| TSH-007 | P1 | Workspaces and Task Item have no tooltip on the item; Task Item has a Marquee tooltip inside | AC-MOD-WSP-4, AC-MOD-TIT-4, AC-MOD-TIT-5 | `tess-shell:src/tess_shell/shipped/Workspaces/Workspaces_Module.tdl`, `Task_Item/Task_Item_Module.tdl` | Add one tooltip on the item with the full name | [[Workspaces Module]], [[Task Item]] |
| TSH-008 | P2 | Applications rows have no tooltip for cut text | AC-MOD-APP-8 | `tess-shell:src/tess_shell/shipped/Applications/Applications_Module.tdl` | Add the cut-text tooltip on the row label | [[Applications Module]] |

### Keyboard reachability

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-010 | P0 | Open owner decision OQ-25: the specification asks for Bar `Auto_Hide` on by default with no default reveal key and a shortcut-mode reveal that is still `proposed`; a Bar that hides and has no keyboard reveal cannot be reached by keyboard. Today the Bar cannot hide at all (`Reveal_Key` removed), so nothing is broken until `Auto_Hide` is built | AC-AHD-8, AC-AHD-9, AC-AHD-10, AC-BAR-13 | `tess-shell:src/tess_shell/schema/blocks.py:438`, `schema/docs.py:192` | Owner decides the reveal path (shortcut mode reveal, or a default key) before `Auto_Hide` is built | [[Auto Hide]], [[Bar]] |
| TSH-011 | P1 | Tray has no key path to an item or its menu | AC-MOD-TRY-4, AC-MOD-TRI-4 | `tess-shell:src/tess_shell/shipped/Tray/Tray_Module.tdl`, `Tray_Item/Tray_Item_Module.tdl` | Make each item a Tab stop and open the menu on Menu, Enter and Shift+F10 | [[Tray Module]], [[Tray Item]] |
| TSH-012 | P1 | Task close is middle click only; Delete key absent | AC-MOD-TIT-3 | `tess-shell:src/tess_shell/shipped/Tasks/Tasks_Module.tdl:61` | Add Delete (and a menu item) on a focused task | [[Task Item]] |
| TSH-013 | P1 | Volume changes by scroll and secondary click with no key path | AC-MOD-AUD-4 | `tess-shell:src/tess_shell/shipped/Audio/Audio_Module.tdl:50` | Keep the slider arrow keys reachable from the module and add Menu for outputs | [[Audio Module]] |
| TSH-014 | P1 | `Tab_Index` positive ordering is the documented model; the specification forbids positive indices | AC-KBN-2 | `tess-shell:src/tess_shell/binder/build.py:643-657` | Keep document order; allow only 0 and -1 | [[Keyboard Navigation]] |
| TSH-015 | P1 | No F6 landmark cycling between surfaces | AC-KBN-3 | text search of origin/main `src` finds none | Add F6 and Shift+F6 over Bar, Panels and the focused window | [[Keyboard Navigation]] |
| TSH-016 | P1 | Text Editor takes Tab and cannot leave the field | AC-MOD-TED-4 | `tess-shell:src/tess_shell/shipped/TextEditor/TextEditor_Module.tdl` | Tab leaves; Ctrl+Tab or an explicit key inserts a tab | [[Text Editor]] |
| TSH-017 | P1 | No keyboard way to move a Movable Panel | AC-DND-5, AC-DND-1, AC-DND-2 | `tess-shell:src/tess_shell/surfaces/manager.py` (`drag_margin`) | Add arrow-key move on a focused Panel handle or a menu command | [[Drag and Drop]], [[Drag and Drop Pattern]] |
| TSH-018 | P2 | Focus ring on Workspaces not built; Orca-dependent items not run | AC-MOD-WSP-5, AC-A11Y-1 | `tess-shell:src/tess_shell/shipped/Workspaces/Workspaces_Style.tdl` | Draw the ring on the item and run the hand check | [[Workspaces Module]], [[Accessibility Tree]] |

### State feedback

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-020 | P1 | Open owner question OQ-23: ADR-0009 shell adoption is undecided. The shell has no state layers; states change `Background`, `Border_Color` or `Opacity` (Toggle and Checkbox hovered 0.85, pressed 0.7; disabled 0.5 on all widgets) | AC-STL-1, AC-STL-2, AC-STL-3, AC-STL-5, AC-C09-1, AC-C09-2, AC-C09-4 | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl:43-83,121-123` | Owner decides adopt or declare a deviation; do not fix until then | [[State Layers]], [[ADR-0009 State layer percentages]] |
| TSH-021 | P1 | Focus ring is 2 px in `primary`, no offset, and only on blocks that take `Shadows` | AC-FOC-1, AC-FOC-2 | `tess-shell:src/tess_shell/model/look.py:140-163` | Offset 2 dp ring on every focusable block | [[Focus Ring]] |
| TSH-022 | P1 | Toggle has no focus ring; hover and pressed are opacity | AC-MOD-TGL-4 | `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl`, `Stylesheets/Default_Stylesheet.tdl:57` | Follow TSH-020 and add the ring | [[Toggle]] |
| TSH-023 | P2 | Task Item minimised shows as opacity 0.5 only, the disabled look | AC-MOD-TIT-7 | `tess-shell:src/tess_shell/shipped/Task_Item/Task_Item_Style.tdl` | Use an icon or text state cue, not the disabled opacity | [[Task Item]] |
| TSH-024 | P2 | Disabled opacity is 0.5 where the specification is 0.38 | AC-LSI-08, AC-MEN-6 | `Stylesheets/Default_Stylesheet.tdl:123` | Set 0.38 | [[List Item]], [[Menu]] |

### Density and sizes

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-030 | P1 | Tray item hit area is the 18 dp icon; spacing 6 literal | AC-MOD-TRY-7, AC-MOD-TRI-2 | `tess-shell:src/tess_shell/shipped/Tray/Tray_Module.tdl:27,31`, `Tray_Item/Tray_Item_Module.tdl:16` | Hit area 40, 32 or 28 dp by density, at least 24 dp, gap 4 | [[Tray Module]], [[Tray Item]] |
| TSH-031 | P1 | Menu item row 28 dp, padding 10, icon 16 literals at default and compact; menu minimum width 160 not 112 | AC-MOD-MIT-4, AC-MOD-TRM-5, AC-MEN-1, AC-MEN-2, AC-MEN-3 | `tess-shell:src/tess_shell/shipped/MenuItem/MenuItem_Module.tdl:37,40,52-53` | Read height and icon from the density tokens | [[Menu Item]], [[Tray Menu]], [[Menu]] |
| TSH-032 | P1 | Audio and Media controls are 32 dp buttons with a 16 dp icon at every density | AC-MOD-AUD-8, AC-MOD-MED-8 | `tess-shell:src/tess_shell/shipped/Audio/Audio_Module.tdl:81`, `Media/Media_Module.tdl:78` | Size from the density tokens; icon 24 at default | [[Audio Module]], [[Media Module]] |
| TSH-033 | P1 | Task Item 24 high, padding 6, gap 6 literals; Workspaces height is text plus padding 10 | AC-MOD-TIT-6, AC-MOD-WSP-6 | `tess-shell:src/tess_shell/shipped/Task_Item/Task_Item_Module.tdl`, `Workspaces/Workspaces_Module.tdl` | Density tokens for height and padding | [[Task Item]], [[Workspaces Module]] |
| TSH-034 | P1 | No density setting; list rows 40, Button 32, Checkbox box 18, Toggle 40 by 22 are literals below 24 dp targets | AC-DEN-1, AC-LSI-01, AC-LSI-02, AC-LSI-03, AC-LSI-06, AC-MOD-TGL-4 | `Button/Button_Module.tdl:34`, `Checkbox/Checkbox_Module.tdl:31-32`, `Stylesheets/Default_Stylesheet.tdl` | Add the density token set and read sizes from it | [[Spacing and Density]], [[List Item]], [[Toggle]] |
| TSH-035 | P2 | Applications rows 40 dp, padding 10, width 456 literal | AC-MOD-APP-5, AC-MOD-APP-6, AC-LNC-13 | `tess-shell:src/tess_shell/shipped/Applications/Applications_Module.tdl` | Density tokens and a width token | [[Applications Module]], [[Launcher]] |
| TSH-036 | P2 | Badge dot is 8 by 8 and pill 18 high, 11 px; specification 6 and 16 | AC-BDG-1, AC-BDG-2 | `tess-shell:src/tess_shell/shipped/Badge/Badge_Module.tdl` | Set 6 and 16 and the badge label type role | [[Badge]] |
| TSH-037 | P2 | Default icon size 16 literal where list and menu icons are 24 | AC-ICO-1, AC-C08-1 | `tess-shell:src/tess_shell/shipped/Icon/Icon_Module.tdl`, `MenuItem/MenuItem_Module.tdl:52-53` | Take icon size from the density tokens | [[Iconography]] |
| TSH-038 | P2 | Label overflow default is `CLIP`; Network name not truncated | AC-MOD-LBL-2, AC-MOD-LBL-3 | `tess-shell:src/tess_shell/shipped/Label/Label_Module.tdl` | Default `ELLIPSIS` | [[Label]], [[Network Module]] |
| TSH-039 | P2 | Modules use pixel literals not the spacing tokens | AC-DEN-1 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:47-55` | Replace literals by `$space` tokens when TSH-034 lands | [[Spacing and Density]] |

### Contrast

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-040 | P0 | Pressed menu item text `on_surface` on `primary` measures 2.58 to 1 in Dark and 2.89 to 1 in Light; the pressed fill is also used by the tray menu | AC-MOD-MIT-5, AC-MOD-TRM-8 | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl:122`, `Themes/Default_Theme.tdl:15-20,72-76` | Use `on_primary` for the pressed text or a state layer (see TSH-020) | [[Menu Item]], [[Tray Menu]] |
| TSH-041 | P0 | Clock Face foreground is the literal `#ffffff`; on the Light `surface` `#F4F7FA` it measures 1.08 to 1 | AC-MOD-CLK-6 | `tess-shell:src/tess_shell/shipped/Clock/Clock_Style.tdl:13` | Use `$color.on_surface` | [[Clock Module]] |
| TSH-042 | P1 | No contrast script over the shipped themes exists | AC-COL-3, AC-COL-4, AC-LNC-15, AC-LNC-17 | `tess-shell:docs/design/60 Quality/Accessibility.md` (rule 9 asks for it) | Add a script that checks every role pair in the three modes | [[Colour Roles]], [[Launcher]] |
| TSH-043 | P1 | `accent` on `surface` measures 4.38 Dark and 3.82 Light and must not carry text | AC-COL-3 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:22` | Keep `accent` to non-text uses; lint text uses | [[Colour Roles]] |
| TSH-044 | P2 | Launcher hover fill `surface_raised` equals the card fill | AC-LNC-18 | `tess-shell:src/tess_shell/shipped/Applications/Applications_Style.tdl` | Use a distinguishable hover fill | [[Launcher]] |

### Surfaces not built

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-050 | P1 | `Auto_Hide`, `Auto_Hide_Delay`, `Reveal_Key` absent: a Bar cannot be hidden; blocked by OQ-25 | AC-AHD-1, AC-AHD-2, AC-AHD-3, AC-AHD-4, AC-AHD-5, AC-AHD-6, AC-AHD-7, AC-AHD-12, AC-AHD-13 | `tess-shell:src/tess_shell/schema/docs.py:191-192`, `schema/blocks.py:438` | Build on the Frame strip slide in `surfaces/frame.py` after OQ-25 | [[Auto Hide]] |
| TSH-051 | P1 | Bar `Visible`, `Input_Region`, `Exclusive_Zone` not built | AC-BAR-4, AC-BAR-17 | `tess-shell:src/tess_shell/schema/docs.py:270-273` | Build `Visible` first (needed by the actions `Show`, `Hide`, `Toggle`) | [[Bar]] |
| TSH-052 | P1 | Bar `Meld` and `Attach_To` not built; Frame `Meld` not built | AC-BAR-17, AC-FRM2-11 | `tess-shell:src/tess_shell/schema/docs.py:274-277,340` | Build the Frame `Meld` key | [[Bar]], [[Frame]] |
| TSH-053 | P1 | Bar and Popup `Animation` not built (no popup show and hide animation) | AC-BAR-17, AC-AHD-13 | `tess-shell:src/tess_shell/schema/docs.py:278,330` | Build `Animation` with the motion tokens and reduced motion | [[Bar]], [[Popup]] |
| TSH-054 | P1 | Frame `Elevation`, `Shadows`, `Shadow_Bleed` not built; one shadow list scaled by percent | AC-FRM2-11, AC-PNL-5, AC-ELV-3 | `tess-shell:src/tess_shell/binder/shadow.py`, `schema/docs.py:339-340` | Decide the level model together with OQ-23, then build the keys | [[Frame]], [[Panel and Surface]], [[Elevation]] |
| TSH-055 | P2 | Panel `Margin`, `Padding`, `Class`, `Exclusive_Zone` and Bar `Padding`, `Class`, `Text_Rotation` not built | AC-BAR-17, AC-PNL-4 | `tess-shell:src/tess_shell/schema/docs.py:203,275-276,307-310` | Build `Padding` and `Class` first | [[Panel and Surface]], [[Bar]] |
| TSH-056 | P2 | Peek handle colour is a literal; handle nodes not exposed; single trigger only | AC-PEK-14, AC-PEK-16, AC-PEK-18 | `tess-shell:src/tess_shell/surfaces/frame.py` (`_handle_colour`), `surfaces/handle.py` | Colour from a role; expose the handle as a named control | [[Peek]], [[Dock]] |
| TSH-057 | P2 | Popup Escape closed by the shell, not verified on KWin; Launcher popup grab faults on KWin | AC-POP-1, AC-POP-6, AC-POP-7 | `tess-shell:src/tess_shell/surfaces/popup.py` (`_key`) | Run the hand checks on KWin and record | [[Popup]] |

### Theming

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-060 | P1 | Reduced motion lives in code; the theme `Reduced_Motion { }` block is empty; `EMPHASIZED` easing differs from the table | AC-MOT-2, AC-MOT-5 | `tess-shell:src/tess_shell/binder/motion.py`, `Themes/Default_Theme.tdl:67-70` | Put the behaviour in the theme and correct the curve | [[Motion]] |
| TSH-061 | P1 | No persistent user override of the scheme; first-frame behaviour with a slow portal not tested | AC-TH-4, AC-TH-5, AC-TH-7 | `tess-shell:src/tess_shell/services/portal.py`, `appearance.py` | Add a settings key for the override | [[Theme Following the System]] |
| TSH-062 | P2 | Theme without `Elevation.Max` draws `#00000040`, theme value is `#00000066` | AC-ELV-3 | `tess-shell:src/tess_shell/binder/shadow.py` | Align the fallback with the theme | [[Elevation]] |
| TSH-063 | P2 | Shape scale has 5 of 7 steps; dialog and rich tooltip steps cannot be expressed | AC-SHP-2, AC-C04-1 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:38-42` | Add 12 and 28 or declare the deviation | [[Shape]] |
| TSH-064 | P2 | Hard-coded colour fallbacks and `Elevation: 20%` repeated outside the theme | AC-TIP-13 | the six tooltip files | Resolved by TSH-004 | [[Colour Roles]] |

### Accessibility roles

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-070 | P1 | Orca not installed: Launcher, announcements and `active_descendant` for the Launcher list are untested | AC-MOD-APP-1, AC-LNC-20 | `tess-shell:docs/design/60 Quality/Accessibility.md`, `docs/design/00 Home/Hand Checks.md` | Install Orca on the test machine and run the hand checks | [[Accessibility Tree]], [[Launcher]] |
| TSH-071 | P1 | Roles for tooltip carriers are `GROUP` (see TSH-001 to TSH-003); a group with a tooltip has no control to announce it | AC-MOD-BAT-1, AC-MOD-NET-1 | the three root files | Same fix as TSH-001 | [[Accessibility Tree]] |
| TSH-072 | P2 | Expander has no header and no keys of its own; the controlling Button carries `expanded`; Accordion opens in 200 ms against 250 ms | AC-ACC-09 | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl` | Document the pairing and set 250 ms | [[Accordion]], [[Expander]] |
| TSH-073 | P2 | Tray attention is colour plus border only | AC-MOD-TRI-7 | `tess-shell:src/tess_shell/shipped/Tray_Item/Tray_Item_Style.tdl` | Add a shape cue | [[Tray Item]] |

### Blocks not built

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-080 | P1 | ScrollBox has no scrollbar of either axis; `Scroll_Snap` and `On_Scroll` not built | AC-SCB-02, AC-SCB-03, AC-SCB-04, AC-SCB-05, AC-SCB-06, AC-SCB-07, AC-SCB-08, AC-SCB-09, AC-SCB-12, AC-SCB-13, AC-BLK-SBX-5, AC-LAY-7, AC-LAY-8 | `tess-shell:src/tess_shell/schema/blocks.py` (`ScrollBox`) | Wait for the engine request ([[UXREQ-001 Two-axis scroll view with the specified scrollbar]]) | [[ScrollBox]], [[Scrollbar and Scroll Container]] |
| TSH-081 | P2 | Text Selection: no copy command | AC-SEL-10 | `tess-shell:src/tess_shell/schema/blocks.py` (`Selectable`) | Add Ctrl+C on a selectable Text | [[Text Selection]] |
| TSH-082 | P2 | List has no empty text; selection is single only; no multi select rules | AC-EMP-1, AC-SLT-1, AC-SLT-2, AC-SLT-3, AC-SLT-4, AC-SLT-6, AC-SLT-9 | `tess-shell:src/tess_shell/shipped/List/List_Module.tdl` | Add an `Empty` slot and the multi-select keys | [[Empty States]], [[Selection]] |
| TSH-083 | P2 | Rectangle block offers no `Hit_Shape` | AC-BLK-RCT-5 | `tess-shell:src/tess_shell/schema/blocks.py` | Add the key | [[Rectangle Block]] |
| TSH-084 | P2 | Text Input has no error, helper text or `invalid` state | AC-VAL-3, AC-VAL-5 | `tess-shell:src/tess_shell/shipped/TextInput/TextInput_Module.tdl` | Add `Error` and `Helper` slots | [[Validation]], [[Text Field]] |
| TSH-085 | P2 | Marquee has no hover pause | AC-MOD-MQT-7 | `tess-shell:src/tess_shell/binder/marquee.py` | Pause on hover | [[Marquee Text]] |

## AC coverage by note (approximate)

Counts come from the prose of each `Status in code` row, not from a run. "Meets" means met by reading or by design; "fails" means a failing id is named; "open" means named as unverified or not run. The ids are those the rows name.

| Note | Meets (by reading) | Fails | Open |
|---|---|---|---|
| [[Audio Module]] | AC-MOD-AUD-1, 2, 7, 9 | AC-MOD-AUD-4, 5, 6, 8, 10 | none named |
| [[Battery Module]] | AC-MOD-BAT-2, 6, 8 | AC-MOD-BAT-1, 5, 9 | none named |
| [[Clock Module]] | AC-MOD-CLK-1, 4 | AC-MOD-CLK-5, 6 | none named |
| [[Media Module]] | AC-MOD-MED-1, 2, 3, 4, 7, 11 | AC-MOD-MED-5, 6, 8, 10 | none named |
| [[Network Module]] | AC-MOD-NET-2, 5, 7 | AC-MOD-NET-1, 4, 8 | none named |
| [[Tray Module]] | AC-MOD-TRY-1, 2, 3, 8 | AC-MOD-TRY-4, 7 | none named |
| [[Tray Item]] | AC-MOD-TRI-1, 3, 5, 6 | AC-MOD-TRI-2, 4, 8 | AC-MOD-TRI-7 |
| [[Task Item]] | AC-MOD-TIT-1, 2 | AC-MOD-TIT-3, 4, 5, 6, 7 | none named |
| [[Tasks Module]] | AC-MOD-TSK-1, 2, 3, 4, 8 | AC-MOD-TSK-9 | none named |
| [[Menu Item]] | AC-MOD-MIT-1, 2, 3, 6, 7 | AC-MOD-MIT-4, 5 | none named |
| [[Tray Menu]] | AC-MOD-TRM-1, 2, 4 | AC-MOD-TRM-5, 8 | AC-MOD-TRM-3 |
| [[Workspaces Module]] | AC-MOD-WSP-1, 2, 3, 7 | AC-MOD-WSP-4, 6 | AC-MOD-WSP-5 |
| [[Volume OSD]] | AC-OSD-1 to 5, 8, 9, 13 | AC-OSD-15 in part | AC-OSD-6, 7, 14 |
| [[Bar]] | AC-BAR-1, 3, 5, 6, 11, 12, 17 | AC-BAR-4 | AC-BAR-8, 13 |
| [[Auto Hide]] | none | AC-AHD-1 to 19 | none |
| [[Frame]] | AC-FRM2-19, 21 (recorded measurements) | AC-FRM2-11 | AC-FRM2-20, 22, 23 |
| [[Popup]] | AC-POP-3, 4, 8, 10, 11, 12 | AC-POP-6, 7 | AC-POP-1, 9 |
| [[Menu]] | AC-MEN-7, 8, 10, 12 | AC-MEN-1 to 6, 9 | AC-MEN-11, 14 in part |
| [[Tooltip]] | AC-TIP-3, 16 | AC-TIP-4, 13, 17, 21 | AC-TIP-1 |
| [[Launcher]] | AC-LNC-1, 2 to 9, 11, 16, 19 | AC-LNC-13, 18 | AC-LNC-10, 15, 17, 20 |
| [[Peek]] | the built keys (owner KWin check 2026-11-08) | AC-PEK-14, 16, 18 | AC-PEK-3, 17 |
| [[State Layers]] | none | AC-STL-1, 2, 3, 5 | none |
| [[Focus Ring]] | none | AC-FOC-1, 2 | none |
| [[Colour Roles]] | AC-COL-7 | AC-COL-3, 4 | none |
| [[Keyboard Navigation]] | AC-KBN-1, 5, 7, 17 | AC-KBN-2, 3 | none |

## Questions for the tess-shell bot

1. Is the default tooltip `Exit_Delay` of 200 ms set in one place (`schema/model.py:129`) so one change reaches all six cards, and is a hoverable tooltip feasible with the popup window route?
2. Can a `Tooltip` move off a `GROUP` root onto a child in Battery, Network and Audio without changing the module parameters?
3. Does `Enter_Shortcut_Mode` already reveal a hidden surface, so that AC-AHD-9 needs only the Bar `Visible` key? (Input to OQ-25.)
4. Is there a global key or shortcut that a Bar could use to reveal itself today, given that `Reveal_Key` was removed in PR 59?
5. Does the `StatusNotifier` tray item expose a menu request (`ContextMenu`) that a Menu key could call?
6. Can the stylesheet express a state layer (an overlay fill with an opacity) without a new engine key? (Input to OQ-23.)
7. Is the default tooltip card (`Elevation: 20%`) meant to match the Popup shadow, and is a theme level model planned?
8. Where does the density setting belong (theme, settings or a module parameter), and has an owner decision been recorded?
9. Does any test or script measure contrast over the shipped themes, and was the 2.58 to 1 pressed pair known?
10. Has the click-away catcher fault of 2026-11-20 (revert PR #111) a new fix, and does it change the Launcher popup grab rows AC-POP-6 and AC-POP-7?

## Open owner decisions

| Id | Question | Related rows |
|---|---|---|
| OQ-23 | Does the shell adopt state layers ([[ADR-0009 State layer percentages]])? The audit records the gap; the Orchestrator asks the owner. | TSH-020 to TSH-024, TSH-040 |
| OQ-25 | The Bar `Auto_Hide` default (on, 1000 ms) conflicts with keyboard reachability when no reveal key exists and the shortcut-mode reveal is only `proposed`. Which path is the rule? | TSH-010, TSH-050 |
