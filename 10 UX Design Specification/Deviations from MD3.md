---
title: Deviations from MD3
type: register
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [register, md3]
related: ["[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[10 UX Design Specification]]"]
depends_on: []
---

# Deviations from MD3

The register of every departure from Material Design 3 recorded in the notes so far, with its reason and decision. Each row is owned by the note named in its section (one source of truth); this note only collects them, so a change is made in the owning note and re-collected here. Policy: [[ADR-0006 MD3 baseline with named Expressive adoptions]]. 105 rows from 28 notes as of 2026-11-21.

## [[10 Layout Overflow and Scrolling]]

| Deviation | Reason | ADR |
|---|---|---|
| Scrollbars always visible on desktop when content overflows, both axes | MD3 treats scrollbars as a platform concern; the owner reported unreachable content | [[ADR-0003 Scrollbar rule]] |
| Middle ellipsis allowed for paths | the end of a path is the part that identifies it | [[ADR-0004 Tooltip rule]] |
| Tooltip with full value on truncated text | desktop pointer affordance | [[ADR-0004 Tooltip rule]] |
| Single-line field height 40, 32, 28 dp with vertical centring (MD3 56 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Colour Roles]]

| Deviation | Reason | ADR |
|---|---|---|
| Role names from MD3, values from a project's own flat roles in tess-shell (12 roles, mapping above) | The shell is independent of tess-ui and ships its own theme format | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Light `on_*_container` roles at tone 10 (2022 scale), not tone 30 (latest token set) | The 2022 role scale is the baseline | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| High contrast level requires 7:1 for every text pair | Tesserae choice, matches WCAG 1.4.6; the measured baseline already meets it | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| `outline_variant` limited to decoration | Its measured contrast is under 3:1 | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Custom colours (warning, success) with four derived roles | MD3 defines the extension method but no warning or success role | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Elevation]]

| Deviation | Reason | ADR |
|---|---|---|
| Container role for levels 4 and 5 is `surface_container_highest` | No component token file read gives a level 4 or 5 container; choice keeps the ladder monotonic | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Popup container at level 2 | MD3 has no popup; the menu level is used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell expresses elevation as a percentage of one shadow | The shell has its own flat token set; an adoption of levels is not decided | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Focus Ring]]

| Deviation | Reason | ADR |
|---|---|---|
| No ring animation (MD3 grows the ring to 8 dp and shrinks it) | animation adds nothing for desktop use; keeps the ring testable in one frame | [[ADR-0009 State layer percentages]] |
| Ring also shown for pointer focus in text inputs | the caret may be hidden when the window is not active; pointer users need to see which field has focus | [[ADR-0009 State layer percentages]] |
| Inward ring where the control touches a clip edge | prevents clipping in scroll containers | [[ADR-0009 State layer percentages]] |
| Optional gradient ring | Tesserae identity option | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Iconography]]

| Deviation | Reason | ADR |
|---|---|---|
| Material Design Icons instead of Material Symbols; no weight, fill, grade, optical size axes | existing icon set in all projects, engine draws static paths | [[ADR-0007 Icon set and Material Symbols deviation]] |
| 20 dp icon at compact and dense, 16 dp in dense rows | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| Fallback icon is a broken-image glyph | MD3 states no fallback; a visible glyph exposes the missing name | [[ADR-0007 Icon set and Material Symbols deviation]] |

## [[Motion]]

| Deviation | Reason | ADR |
|---|---|---|
| `emphasized` is a single cubic (0.2, 0, 0, 1) | The two-segment path cannot be expressed in the engines' easing forms; Material Web does the same | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Desktop limits on duration (control change at most 200 ms) | Pointer-driven desktop UI; MD3 durations are phone-scale | [[ADR-0002 Desktop density levels and target sizes]] |
| Springs are not in the baseline | Expressive; adopted by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell keeps 3 duration tokens | Shell has its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Scrim]]

