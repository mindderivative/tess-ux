---
title: Routed View
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, pattern, navigation, routing, keyboard, accessibility]
related: ["[[Window]]", "[[Navigation Rail]]", "[[Navigation Drawer]]", "[[Top App Bar]]", "[[Routed View|Screen Transitions]]", "[[Dock]]", "[[Tabs]]", "[[Icon Button]]", "[[Tooltip]]", "[[Dialog]]", "[[Focus Ring]]", "[[Motion]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[Window]]"]
---

# Routed View

> [!info] Summary
> A Routed View is a destination of the application whose content is a view of its own: the window view calls it with a `Route:`, the app registers it as a screen, shows it while it is current and hides the others with their state. Moving between screens is a step in a history the user can go back through. The MD3 counterpart is the destination model of the [navigation rail](https://m3.material.io/components/navigation-rail/overview) and navigation bar; MD3 states no routing, history or back rules, so those come from the project code, the platform back-stack idea and WCAG. Source of truth in code: see Status in code. The note's title is the Inventory name Routed View; the tess-ui component page is called routed views.

## Purpose

An application with more than one main area (Notes, Settings, an editor per document) shows one area at a time. Routed views give each area an address, remember where the user has been, let the user go back, and keep the state of areas they left.

## When to use and not

- Use when: the application has two or more destinations that replace each other in the window, each with its own state and address (a path such as `notes/42`).
- Do not use when: the choice is between views of the same data in one area ([[Tabs]]); panels arranged around content ([[Dock]]); a temporary question ([[Dialog]]); a second OS window ([[Window]]: a second window has no screens and no routes).
- A routed view inside another routed view is a nested screen with a path under its parent's.

## Anatomy

1. Screen: a view called in the window view with `Route:`; named for the view it calls.
2. Route: the screen's path (`""` for home, `settings`, `notes/{id:int}`), optionally a mapping with `Path`, `Guard`, `Redirect` and `Lazy`.
3. History: the ordered entries of screens and params; the current entry; `can_go_back`, `can_go_forward`.
4. Navigation control: [[Navigation Rail]] (`NavigationRailScreens`), a back button, links, handlers `navigate.<Screen>`, `navigate.back`, `navigate.forward`, `navigate_to(...)`.
5. Transition: the animation between two screens ([[Routed View|Screen Transitions]]).
6. Content region: where the current screen is laid out, filling what the navigation control leaves.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Eager screen | Small, always used | built at start; kept with its state when hidden |
| Lazy screen | Rarely visited | `Lazy: true`: built when first reached, then kept; cannot have an `If:` |
| Nested screen | Section with children (`settings`, `settings/profile`) | path under the parent's (a path starting with `/` is from the root); the parent shows while a child is current; a parent's guard covers its children |
| Guarded screen | Needs a condition (signed in) | `Guard` read on every `navigate`, `navigate_to`, `back`, `forward`; falsy keeps the app where it is; `Redirect` names where to go instead; `show()` is a jump and skips the guard |

## States

| State | Visual change | Token values |
|---|---|---|
| Current screen | Attached, laid out, drawn, in the accessibility tree | not applicable |
| Hidden screen | Detached from the window and out of the accessibility tree; its state and bindings are kept | not applicable |
| Transition | Both screens laid over each other (`position: absolute`), the outgoing leaves and the incoming arrives | 90 ms out, 210 ms in, 300 ms total ([[Motion]]) |
| Back unavailable | The back control is disabled: greyed, skipped by Tab, deaf to clicks | disabled scheme ([[State Layers]]) |
| Navigation control, selected destination | Follows the current screen, also after `back()` and `forward()` | see [[Navigation Rail]] |

## Tokens used

The routed view draws nothing of its own: the screen's background is the view's own (`surface` by default, [[Colour Roles]]). Transition easing: `emphasized_accelerate` for the outgoing screen and `emphasized_decelerate` for the incoming one, `emphasized` for a container transform ([[Motion]]). The navigation control uses its own note's tokens.

## Sizing and density

Not applicable: a routed view has no size of its own; the screen fills the content region (`Flex: fill`). Density follows the project's level ([[Spacing and Density]]); the navigation control's sizes are in [[Navigation Rail]]. At the window minimum the screen is still reachable and no destination is clipped ([[10 Layout Overflow and Scrolling]]).

## Dimensions and defaults

The routed view has no size of its own, so the rows give the content region it fills. The minimum height is derived: the window minimum of 240 dp ([[Window]]) less the title bar of a borderless window (40, 32 or 28 dp, [[Title Bar]]); a bordered window's OS title bar is not counted.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| Content region | min width | - | 320 | 320 | 320 | [[Window]] Sizing (minimum window width) | tess-ui: via Window min_width; tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Content region | min height | - | 200 | 208 | 212 | derived from [[Window]] and [[Title Bar]] Sizing: 240 minus 40, 32 and 28 | tess-ui: via Window min_height; tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Screen | height | - | N/A: the screen fills the content region (`Flex: fill`) and has no height of its own | N/A: same as default | N/A: same as default | [[Routed View]] Sizing | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | padding | - | N/A: the routed view draws nothing; the screen's own view sets its padding | N/A: same as default | N/A: same as default | [[Routed View]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | margin | - | N/A: the screen fills the region; the navigation control sets the space beside it | N/A: same as default | N/A: same as default | [[Navigation Rail]] | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Content region | gap | - | N/A: one screen at rest; the space beside the navigation control is that control's own | N/A: same as default | N/A: same as default | [[Navigation Rail]] | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | border width | - | N/A: the routed view draws no border; the screen's own view does | N/A: same as default | N/A: same as default | [[Routed View]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | border color | - | N/A: the routed view draws no border; the screen's own view does | N/A: same as default | N/A: same as default | [[Routed View]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | corner radius | - | N/A: the content region is square and clipped by the window; no shape is drawn | N/A: same as default | N/A: same as default | [[Window]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | font | - | N/A: the routed view draws no text; each screen view sets its own roles | N/A: same as default | N/A: same as default | [[Routed View]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | icon size | - | N/A: the routed view draws no icon; the back control is a separate icon button | N/A: same as default | N/A: same as default | [[Routed View]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Screen | elevation | - | N/A: the routed view paints no surface; the screen's own view sets its elevation | N/A: same as default | N/A: same as default | [[Routed View]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Back control | height | `density.icon_button_container` | 40 | 32 | 28 | [[Spacing and Density]], [[Icon Button]] | tess-ui: yes (IconButton style height); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Back control | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Spacing and Density]], [[Icon Button]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |

## Layout and overflow

- Exactly one screen occupies the content region at rest; its layout is the view's own; it scrolls itself ([[ADR-0003 Scrollbar rule]]).
- During a transition both screens are laid over each other at the origin of the region; afterwards the outgoing screen is detached and both nodes are put back as they were (position, x, y).
- A narrow window may collapse the navigation control (rail to drawer or bar) by window size class ([[10 Layout Overflow and Scrolling]]); the current screen does not change.

## Behaviour

- Navigation: `navigate(name, **params)` pushes a history entry and drops the forward entries; `navigate_to(route)` does the same from a route string; `show(name)` is a jump that replaces the current entry and calls no hook; navigating to the entry already showing (same screen, same params) does nothing; going back or forward restores each step's params.
- Back: `back()` goes to the entry before and returns `False`, doing nothing, when there is none; `forward()` goes to the entry `back()` left. `can_go_back` and `can_go_forward` are signals a back control binds to.
- Keyboard: Alt+Left goes back and Alt+Right forward, except while a text input has focus (Option+Left moves by word on macOS). Escape never navigates; it closes the overlay or cancels the action that is open. The mouse back and forward side buttons do the same, wherever the pointer is.
- Pointer: a click on a navigation control destination navigates; a click on a disabled back control does nothing.
- Touch: an edge swipe back is not specified #needs-verification (MD3 predictive back is an Android system gesture; no desktop rule).
- Routes: `navigate_to` raises `KeyError` when no route matches and leaves the current screen as it is; `app.location` returns the current screen as a route string (the first route that reads its params back exactly) or none; a deep link from the command line is `navigate_to(argument)`. Redirect chains longer than 8 steps raise an error.
- Params: a route reads params from its path (`notes/{id:int}`); the screen reads them as `app.params`; the ViewModel gets `on_navigated(params)` before the screen shows, on every `navigate`, `back` and `forward`; if it raises, nothing changes.
- Focus on a screen change (Tesserae rule): when a navigation control caused the change (a rail destination, a tab), keyboard focus stays on that control; for any other cause (a link, a button, `navigate_to`, a deep link) focus moves to the new screen's initial control, the first focusable control unless the screen names one; on back or forward focus returns to the control that had focus when that entry was left, if it is still present, else the initial control. The focus ring shows only after a key press ([[Focus Ring]]). This follows WCAG 2.2 SC 2.4.3 Focus Order.

## Tooltip and overlay behaviour

- A back control that is an icon button shows a tooltip "Back" on the control only (500 ms, immediate on keyboard focus: [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]); a disabled back control shows it too.
- A screen change closes open tooltips and menus (they dismiss on scroll, press and focus loss; a navigation is all three) ([[Tooltip]], [[Menu]]).
- A modal [[Dialog]] open over a screen blocks Alt+Left and the mouse side buttons until it closes #needs-verification.
- The routed view opens no overlay of its own.

## Motion

- The transition between screens is the app's `transition` (`none`, `fade_through`, `shared_axis_x`, `shared_axis_y`, `shared_axis_z`, `container_transform`): the outgoing screen leaves in 90 ms and the incoming arrives in the next 210 ms (container transform: one 300 ms move); a shared axis slides 30 px; going back reverses the direction ([[Routed View|Screen Transitions]], [[Motion]]).
- A new navigation while one plays finishes the first at once. With reduced motion on, the swap is instant (one frame).
- The default transition is `fade_through` for destinations of equal rank (rail destinations) and `none` for the first screen shown #needs-verification (a Tesserae choice; the code default for `app.transition` is not stated in the docs read).

## Accessibility

- A screen change is announced: the new screen's title is announced once, politely, through `Window.announce` after the change (WCAG 2.2 SC 4.1.3 Status Messages: a change the user must be told about without moving focus) #needs-verification (not heard with a screen reader yet, [[Accessibility Rules]] AR-29).
- Hidden screens are out of the accessibility tree; only the current screen's nodes are exposed. The navigation control exposes the selected destination (selected state) and it follows `back()` and `forward()`.
- Keys: Alt+Left, Alt+Right as above; no single-character shortcut.
- The back control has role `button` and the name "Back", disabled when unavailable.
- Every screen has a visible way back or to its parent (back control, rail, breadcrumb) in addition to the keyboard shortcut and the mouse buttons.
- Focus order within the screen is the view order (WCAG 2.2 SC 2.4.3).
- The transition never carries information alone and respects reduced motion ([[14 Accessibility Basics]]).

## Dark and light

No colours of its own. During a container transform and a fade through both screens draw in the same scheme; a scheme change during a transition finishes it first.

## Defaults

| Setting | Default |
|---|---|
| History | on; unlimited entries #needs-verification |
| Back shortcuts | Alt+Left, Alt+Right, mouse side buttons |
| Transition | the app's `transition` (see Motion) |
| Redirect limit | 8 |
| Screens | eager; `Lazy` off |
| Hidden screen state | kept |
| Back control | disabled when `can_go_back` is false |

## Acceptance criteria

- [ ] AC-RTV-1 (scripted input): a window view with three routed calls registers three screens named for their views; at rest exactly one screen is attached and laid out, the other two are detached and absent from the accessibility tree; text typed into a screen's field, then navigating away and back, is still there; a `Lazy` screen is not built until first reached and is kept afterwards. Pass: attached-screen list, field value, build counts.
- [ ] AC-RTV-2 (scripted input): history: `navigate` A, B, C then `back` twice gives C, B, A; `forward` gives B; `navigate` D from B drops C (`can_go_forward` false); navigating to the showing entry changes nothing; `show` replaces the current entry and calls no `on_navigated`; `back` with no entry returns `False` and changes nothing. Pass: current screen, history and signal values after each step.
- [ ] AC-RTV-3 (scripted input): a back control bound to `not can_go_back` is disabled at the first entry: skipped by Tab, a click does nothing, its accessibility state is disabled; after one `navigate` it is enabled and a click goes back. Pass: focus order, call counts and AT state.
- [ ] AC-RTV-4 (scripted input): with focus on a non-text control Alt+Left goes back and Alt+Right forward; with focus in a text input neither navigates; the mouse back and forward side buttons navigate with the pointer over any node; Escape never navigates, in any focus position. Pass: current screen after each of eight inputs.
- [ ] AC-RTV-5 (scripted input): with routes `""`, `notes` and `notes/{id:int}`, `navigate_to("notes/42")` shows screen Note with params `{"id": 42}` and `location` is `notes/42`; back and forward restore params; `show` clears params; `navigate_to("nope")` raises `KeyError` and leaves the current screen unchanged. Pass: screen, params, location, exception.
- [ ] AC-RTV-6 (scripted input): a falsy `Guard` on `navigate`, `navigate_to`, `back` and `forward` keeps the app where it is; a guard that returns a route sends the app there; `show` skips the guard; a parent's guard covers its children; a redirect loop raises an error after 8 steps. Pass: current screen after each of six cases, error on the ninth redirect.
- [ ] AC-RTV-7 (scripted input): nested screens: `settings` holding `profile` has the path `settings/profile`; a child path starting with `/` is read from the root; the parent shows while a child is current; the app's transition plays between siblings of one parent. Pass: route table and visible screens.
- [ ] AC-RTV-8 (scripted input): with `fade_through` the outgoing screen reads opacity 0 by 90 ms and the incoming reads 1 by 300 ms, both laid over each other during the play and back at their original position, x and y afterwards (outgoing detached); going back with a shared axis reverses the direction; with reduced motion the swap completes in one frame; a second navigation during a play finishes the first. Pass: opacity and translate values at 0, 90, 300 ms and node placement afterwards.
- [ ] AC-RTV-9 (scripted input): after a navigation caused by a non-navigation control the focused node is the new screen's initial control (the first focusable unless named) within one frame; after one caused by a rail destination focus stays on that destination; after `back` focus is on the control that had focus when the entry was left, or the initial control if it is gone; the ring shows only after a key press. Pass: focused node ids in four cases.
- [ ] AC-RTV-10 (AT tree assertion): after `navigate`, `back` and `forward` exactly one announcement with the new screen's title reaches `announce` (polite), within one frame of the change; the previous screen's nodes are not in the tree; the selected destination of the navigation control equals the current screen. Pass: announce call list and tree contents.
- [ ] AC-RTV-11 (scripted input): a `NavigationRailScreens` destination activated by click, Enter or Space navigates and adds a history entry; `back()` returns and the rail selection follows within one frame; the rail stays focusable and keeps focus on activation. Pass: history, selected item and focused node.
- [ ] AC-RTV-12 (geometry check): at rest the current screen's root equals the content region (width and height within 0.5 dp) at the window minimum and at 1100 by 700 dp; no hidden screen has a laid-out box; after a transition no node keeps `position: absolute`. Pass: rectangles and property values.
- [ ] AC-RTV-13 (scripted input): `location` saved to a file and `navigate_to(location)` in a new run reopens the same screen with the same params; an unknown saved location is ignored and the home screen shows. Pass: screen and params in both runs #needs-verification (the fallback to home is a Tesserae choice; the code raises `KeyError`).
- [ ] AC-RTV-14 (review): every screen reachable only through another has a visible way back or up in addition to Alt+Left, Alt+Right and the mouse buttons; no screen is a dead end; the reviewer lists the route graph and the back control of each. Pass: sign-off.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/app.py` (`show`, `navigate`, `navigate_to`, `back`, `forward`, `navigate_with`, `guard`, `route`, `location`, `can_go_back`, `can_go_forward`), `tess-ui:src/tess_ui/screen_transition.py` (`OUT_MS` 90, `IN_MS` 210, `DISTANCE` 30), `tess-ui:docs/components/routed-views.md`, `tess-ui:docs/guide/apps-and-screens.md`, tests `tess-ui:tests/test_routed_views.py`, `test_routing.py`, `test_route_params.py`, `test_route_tree.py`, `test_screen_transition.py` | Partly meets. Meets (per code and docs, not all run): registration and hidden screens with state, `Lazy`, history with push, back and forward, params, routes and `location`, guards and redirects (limit 8), nested screens, the Alt+Left and Alt+Right keys excluding text inputs, mouse side buttons, `can_go_back` and `can_go_forward` signals with a disabled back control, `NavigationRailScreens` following back and forward, transitions at 90 and 210 ms with reduced-motion swap (AC-RTV-1 to AC-RTV-8, AC-RTV-11). Fails AC-RTV-9: no focus management on a screen change was found in `app.py` (the only `focus_first` is for overlays). Fails AC-RTV-10: no `announce` call was found in `app.py` for a screen change [INFERENCE from a search of the module, not run]. AC-RTV-13 fails: an unmatched route raises `KeyError`, no home fallback is specified in code. AC-RTV-12 and AC-RTV-14 are not run. The emphasized easing used by a transition differs between `theme.py` and `spec/transition.py` ([[Motion]]). Not built: a push and pop stack apart from the history; edge-swipe back |
| tess-ui (dimensions) | `tess-ui:src/tess_ui/app.py` | No project value differs from [[#Dimensions and defaults]]: the routed view paints nothing; the minimum content height is derived from the window and title bar values, whose differences are listed in [[Window]] and [[Title Bar]] |
| tess-shell | not applicable | Not applicable: the shell has no routed screens; modules do not navigate. The configuration app (`tess-ui:apps/shell_config`) is one screen |
| tre | not applicable | Not applicable: the engine has no routing or history; it delivers key and pointer button events (Alt+Left, side buttons are tess-ui's reading) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Routes, history, guards and back rules exist (MD3 states destinations only) | an application with many screens needs addressing and back behaviour | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Alt+Left and Alt+Right and mouse side buttons go back and forward | desktop convention; MD3 has the Android system back gesture | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Focus placement and screen announcement on a screen change | keyboard-first and screen-reader use; MD3 does not state them | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Fade through 300 ms (90 out, 210 in) from [[Motion]] | an MD3 transition pattern with Tesserae timings | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- MD3 navigation rail (destinations), the nearest counterpart; the page is a script-rendered app and returns no text: https://m3.material.io/components/navigation-rail/overview
- Android principles of navigation (back stack and back behaviour; page fetched, but no value was read from it, so no number in this note depends on it) #needs-verification: https://developer.android.com/guide/navigation/principles
- WCAG 2.2 SC 2.4.3 Focus Order (verified 2026-11-21): https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html
- WCAG 2.2 SC 4.1.3 Status Messages (verified 2026-11-21): https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- tess-ui: `tess-ui:docs/components/routed-views.md`, `tess-ui:docs/guide/apps-and-screens.md` (Navigation and history, Routes and deep links), `tess-ui:src/tess_ui/screen_transition.py`; motion tokens in [[Motion]].
- Not verified: the focus rule, the announcement, the home fallback for an unknown saved route, the unlimited history, the default transition and the edge-swipe rule are Tesserae design choices #needs-verification.
