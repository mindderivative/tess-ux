---
title: Inventory Source tess-ui Foundations
type: research
status: research
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [research, inventory]
related: ["[[Inventory]]"]
depends_on: []
---

# Inventory Source tess-ui Foundations

Raw element rows from the Phase 0 read of tess-ui Foundations, unmerged. The merged table is [[Inventory]]. Paths are relative to the project root with the project prefix.

| Element | Kind | Defined | Used | MD3 counterpart | Code status | Spec note |
| --- | --- | --- | --- | --- | --- | --- |
| Colour roles | foundation | tess-ui:src/tess_ui/tokens.py, tess-ui:src/tess_ui/theme.py | every stylesheet and widget | [Color roles](https://m3.material.io/styles/color/roles) | exists; 49 roles from seed, light and dark | `Colour Roles` |
| Dynamic colour from seed | foundation | tess-ui:src/tess_ui/tokens.py, tess-ui:docs/themes/index.md | App(theme_seed=), theme Seed | [Dynamic color](https://m3.material.io/styles/color/dynamic-color/overview) | exists; TonalSpot only, spec 2021; no user-wallpaper extraction | `Dynamic Colour` |
| Theme switching (light/dark) | behaviour | tess-ui:src/tess_ui/app.py, tess-ui:src/tess_ui/follow.py | App.set_dark, set_theme_specs, hot reload | [Color system](https://m3.material.io/styles/color/system/overview) | exists; in-place re-theme, no view rebuild | `Theme Switching` |
| Follow system appearance | behaviour | tess-ui:src/tess_ui/app.py | App(dark="system") | none (Tesserae-specific) | partial; Linux known at start via portal, macOS/Windows after first frame, headless dark | `System Appearance Following` |
| High contrast | behaviour | tess-ui:src/tess_ui/tokens.py, tess-ui:src/tess_ui/app.py | App(high_contrast="system") | [Color contrast](https://m3.material.io/foundations/designing/color-contrast) | partial; scheme contrast 0 or 1 only | `High Contrast` |
| Reduced motion | behaviour | tess-ui:src/tess_ui/motion.py | ripple, screen transitions, transitions | [Motion](https://m3.material.io/styles/motion/overview) | exists; durations 0, repeating animation not started | `Reduced Motion` |
| Theme file and cascade | pattern | tess-ui:src/tess_ui/spec/tdl_theme.py, tess-ui:src/tess_ui/spec/cascade.py | App(custom_theme=) | none (Tesserae-specific) | exists; shipped rules, stylesheet, node Style layers | `Theme Cascade` |
| Stylesheet rules and states | pattern | tess-ui:src/tess_ui/spec/tdl_stylesheet.py, tess-ui:docs/stylesheets/index.md | views/*_Stylesheet.tdl | none (Tesserae-specific) | exists | `Stylesheet Rules` |
| Typography scale | foundation | tess-ui:src/tess_ui/tokens.py | Text Typography_Role | [Typography](https://m3.material.io/styles/typography/overview) | partial; 15 roles, tracking 0 by default (MD3 values defined unused) | `Type Scale` |
| Fonts | foundation | tess-ui:src/tess_ui/fonts.py, tess-ui:src/tess_ui/font_families.py | App(system_fonts=) | [Typography](https://m3.material.io/styles/typography/overview) | exists; Roboto, Noto Sans Arabic, Hack Nerd Font Mono bundled | `Fonts` |
| Shape scale | foundation | tess-ui:src/tess_ui/tokens.py | Corner_Radius in sheets | [Shape](https://m3.material.io/styles/shape/overview-principles) | partial; no increased/XXL tokens | `Shape Scale` |
| Elevation | foundation | tess-ui:src/tess_ui/tokens.py | Elevation in sheets | [Elevation](https://m3.material.io/styles/elevation/overview) | exists; 6 levels as paired shadows, no tint | `Elevation` |
| Motion tokens | foundation | tess-ui:src/tess_ui/theme.py, tess-ui:src/tess_ui/spec/transition.py | Transition in sheets | [Motion easing and duration](https://m3.material.io/styles/motion/easing-and-duration/tokens-specs) | partial; emphasized curve differs between two files | `Motion Tokens` |
| Style transitions | behaviour | tess-ui:src/tess_ui/spec/transition.py | views/*_Stylesheet.tdl | [Motion](https://m3.material.io/styles/motion/overview) | exists; literal ms, not token names | `Style Transitions` |
| Screen transitions | behaviour | tess-ui:src/tess_ui/screen_transition.py | App.navigate_with | [Transitions](https://m3.material.io/styles/motion/transitions/transition-patterns) | exists; fade through, shared axis x/y/z, container transform | `Screen Transitions` |
| State layers | state | tess-ui:src/tess_ui/interaction.py | all clickable nodes | [State layers](https://m3.material.io/foundations/interaction/states/overview) | exists; 8/10/10/16 percent | `State Layers` |
| Ripple | behaviour | tess-ui:src/tess_ui/interaction.py, tess-ui:src/tess_ui/ripple.py | clickable nodes | [Interaction states](https://m3.material.io/foundations/interaction/states/overview) | exists; node circles or optional shader | `Ripple` |
| Focus ring | state | tess-ui:src/tess_ui/interaction.py, tess-ui:src/tess_ui/focusring.py | clickable nodes | [Focus indicators](https://m3.material.io/foundations/designing/structure) | exists; 3 px, 2 px offset, secondary, optional gradient | `Focus Ring` |
| Disabled state | state | tess-ui:src/tess_ui/controls.py | controls | [State layers](https://m3.material.io/foundations/interaction/states/state-layers) | exists; 38 and 12 percent | `Disabled State` |
| Keyboard navigation and focus groups | behaviour | tess-ui:docs/guide/interaction.md, tess-ui:docs/guide/view-language.md | toolbars, tabs, menus, radio sets | [Keyboard](https://m3.material.io/foundations/designing/structure) | exists; one tab stop per focus_group, arrows, Home/End, type-ahead | `Keyboard Navigation` |
| Iconography | foundation | tess-ui:src/tess_ui/icons.py | Icon, IconButton | [Icons](https://m3.material.io/styles/icons/overview) | partial; static Material Symbols paths plus MDI, no weight/fill/grade axes | `Iconography` |
| Window size classes | foundation | tess-ui:src/tess_ui/tokens.py, tess-ui:src/tess_ui/app.py | app.width_class, app.height_class | [Window size classes](https://m3.material.io/foundations/layout/applying-layout/window-size-classes) | exists | `Window Size Classes` |
| Density | foundation | absent | n/a | none (Material 3 has no density scale) #needs-verification | planned; no density setting in tess-ui | `Density` |
| Spacing | foundation | absent as tokens; literals in tess-ui:src/tess_ui/views/*_Stylesheet.tdl | all sheets | [Spacing](https://m3.material.io/foundations/layout/understanding-layout/spacing) | partial; no spacing tokens | `Spacing` |
| Touch and hit targets | foundation | tess-ui:src/tess_ui/controls.py | controls | [Accessibility](https://m3.material.io/foundations/designing/structure) | exists; 48 px target, 40 px state layer | `Touch Target` |
| Scrollbars | widget | tess-ui:src/tess_ui/spec/build.py | ScrollView | none (Tesserae-specific) | partial; colour only (outline), geometry engine-owned | `Scrollbar` |
| Tooltips (plain and rich) | tooltip | tess-ui:src/tess_ui/composed.py | tooltip: on any node | [Tooltips](https://m3.material.io/components/tooltips/overview) | exists; 500 ms delay, rich has subhead and actions | `Tooltip` |
| Selection | state | tess-ui:src/tess_ui/controls.py, tess-ui:src/tess_ui/list_controls.py | lists, chips, checkbox | [Selection](https://m3.material.io/foundations/interaction/selection) | exists; selected state in rules | `Selection` |
| Drag and drop | behaviour | tess-ui:src/tess_ui/docking.py, tess-ui:src/tess_ui/dockhost.py | dock host | [Gestures](https://m3.material.io/foundations/interaction/gestures) | partial; dock panels only, 4 px threshold | `Drag and Drop` |
| Validation and error state | state | tess-ui:src/tess_ui/a11y.py, tess-ui:src/tess_ui/views/TextField_Stylesheet.tdl | text fields | [Text fields](https://m3.material.io/components/text-fields/overview) | exists; State: error, a11y invalid | `Validation` |
| Accessibility announcements | behaviour | tess-ui:src/tess_ui/a11y.py | all widgets | [Accessibility](https://m3.material.io/foundations/designing/structure) | exists; live off/polite/assertive, roles, a11y_action | `Accessibility Announcements` |
| Notifications | pattern | tess-ui:src/tess_ui/overlays.py, tess-ui:src/tess_ui/views/Snackbar_View.tdl | Snackbar | [Snackbar](https://m3.material.io/components/snackbar/overview) | exists | `Notifications` |
| Empty, loading and error states | pattern | absent as a shared pattern; loading in tess-ui:src/tess_ui/views/Button_Stylesheet.tdl | Button loading, a11y busy | [Progress indicators](https://m3.material.io/components/progress-indicators/overview) | partial; no empty or error screen pattern | `Empty Loading Error States` |
| Scrim | foundation | tess-ui:src/tess_ui/overlays.py | Dialog, modal side sheet, drawer | [Dialogs](https://m3.material.io/components/dialogs/overview) | partial; scrim is the overlay's own alpha colour, not the scrim role | `Scrim` |
| Hot reload of theme and stylesheet | behaviour | tess-ui:src/tess_ui/app.py, tess-ui:src/tess_ui/spec/watch.py | run(hot_reload=True) | none (Tesserae-specific) | exists | `Theme Hot Reload` |
| Shell theme vocabulary | foundation | tess-ui:apps/shell_config/tests/fixtures/shipped/Themes/Default_Theme.tdl | shell_config editor fixture | none (Tesserae-specific) | partial; separate token set (Color, Type, Shape, Space, Elevation, Motion, Modes) | `Shell Theme Tokens` |

Back to [[90 Research]].
