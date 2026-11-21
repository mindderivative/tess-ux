---
title: Test Method
type: quality
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [quality, testing]
related: ["[[01 Principles and Scope]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[Text Field]]", "[[Switch]]", "[[Icon Button]]", "[[Button]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Tree]]", "[[Owner Feedback 2026-11-20]]", "[[Plan]]"]
depends_on: ["[[01 Principles and Scope]]"]
---

# Test Method

> [!info] Summary
> The seven test types every acceptance criterion names, how each is run in tess-ui, tess-shell and tre, which parts need a real display or a human, and the audit format for `70 Adoption`. A criterion that no test type can pass or fail is not accepted into the specification ([[01 Principles and Scope]], principle 7).

## Ground rules

- Every acceptance criterion `AC-<prefix>-<n>` names exactly one primary test type and states the pass condition in numbers. A criterion may add a second type (for example a token test plus a pixel check).
- Units: dp equals px at scale factor 1.0. Geometry checks run at scale 1.0, 1.25 and 2.0 and compare in dp (measured px divided by scale) with the tolerance the criterion states.
- Tests run headless wherever possible. Tests that need a real compositor (KWin popups, input grabs, screen readers) are hand checks with a recorded script, and the audit says "hand check, not automated".
- A project's audit never reports a criterion as passing that it did not run; the allowed results are pass, fail with defect, not run with reason, not testable (with reason) and not applicable (with reason).

## The seven test types

| Type | What it checks | Pass condition form |
|---|---|---|
| Token test | a value in the project's token or stylesheet source equals the specified value, or references a role (no literal) | exact equality or "is a role reference" |
| Geometry check | positions and sizes of laid-out nodes, in dp | equality or inequality with a tolerance of at most 0.5 dp unless stated |
| Pixel check | colours or shapes read from a rendered frame | pixel inside or outside a region, colour within a stated distance, offsets within 1 px |
| Contrast script | contrast ratio of role pairs per scheme | ratio at or above a limit (4.5, 3, 7 to 1) |
| Scripted input | a sequence of key, pointer and time events, then state, event counts and visible overlays | observed state equals the expected list |
| AT tree assertion | role, name, description and state flags of nodes in the accessibility tree | property equality |
| Review | a human reads and answers yes or no from a checklist | checklist complete, reviewer named, date recorded |

## How each type runs, per project

### tess-ui (`tess-ui`, pytest)

- Environment: `tests/real_session.py` removes the person's display and session bus so tests never touch a real desktop, points config and cache at a private folder, and renders on Mesa software Vulkan (lavapipe) where installed, as CI does. A hand run on the real session needs `TESS_UI_ALLOW_REAL_SESSION=1`.
- Token test: read the shipped stylesheet and view TDL (`src/tess_ui/views/<Name>_Stylesheet.tdl`, `<Name>_View.tdl`) and the theme token tables in `src/tess_ui/theme.py` and `tokens.py`; the existing tests assert roles with `node.get("fill") == role(view, "on_surface")` (example `tests/test_accordion.py`). Add: scan of stylesheets for colour literals.
- Geometry check: build a `View` in an `App(width=..., height=..., theme_seed=..., dark=...)`, call `app.window.advance(ms)` and read `node.get("layout_x")`, `layout_y`, `layout_width`, `layout_height` (examples in `tests/test_accordion.py`). For scale 1.25 and 2.0 set the window scale factor if the test window supports it #needs-verification.
- Pixel check: `app.window.advance(32)` then `rgba, width, height = app.window.snapshot()` and index `rgba[(y * width + x) * 4:...]` (helper pattern in `tests/test_effects_visual.py`). For "no pixel outside a region", snapshot before and after the action and diff.
- Scripted input: `window.simulate("click", node=n)`, `simulate("pointer_enter", node=n)`, `simulate("key_down", key="enter")`, then `window.advance(ms)` for timers (examples `tests/test_button.py`); the shell config app has a headless test driving the window with key events only (`docs/guide/shell-config.md`).
- AT tree assertion: read `node.get("role")`, `label`, `description`, `expanded`, `checked`, `a11y_hidden`, `focusable`; the engine path for assistive requests is `window.simulate("a11y_action", node=..., action=..., value=...)` (`tre:docs/guide/accessibility.md`). Existing tests: `tests/test_a11y*.py`.
- Contrast script: compute relative luminance from the resolved role colours of `Theme` for light, dark and high contrast; the script is new (none exists) and lives in the project's `tests/`; spec of the script below.
- Run only the affected tests (`pytest tests/test_<component>.py`); the full suite is not run per change.

### tess-shell (`tess-shell`, pytest plus hand checks)