| Deviation | Reason | ADR |
|---|---|---|
| One scrim opacity (0.32) for every modal surface | Material Web uses 0.32 for the dialog; Android uses other values per component; one value is testable | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Scrim fade-in of 500 ms is a Material Web value | Verified in Material Web; a desktop shortening is not decided | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Shape]]

| Deviation | Reason | ADR |
|---|---|---|
| Expressive steps 20, 32 and 48 dp excluded from the baseline | Baseline is the 2022 shape scale; Expressive adopted by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell scale has 5 steps with names shifted by one | The shell has its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Popup container radius `extra_small` | MD3 has no popup; the menu value is used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Spacing and Density]]

| Deviation | Reason | ADR |
|---|---|---|
| Three density levels (default, compact, dense) | MD3 specifies touch-first sizes; desktop forms and trees need more rows per screen | [[ADR-0002 Desktop density levels and target sizes]] |
| Desktop minimum target 24 dp (touch 48 dp) | WCAG 2.2 SC 2.5.8 gives 24 CSS px as the AA minimum; MD3 states 48 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Text field 40 dp high at default (MD3 56 dp) | row economy on desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Menu item 40 dp at default (Material Web 48 px) | same | [[ADR-0002 Desktop density levels and target sizes]] |
| Row padding 12, 8, 4 (MD3 16) and icon gap 8, 8, 4 (MD3 16) | narrow side panels | [[ADR-0002 Desktop density levels and target sizes]] |
| Spacing token set with a 2 dp half step | the shell already ships a 2 dp step; focus ring offset is 2 dp | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[State Layers]]

| Deviation | Reason | ADR |
|---|---|---|
| Focus and pressed use 10 percent (the latest MD3 tokens), not the 12 percent of older tokens | follows the current published tokens | [[ADR-0009 State layer percentages]] |
| One layer at a time, with precedence | avoids stacked opacity that changes contrast unpredictably | [[ADR-0009 State layer percentages]] |
| Reduced motion removes the ripple | accessibility | [[ADR-0009 State layer percentages]] |

## [[Theme Following the System]]

| Deviation | Reason | ADR |
|---|---|---|
| Selection of scheme, override and flash rules are Tesserae-specific | MD3 specifies the schemes, not how an application chooses one | [[ADR-0005 Theme follows the system]] |
| Pending surface and re-theme budget values | Design choices to make the no-flash rule testable | [[ADR-0005 Theme follows the system]] |

## [[Typography]]

| Deviation | Reason | ADR |
|---|---|---|
| tess-ui applies tracking 0 for all roles | Engine and theme defaults predate the tracking table; flagged as a gap to close, not a design choice | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Dimensions in dp equal px at scale 1.0 | Projects scale by the window scale factor | [[ADR-0002 Desktop density levels and target sizes]] |
| The 5 shell type roles map to the nearest MD3 role | Shell keeps its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Single-line text vertical centring and ellipsis rules | Desktop controls; owner feedback F5 and F7 | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Accordion]]

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | settings grouping | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Header heights 40, 32, 24 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Open and close use different durations and easings | decelerate in, accelerate out is the MD3 pattern for enter and exit; applied by analogy | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 28 dp; paddings reduced at compact and dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Icon 16 dp at dense | 28 dp container | [[ADR-0002 Desktop density levels and target sizes]] |
| Sizes xs, m, l, xl (32 to 136 px) and the square shape, pressed squaring (Expressive) | tess-ui implements Expressive sizes; the baseline is the 2022 scale | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| Pointer hit area is the container (24 dp floor), 48 dp only in touch contexts | desktop density, WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus ring 3 dp, 2 dp offset, `secondary` | [[Focus Ring]] | [[ADR-0009 State layer percentages]] |

## [[Dialog]]

