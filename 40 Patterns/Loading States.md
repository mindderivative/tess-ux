---
title: Loading States
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, state, loading, progress]
related: ["[[40 Patterns]]", "[[Empty States]]", "[[Error States]]", "[[Notifications]]", "[[Button]]", "[[Progress Indicator]]", "[[Circular Progress Indicator]]", "[[Linear Progress Indicator]]", "[[Motion]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Motion]]", "[[Colour Roles]]", "[[Spacing and Density]]"]
---

# Loading States

> [!info] Summary
> How a view, region or control shows that it waits for something: nothing for short waits, a skeleton or a spinner for regions, a progress bar when the fraction is known, a busy flag always. The MD3 counterpart is [progress indicators](https://m3.material.io/components/progress-indicators/overview); skeletons and timeouts are Tesserae rules. Source of truth in code: see Status in code.

## Problem

Every project has the pieces and no rule for combining them: tess-ui has `Button` `Loading` and progress indicators, tre has the `busy` flag, the shell has an Image placeholder; nothing says when to show what, how long to wait before showing it, or what happens when the wait does not end ([[Gaps and Contradictions]], summary item 8; evidence "Empty, loading and error states have no engine support beyond `busy`, `invalid`, `description` and `live` flags").

## Purpose

Make a wait visible without flashing for short waits, honest about its length, and always leaving the user a way out.

## When to use and not

- Use when: content or an action result is pending for more than 200 ms.
- Do not use when: the wait is under 200 ms (show nothing); the thing is empty ([[Empty States]]); the load failed ([[Error States]]).

## Rules

1. Delay: nothing visible changes in the first 200 ms of a wait. After 200 ms the loading indicator appears; once shown it stays at least 400 ms, so a wait that ends at 250 ms does not flash (design choice, #needs-verification-as-design-choice).
2. The `busy` flag is set on the waiting node from the start of the wait (0 ms), independent of the delay, and cleared when the wait ends. A screen reader hears busy even when nothing is drawn yet ([[14 Accessibility Basics]]).
3. Choose the indicator by what is known (decision table). A determinate bar is used when the fraction is known; a bar never moves backwards.
4. A waiting control keeps its place and size: the button spinner replaces the leading icon and the button width does not change; the control takes no second activation ([[Button]]).
5. A waiting region keeps its container size: a skeleton or spinner occupies the same bounds as the content it replaces, so nothing below moves when content arrives.
6. Only one indicator is visible for one wait. A region with a spinner has no spinner in its child controls for the same wait.
7. Timeouts: after 10 s without progress the region adds the text "Still loading" and a Cancel action; after 30 s, or at the project's stated timeout, the wait ends in an [[Error States|error state]] with Retry (design choice, #needs-verification-as-design-choice). The timer is the app's: tre has `window.after`, no built-in timeout.
8. A wait the user started and can cancel (save, check, import) offers Cancel from 200 ms onward; a wait the user did not start (background refresh) never blocks input and shows no modal.
9. The end of a long action (more than 3 s) is announced politely once, with its result ([[Notifications]]). Progress percentages are not announced on every update; the node exposes `value` and the reader polls it (an announcement at most every 25 percent, design choice).
10. Reduced motion: indeterminate indicators become a still arc or bar and the text "Loading" is shown next to it; determinate bars update without easing ([[Motion]], [[14 Accessibility Basics]]).
11. Skeletons use `surface_container_highest` blocks with the shape of the content and no shimmer under reduced motion; they carry no accessible name of their own (the region has `busy`).

## Decision table

| What is waiting | Known fraction | Expected length | Show | Cancel |
|---|---|---|---|---|
| A button action (Save, Check) | no | under 3 s | spinner in the button, `busy` | no |
| A button action | no | over 3 s | spinner in the button plus status text in the status line | yes |
| A region of content (list, form, preview) | no | 200 ms to 3 s | skeleton of the content shape | no |
| A region of content | no | over 3 s | circular indeterminate indicator centred, text "Loading" | yes after 10 s |
| A transfer, import, build | yes | any | linear determinate bar with the percentage as text | yes |
| An image or icon | no | any | placeholder at the final size (shell Image `Placeholder`) | no |
| Whole-window start | no | any | window shell and skeleton, never a blank frame | no |
| Background refresh | no | any | no indicator on the content; `busy` only | no |

## Examples (short snippets only)

```tdl
Button { Label: Check, Loading: <| checking |>, On_Click: run_check }
CircularProgressIndicator { Label: "Loading files" }
LinearProgressIndicator { Value: <| sent |>, Label: Uploading }
```

The config app runs `check` on a worker thread with a 10 s timeout and reports a failed or late check as one message row in the Problems list while editing continues (`tess-ui:apps/shell_config/README.md`, "Check, saving and the shell").

## States

| State | Visual change | Token values |
|---|---|---|
| Waiting under 200 ms | none; `busy` true | none |
| Indicator shown | indicator in `primary` on the surface, track `secondary_container` | [[Colour Roles]] |
| Determinate | arc or bar length equals value 0 to 1; eased to each new value | [[Motion]] |
| Slow (over 10 s) | text "Still loading" and Cancel | `body_medium` |
| Timed out | error state | [[Error States]] |
| Reduced motion | still indicator plus text | [[Motion]] |

## Sizing and density

Indicator sizes are Tesserae choices on the 4 dp grid (#needs-verification-as-design-choice): inline (in a button or row) 18 dp at default and compact, 16 dp at dense, stroke 2 dp; region indicator 40 dp, stroke 4 dp (Material Web circular `active-indicator-width` 4 px, [token file](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-circular-progress-indicator.scss)); linear bar 4 dp high at all densities, full width of the region, `corner-full` ends. The inline sizes equal the button icon sizes ([[Button]]).

## Accessibility

- `busy` true on the waiting node for the whole wait; a progress node has role `progressbar` with `value` as a percentage, or no value when indeterminate (`tess-ui:docs/components/progress-indicators.md`: "a progress bar with its value as a percentage, or as busy when there is none").
- The region's content is not announced while busy.
- The completion message is a polite live region or `window.announce` once ([[14 Accessibility Basics]]).
- Indicator against surface at least 3 to 1 (WCAG 1.4.11).

## Acceptance criteria

- [ ] AC-LOD-1 (scripted input): a wait of 150 ms draws no indicator; a wait of 250 ms draws one that remains for at least 400 ms in total. Pass: indicator visibility equals the timeline within one frame.
- [ ] AC-LOD-2 (AT tree assertion): the waiting node has `busy` true from the first frame of the wait and false in the frame after it ends. Pass: flag equals in both frames.
- [ ] AC-LOD-3 (geometry check): a loading button has the same width and height before, during and after loading (0.5 dp), the spinner replaces the leading icon, and a press during loading raises no activation. Pass: size equal, activation count 0.
- [ ] AC-LOD-4 (geometry check): a skeleton region has the bounds of the content it replaces (0.5 dp); the siblings below move by at most 0.5 dp when content arrives. Pass: offsets at most 0.5 dp.
- [ ] AC-LOD-5 (scripted input): in a wait with a known fraction the bar value never decreases across 20 updates and equals the given value at the end. Pass: sequence non-decreasing.
- [ ] AC-LOD-6 (scripted input): with a simulated clock, a wait of 10 s shows "Still loading" and Cancel; Cancel ends the wait and clears `busy`; a wait of 30 s ends in the error state with Retry. Pass: state at 9.9 s, 10 s, 30 s equals the table.
- [ ] AC-LOD-7 (scripted input): with `reduced_motion` true, an indeterminate indicator shows no animation over 30 frames and the text "Loading" is present. Pass: frames identical.
- [ ] AC-LOD-8 (AT tree assertion): an action of 5 s produces exactly one polite announcement at its end; progress updates produce none beyond every 25 percent. Pass: announcement count equals.
- [ ] AC-LOD-9 (contrast script): the indicator colour against its surface is at least 3 to 1 in light and dark. Pass: ratio at or above 3.
- [ ] AC-LOD-10 (token test): inline indicator 18, 18, 16 dp; region 40 dp; linear 4 dp; colours are role references. Pass: values equal.
- [ ] AC-LOD-11 (scripted input): a region with a region indicator has no second indicator for the same wait in any child. Pass: indicator count 1.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Button_View.tdl` (`Loading`), `tess-ui:src/tess_ui/widgets/progress.py`, `tess-ui:docs/components/progress-indicators.md` | partly meets: `Button` `Loading` spinner and `busy` (AC-LOD-2, AC-LOD-3 meet by reading), determinate and indeterminate indicators, `LoadingIndicator`, still bar under reduced motion (AC-LOD-7 meets by reading); no delay or minimum display (AC-LOD-1 fails), no skeleton (AC-LOD-4 fails), no timeout rule (AC-LOD-6 fails); the config app handles the 10 s `check` timeout in the app |
| tess-shell | `tess-shell:src/tess_shell/shipped/Image/Image_Module.tdl`, ProgressBar module | partly meets: Image `Placeholder` at final size (rule 5 for images); `ProgressBar` honours reduced motion per the shell accessibility note; no busy flag convention, no delay, no timeouts (AC-LOD-1, AC-LOD-2, AC-LOD-6 fail) |
| tre | `tre:docs/reference/node.md` (`busy`) | not applicable: the engine supplies the flag and timers (`window.after`); no indicator or delay |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| 200 ms show delay, 400 ms minimum display, skeleton and timeout rules | MD3 gives no timing rule; desktop waits are mostly short and flashing is a defect | none; design choice |
| Inline indicator 18 dp and 16 dp at dense | matches the button icon size | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Still indicator plus text under reduced motion | WCAG 2.2 SC 2.3.3 is adopted as a MUST | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- [Material Components Android: Progress indicator](https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md) (determinate and indeterminate variants, linear and circular); [Material Web circular progress tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-circular-progress-indicator.scss) (active indicator width 4 px).
- [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), [SC 2.2.1 Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html), [SC 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html); [WAI-ARIA 1.2 `progressbar`, `aria-busy`](https://www.w3.org/TR/wai-aria-1.2/).
- The 200 ms, 400 ms, 10 s and 30 s values and the skeleton rule are not from a source: #needs-verification-as-design-choice.
- Code: `tess-ui:docs/components/progress-indicators.md`; `tre:docs/reference/node.md`; `tess-ui:apps/shell_config/README.md`; [[Gaps and Contradictions]].