- Environment: pytest with fakes (`tests/fake_kwin.py`, `fake_dbus.py`, `fake_input_server.py`, `fake_portal.py`); an AT-SPI helper `tests/atspi_env.py` runs a private bus (`tests/test_announce_atspi.py` checks `announce` against AT-SPI's `Announcement` signal).
- Token test: read the Default stylesheet (`src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl`) and the look model (`src/tess_shell/model/look.py`) and compare to the spec value. The shell has 12 flat roles; the mapping to MD3 role names is the table of [[ADR-0001 MD3 role names are the specification vocabulary]] and a token test goes through that mapping.
- Geometry, pixel and scripted input: module tests build the module in a headless tre window as tess-ui does; surfaces that need KWin (Popup, Launcher, Frame) are hand checks with the kits `tests/test_kwin_*_kit.py` and the "Hand Checks" note (`tess-shell:docs/design/00 Home/Hand Checks.md`); results are recorded there.
- AT tree assertion: via the module's role and state keys read from the built tree; real screen-reader runs are hand checks (Orca is not installed on the owner's machine today, so those items are "not run").
- Contrast script: required by the shell accessibility rule 9 and not yet existing (`tess-shell:docs/design/60 Quality/Accessibility.md`); the spec script below is the target.

### tre (`tre`, cargo and pytest)

- tre owns primitives, not components: it is tested for the properties the specification relies on, listed in the Status in code table of each component (for example `overflow="ellipsis"`, `max_length`, `caret_blink`, scroll view keys, `announce`).
- Pytest over the Python bindings with `window.simulate` and `window.snapshot` as above; a private bus for AT-SPI (`tests/atspi_env.py`); Rust unit tests in `crates/*`.
- To pick tests for a change run `python3 -I tools/tests_for.py` (it prints the commands and runs nothing); no full suite without the owner's word (`tre:AGENTS.md`).

## Contrast script specification

- Input: the resolved colour of each role for a scheme (light, dark, high contrast), as sRGB.
- Method: WCAG 2.2 relative luminance and contrast ratio ([definition](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio)): ratio = (L1 + 0.05) / (L2 + 0.05).
- Alpha: colours with alpha (state layers, disabled at 38 percent) are composited over their actual background before measuring.
- Pairs: the list "role on role" of [[Colour Roles]] (for example `on_surface` on `surface_container_highest`); a component criterion may add a pair.
- Output: a table scheme, pair, ratio, limit, pass; non-zero exit when any pair fails. The audit records the table.

## Hand check format

A hand check records: id, steps (keys and pointer moves), expected result, environment (compositor, version, scale, theme), observed result, tester, date. Hand checks are the only way to cover real KWin behaviour and real screen readers; they never count as automated.

## Audit format for `70 Adoption`

One note per project and spec slice, named `Audit <project> <slice> <date>`, with this front matter and table:

```yaml
---
title: Audit tess-ui Text Field 2026-12-01
type: audit
status: draft
owner: phil
created: 2026-12-01
updated: 2026-12-01
tags: [audit]
related: ["[[Text Field]]"]
depends_on: ["[[Text Field]]"]
---
```

| Criterion | Type | Result | Evidence | Defect or note |
|---|---|---|---|---|
| AC-TXF-1 | geometry check | pass, fail, not run, not testable or not applicable | test name and commit, or screenshot path | link to the issue or request note |

Rules for the audit:

- One row per criterion of the audited notes; no row is omitted.
- Evidence is a test name with commit hash, a recorded hand-check id, or a screenshot path in the project's repo; "looks right" is not evidence.
- The audit states the project commit it ran against and the date; it ends with a count: pass, fail, not run, not testable, not applicable.
- A failing criterion gets a defect link; the audit does not fix code. Audits are routed through `bot:Orchestrator` ([[Plan]]).
- The `Status in code` table of the component note is updated from the audit by the vault, with the audit linked.

## Acceptance criteria

- [ ] AC-TM-1: Review. Every `AC-*` item in every note names one of the seven test types in its first sentence. Pass: a script that parses acceptance-criteria lists finds zero items without a type name.
- [ ] AC-TM-2: Contrast script. The script exists in a project, runs on light and dark, and exits non-zero when a pair is below its limit (negative test with a deliberately low-contrast pair). Pass: exit codes equal 0 and non-zero respectively.
- [ ] AC-TM-3: Review. Each audit in `70 Adoption` has a row for every criterion of its notes and a count per result value (pass, fail, not run, not testable, not applicable) that sums to the number of rows. Pass: arithmetic holds.

## Sources

- `tess-ui:tests/real_session.py`, `tess-ui:tests/test_effects_visual.py` (snapshot helper), `tess-ui:tests/test_accordion.py` (geometry and role assertions), `tess-ui:tests/test_button.py` (simulate), `tess-ui:docs/guide/shell-config.md` (key-only test).
- `tess-shell:tests/` (fakes, AT-SPI helper, KWin kits), `tess-shell:docs/design/60 Quality/Accessibility.md`.
- `tre:docs/guide/accessibility.md` (testing section, `simulate("a11y_action")`), `tre:AGENTS.md` (test selection rule).
- [WCAG 2.2 contrast ratio definition](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio) (the formula is the standard definition; the anchor was not separately fetched).
- Scale-factor testing of geometry in tess-ui is not confirmed in the code read and is marked #needs-verification.