| Deviation | Reason | ADR |
|---|---|---|
| Several actions allowed in the full-screen header | tess-ui allows `Actions` list there; MD3 has one confirming action | [[Deviations from MD3]] |
| Dialog metrics do not scale with density | Rare, spacious surface; actions still follow density | [[ADR-0002 Desktop density levels and target sizes]] |
| Alert dialog is a `dialog` role where `alertdialog` is missing | Engine limit | [[Deviations from MD3]] |

## [[Form Row]]

| Deviation | Reason | ADR |
|---|---|---|
| A settings row pattern that MD3 lacks | configuration tools are lists of named values | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Label beside the control, not a floating or in-field label | scan by label column, fixed grid | [[ADR-0002 Desktop density levels and target sizes]] |
| Persistent reset button | defaults matter in config files | none; design choice |

## [[Icon Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Container 32 dp and 28 dp, icon 20 dp at compact and dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| 48 dp hit area only in touch contexts; pointer contexts use the container with a 24 dp floor | desktop density and WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Sizes xs to xl, width kinds, square shape and pressed squaring (Expressive) only as named adoptions | MD3 baseline is the 2022 scales | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| Icons from Material Design Icons, not Material Symbols | existing icon set | [[ADR-0007 Icon set and Material Symbols deviation]] |

## [[List Item]]

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 24 (one line) instead of 56 | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Padding 12, 8, 4 dp and gap 8, 8, 4 dp instead of 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Disabled text 0.38 instead of MD3 label opacity 0.30 | one disabled content value across Tesserae ([[State Layers]]) | [[ADR-0009 State layer percentages]] |
| State layer focus and pressed 10 percent instead of the 12 percent listed in the Material Web tokens | decided state layer scale | [[ADR-0009 State layer percentages]] |
| Selected container `secondary_container` | MD3 list tokens give no selected container | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[List]]

| Deviation | Reason | ADR |
|---|---|---|
| Keyboard model from the WAI-ARIA listbox pattern; MD3 defines no list keyboard behaviour | desktop, keyboard first | [[ADR-0010 Document structure of the specifications]] |
| Densities per [[List Item]] | desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Scrollbar visible, no auto-hide | desktop | [[ADR-0003 Scrollbar rule]] |

## [[Menu]]

| Deviation | Reason | ADR |
|---|---|---|
| Item height 40 / 32 / 28 dp (MD3: 48 dp) | Desktop density with a 24 dp minimum target; 48 dp kept for touch | [[ADR-0002 Desktop density levels and target sizes]] |
| State layers 8, 10, 10 percent on items | Same as MD3; the shell has none yet (gap, not a promise) | [[ADR-0009 State layer percentages]] |
| Tab closes the menu | WAI-ARIA Authoring Practices menu pattern; Material Web closes on focusout | [[Deviations from MD3]] |
| Typeahead buffer 500 ms, submenu hover delays 250 and 300 ms | Material Web defaults are 200 ms and 400 ms; shell values are built and decided in the shell vault | [[Deviations from MD3]] |

## [[Panel and Surface]]

| Deviation | Reason | ADR |
|---|---|---|
| Surface tint layer is not applied | tone steps and shadows carry depth in all three projects | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Shell uses 12 flat roles mapped to MD3 roles | shell independent of tess-ui (shell ADR-0006); mapping documented | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Shell elevation is one shadow scaled by a percentage | engine takes shadow lists; levels are a gap, not a promise | [[Deviations from MD3]] |
| Shell shape scale 0, 4, 8, 16, 999 | existing shell tokens; mapped to the MD3 names | [[Deviations from MD3]] |
| Shell surface types (Bar, Frame, Panel, Popup) and melding | desktop shell elements with no MD3 counterpart | [[Deviations from MD3]] |

## [[Popup]]

