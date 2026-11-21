---
title: Audit Template
type: template
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [template, audit, adoption]
related: ["[[17 Conformance]]", "[[Test Method]]", "[[Accessibility Rules]]", "[[70 Adoption]]", "[[80 Requests]]", "[[Inventory]]", "[[Plan]]"]
depends_on: ["[[17 Conformance]]", "[[Test Method]]"]
---

# Audit Template

> [!info] Summary
> The skeleton of an audit of one project against one slice of the specifications. Copy the block under "Note skeleton" into a new note named `Audit <project> <slice> <date>` in [[70 Adoption]], fill every cell and delete this paragraph. The rules for results, evidence, levels and routing are in [[17 Conformance]]; the test types are in [[Test Method]]. This note is a template and has no acceptance criteria of its own.

## How to use

1. Name the note `Audit <project> <slice> <date>`, for example `Audit tess-ui Text Field 2026-12-01`. One project and one slice per note; a slice is a list of component or chapter notes.
2. List every acceptance criterion of every note in the slice, one row each, in the order of the notes. Copy the check type the criterion names. No row is omitted.
3. Send the id list to the Orchestrator, who assigns the project bot ([[17 Conformance]], audit workflow). Record the assignment in the header.
4. Fill Result, Evidence, Owner and Issue link from the project bot's return. Write nothing that was not run as `pass`.
5. Write the count and check that the five numbers sum to the number of rows.
6. Update the `Status in code` table of each audited note, linking this audit, in the same pull request.

## Result values

| Result | Required cells |
|---|---|
| pass | Evidence: test name and commit, hand-check id, or screenshot path in the project's repository |
| fail | Evidence of the failing run; Owner; Issue link; a declared deviation adds the project ADR |
| not run | Evidence column holds the reason (no harness, no device, time) |
| not testable | Evidence column holds why and the replacing review with reviewer and date |
| not applicable | Evidence column names the element the project does not draw |

## Columns

| Column | Content |
|---|---|
| AC id | the identifier, for example `AC-BTN-5`; copied exactly |
| Note | the wikilink of the note that holds the criterion |
| Check type | one of the eight types of [[Test Method]] as the criterion names it |
| Result | pass, fail, not run, not testable or not applicable |
| Evidence | see the table above; "looks right" is not evidence |
| Owner | the person or bot who answers for a failing or open row; empty for a pass |
| Issue link | the project's issue for a failing row; a request note [[80 Requests]] for a gap in the engine or toolkit |

## Note skeleton

Copy from the line `---` below to the end of the last table. Replace every text in angle brackets and the example links (`[[Button]]`) with the audited notes.

```markdown
---
title: Audit <project> <slice> <date>
type: audit
status: draft
owner: phil
created: <date>
updated: <date>
tags: [audit]
related: ["[[Button]]"]
depends_on: ["[[Button]]"]
---

# Audit <project> <slice> <date>

> [!info] Summary
> <One sentence: the project, the slice, the level audited (1, 2 or 3), the result counts.>

## Header

| Item | Value |
|---|---|
| Project | <tess-ui, tess-shell or tre> |
| Project commit | <hash> |
| Specification version and vault commit | <version, hash> |
| Level audited | <1, 2 or 3> |
| Scope | <notes audited> |
| Environment | <headless or real compositor, display scale factors, schemes light dark high contrast> |
| Assigned by | <Orchestrator message id and date> |
| Run by | <project bot or person> |
| Date | <date> |

## Results

| AC id | Note | Check type | Result | Evidence | Owner | Issue link |
|---|---|---|---|---|---|---|
| AC-BTN-1 | [[Button]] | geometry check | pass, fail, not run, not testable or not applicable | <test name and commit, hand-check id, screenshot path or reason> | <owner for a non-pass> | <issue or request link> |
| AC-BTN-2 | [[Button]] | token test | | | | |

## Count

| Pass | Fail | Not run | Not testable | Not applicable | Rows |
|---|---|---|---|---|---|
| <n> | <n> | <n> | <n> | <n> | <n, the sum of the five> |

## Declared deviations

| AC id | Project ADR | Reason | Accepted by | Review date |
|---|---|---|---|---|
| <id or none> | <link> | <reason> | <owner through the Orchestrator for a MUST> | <date> |

## Hand checks

| Hand-check id | Steps | Expected | Environment | Observed | Tester | Date |
|---|---|---|---|---|---|---|
| <id or none> | | | | | | |

## Follow-up

- Candidate request notes: <UXREQ ids or none>.
- Status in code tables updated: <list of notes>.
- Delta audit needed for: <AC ids that failed or were not run>.

Back to [[70 Adoption]].
```

## Status in code

Not applicable: a template has no implementation. Audits created from it record status per project.

## Deviations from Material Design 3

Not applicable: the template carries no design rule.

## Sources

- [[Test Method]], section Audit format for `70 Adoption` (columns, rules, the example frontmatter).
- [[17 Conformance]] (result values, evidence, levels, workflow, deviations).
