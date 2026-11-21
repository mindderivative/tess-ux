---
title: Vault Lint
type: quality
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [quality, tooling]
related: ["[[60 Quality]]", "[[Test Method]]", "[[Accessibility Rules]]", "[[Colour Roles]]"]
depends_on: ["[[Test Method]]"]
---

# Vault Lint

> [!info] Summary
> Two standard-library Python scripts in `tools/` check the vault mechanically: `lint_vault.py` (structure, links, acceptance criteria, tokens, markdown rules, privacy) and `contrast_check.py` (WCAG 2.2 ratios stated in the notes). Both exit with code 1 on errors, so they run before every commit and in CI.

## Running

```text
python3 tools/lint_vault.py [vault root]
python3 tools/lint_vault.py [vault root] --json
python3 tools/contrast_check.py [vault root]
python3 tools/contrast_check.py [vault root] --json
```

- The vault root defaults to the parent of `tools/`. Python 3.9 or later; no packages.
- The text report groups findings by check and prints `SEVERITY file:line: message`, then a summary table per check. `--json` prints the same findings as one JSON document for scripts.
- Exit code 0: no errors (warnings and info lines do not fail). Exit code 1: at least one error. Exit code 2: the root is not a folder.
- Scope: every `.md` file below the numbered folders. Files at the repository root, `_templates`, `tools` and hidden folders are not notes. The scripts never write to the vault.

## Severities

| Severity | Meaning | Effect on exit code |
|---|---|---|
| error | breaks a hard rule of the vault or a testable claim | exit 1 |
| warn | inconsistent or suspicious but not provably wrong | none |
| info | a count or list for the maintainer | none |

## Checks of lint_vault.py

| Id | Check | Severity |
|---|---|---|
| FM | Every note starts with a frontmatter block holding `title`, `type`, `status`, `owner`, `created`, `updated`, `tags`, `related`, `depends_on`, all keys in lowercase. `status` is one of `draft`, `proposed`, `accepted`, `stable`, `superseded`, `research`; `type` is one of the types in use (`adr`, `audit`, `chapter`, `component`, `dashboard`, `foundation`, `glossary`, `index`, `inventory`, `pattern`, `plan`, `quality`, `questions`, `register`, `request`, `research`, `template`, `tokens`). A date that is not `YYYY-MM-DD` is a warning. | error |
| LINK | Every wikilink (body and frontmatter, not code) resolves to a note by file name, `title` or an `aliases` entry; a link that matches only ignoring case is a warning. | error |
| ORPHAN | Every note is linked from at least one other note. Every folder holds an index note named after it (`00 Home` may use `Home`). | error |
| COMP | A note of type `component` under `30 Component Specifications` (not the Inventory, not the folder index) has every `##` section of `_templates/Component.md`, in the template order. | error |
| AC | Acceptance-criteria rules, listed below. | error, one warning |
| TOKEN | `scrollbar.*` and `density.*` names in code spans exist in the foundation notes (error). A colour-role-shaped name such as `on_surface_variant` that does not occur in `20 Foundations and Tokens` is a warning. Tokens defined only in the Scrollbar component note are accepted and reported once as a warning. | error, warn |
| MD | No emoji or pictograph (a check mark or cross symbol is a warning); no bold or italic marker touching a code span; no raw HTML tag outside code (angle-bracket placeholders such as a label name in prose count as HTML and go in a code span). | error |
| PRIV | No absolute path under a user's home folder (Linux, macOS or Windows), and no secret-shaped string (key prefixes, private-key headers, `password = ...`). The repository is public. | error |
| NV | Counts every needs-verification tag (the hash-prefixed marker) and lists each note that carries one. | info |

## Acceptance criteria rules (check AC)

- A criterion is a task-list line `- [ ] AC-<PREFIX>-<n>` where `<PREFIX>` is upper-case letters and digits, optionally with hyphen groups (for example a module prefix with two groups), and `<n>` is a decimal number. A ticked box is a warning.
- The line names a check type from [[Test Method]] right after the id, either in parentheses or after a colon: token test, geometry check, pixel check, contrast script, scripted input, AT tree assertion, review. A second type may follow. Any other label is an error.
- The line states a pass condition: after the check type, at least 30 characters that state the assertion (the criterion is itself the assertion; a "Pass:" clause is optional).
- Ids are unique across the vault.
- Numbers are consecutive from 1 per prefix per note, in order of appearance.
- Every id cited anywhere (pattern `AC-` followed by prefix and number) is defined by a criterion line. A citation that differs from the definition only in zero padding is a warning.

## Checks of contrast_check.py

| Section | What is recomputed | Error when |
|---|---|---|
| pairs | Every row of the required-pairs tables in [[Colour Roles]] in the six schemes (light, dark at standard, medium, high), using the hex tables of the same note. Also the stated 1.62 and 1.99 of `outline_variant`. | the stated ratio differs by more than 0.05, or a text pair is below 4.5 (7 at the high level) or a non-text pair below 3 |
| shell | The measured shell pairs (Dark, Light, High_Contrast) from the shell role table. A value written as inherits takes the Dark value and downgrades the finding to a warning. | same limits (4.5 text, 3 non-text) |
| notes-stated | Lines with a pair written as role `on`, `over` or `against` role and a stated ratio (`N:1` or `N to 1`, tagged light or dark). A shell role pair is accepted when the shell hex values reproduce the number. | the stated ratio differs by more than 0.05 |
| notes-limit | The same pairs with a limit (at least N to 1), compared with the light and dark standard values. | the computed ratio is below the limit |
| thumb | The scrollbar thumb, `on_surface_variant` at the rest opacity 0.70 (ADR-0012) over each surface role, in light and dark at the standard and high levels; compared with the 5.85 and 3.96 stated in the Scrollbar note. | below 3.0 or differs from the stated values |
| scrim | The caption band, `scrim` at 0.60, with the caption text colour taken as white (the role name ADR-0016 uses for it is not defined in Colour Roles), over a white, mid-grey and black picture; stated 5.7 over white. | below 4.5 |
| focus-ring | `secondary` over each surface role in all six schemes; stated about 6 (light) and 10.9 (dark) over `surface`. | below 3.0 |

- Alpha colours are composited over their background in sRGB before the ratio is computed, as the contrast script of [[Test Method]] specifies.
- The ratio is the WCAG 2.2 formula (L1 + 0.05) divided by (L2 + 0.05) with sRGB relative luminance.
- Pairs written in prose without code-span role names are not read; the script reports how many pairs and stated ratios it compared.

## Known violations

`tools/known_violations.json` lists spec-documented violations by a project (fields: project, ac, section, match, tracked, reason). The contrast check reports a matching error as a warning that names the project and its worklist id, so the tool is green on the specification and still lists the project debt. An entry that no longer matches any error is itself reported as a warning and is removed. The current entry is the tess-shell `accent` colour on `surface` in the dark scheme (TSH-043, AC-COL-3).

## Use

- Run both scripts before a commit that touches notes; fix errors, review warnings.
- The scripts are the machine check behind acceptance criterion AC-PRI-1 (sections present) and the style rules of the vault; they do not replace review of content.
- Raw reports are not stored in the vault; they change with every edit.