| Deviation | Reason | ADR |
|---|---|---|
| A popup that takes text input is allowed; MD3 menus hold commands only | Launcher and search flyouts; the text input rule is needed because the outside-click mechanism broke typing on KWin | [[ADR-0001 MD3 role names are the specification vocabulary]] (vocabulary); behaviour recorded here |
| The popup-window route (`xdg_popup`) and its grab have no MD3 counterpart | MD3 is platform-agnostic; Wayland layer-shell hosts clip layers to the surface | [[Deviations from MD3]] |
| Outside click is consumed | MD3 menus dismiss on outside tap; whether the tap is consumed is not specified in the sources read | [[Deviations from MD3]] |

## [[Scrollbar and Scroll Container]]

| Deviation | Reason | ADR |
|---|---|---|
| MD3 has no scrollbar component; Tesserae specifies one | desktop content overflows on two axes and needs a visible indicator | [[ADR-0003 Scrollbar rule]] |
| No auto-hide by default | desktop users need a permanent cue that content continues | [[ADR-0003 Scrollbar rule]] |
| Track-less thumb with opacity states instead of state layers | a thumb is an indicator, not a surface | [[ADR-0003 Scrollbar rule]] |

## [[Switch]]

| Deviation | Reason | ADR |
|---|---|---|
| Track 46 by 28 dp with scaled handles at dense | dense row height 28 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| 40 dp state layer is 32 dp at compact and 28 dp at dense | the layer must not exceed the row | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard focus ring 3 dp, 2 dp offset, role `secondary` | [[Focus Ring]] rule for all controls | [[ADR-0009 State layer percentages]] |
| Enter optional for toggling | follows the WAI-ARIA Authoring Practices | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |

## [[Text Field]]

| Deviation | Reason | ADR |
|---|---|---|
| Container height 40, 32, 28 dp instead of 56 dp (MD3 height from Material Web `textfield/demo` min-height 56 px and the label plus padding stack #needs-verification) | desktop density, config panels hold many fields | [[ADR-0002 Desktop density levels and target sizes]] |
| Body text `body_medium` at compact and dense | 20 dp line box fits 32 and 28 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Label may be external (above the field) | forms with aligned label column ([[Form Row]]) | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Keyboard focus indicator is the 2 dp indicator or outline, no extra ring | MD3 text fields draw no separate ring | [[ADR-0009 State layer percentages]] |
| Escape clears only in search fields | keyboard-first rule | [[ADR-0010 Document structure of the specifications]] (convention only) |

## [[Tooltip]]

| Deviation | Reason | ADR |
|---|---|---|
| Hover delay 500 ms | MD3 sources read (Flutter M3 default wait 0 ms, Compose long-press only) give no desktop hover delay; desktop toolkits use about 500 ms and the code already uses it | [[ADR-0004 Tooltip rule]] |
| Tooltip on keyboard focus is shown within one frame | Keyboard users have no hover; matches WAI-ARIA tooltip pattern | [[ADR-0004 Tooltip rule]] |
| Dismiss on scroll, press and activation | WCAG 1.4.13 dismissible; prevents the F2 and F9 symptoms | [[ADR-0004 Tooltip rule]] |
| Rich tooltip grace period 150 ms | Hoverable condition of WCAG 1.4.13 | [[ADR-0004 Tooltip rule]] |
| Rich tooltip actions reachable by Tab | Keyboard access; MD3 describes touch and pointer | [[ADR-0004 Tooltip rule]] |
| Trigger is the control, never a row or group | Owner feedback F8; MD3 has no row-level tooltip, so this is a restriction rather than a deviation | [[ADR-0004 Tooltip rule]] |

## [[Tree Node]]

| Deviation | Reason | ADR |
|---|---|---|
| A tree row exists although MD3 has no tree | hierarchical data in the config app and shell | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row heights 40, 32, 24 dp instead of the 56 dp one-line list item | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Label type `body_medium` at `compact` and `dense` | fits 32 and 24 dp rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Row padding 12, 8, 4 dp instead of 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Tree]]

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | hierarchical navigation | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Selection does not follow focus | APG: authors choose; avoids accidental action in file trees | none; design choice |

Back to [[10 UX Design Specification]].
