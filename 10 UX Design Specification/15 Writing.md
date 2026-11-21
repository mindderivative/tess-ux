---
title: 15 Writing
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, writing, ux-writing, microcopy]
related: ["[[01 Principles and Scope]]", "[[11 Interaction]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[17 Conformance]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Glossary]]", "[[Button]]", "[[Icon Button]]", "[[Switch]]", "[[Text Field]]", "[[Form Row]]", "[[Tooltip]]", "[[Dialog]]", "[[Menu]]", "[[List]]", "[[Tree]]", "[[Accordion]]", "[[Typography]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0004 Tooltip rule]]"]
depends_on: ["[[01 Principles and Scope]]", "[[14 Accessibility Basics]]"]
---

# 15 Writing

> [!info] Summary
> The rules for the words in the interface: labels, buttons, menu items, titles, tooltips, helper text, placeholders, errors, confirmations, empty states, numbers and shortcut hints. Each rule is a number or a pattern a string scan or a reviewer can pass or fail. The conventions come from the ux-writing skill of the Tesserae vaults (four quality standards: purposeful, concise, conversational, clear) and from the strings the config app already ships.

## Scope

Covers every string a person reads or a screen reader speaks in an application that follows these specifications. Visual typography is in [[Typography]]; how text overflows is in [[10 Layout Overflow and Scrolling]]; when a tooltip shows is in [[Tooltip]] and [[12 Overlays]]. This chapter says what the text says and how it is written.

Evidence: the `Label`, `Placeholder` and message strings of the config app (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, `tess-ui:apps/shell_config/src/tess_shell_config/`), the finding format of its Problems area (an icon and a word, the place, the message and what to write instead, `tess-ui:apps/shell_config/README.md`), the shell's validation messages (`shell-vault:40 Specifications/Runtime/Validation and Errors.md`) and the ux-writing skill (`shell-vault:.claude/skills/ux-writing/SKILL.md`).

## The four standards

| Standard | Test a reviewer applies |
|---|---|
| Purposeful | the text helps the person do or understand the task at this point; removing it would lose information |
| Concise | the fewest words that keep the meaning; no filler such as "please note that", "in order to" |
| Conversational | said aloud it sounds like a person; active voice; plain words |
| Clear | one meaning; the same word for the same thing everywhere ([[Glossary]]) |

## Voice and tone

- Plain, direct and calm. Second person ("you") only where the sentence needs an actor; most labels need none.
- Active voice; present tense for state ("The file changed on disk"), past tense for a result ("Changes saved", not "Changes have been saved").
- No exclamation marks, no humour in errors, no apology filler ("Oops", "Sorry"), no blame ("You entered an invalid value").
- Reading level: plain language of about 7th to 8th grade for general text, 9th to 10th for professional tools such as the config app (ux-writing skill benchmark).
- Technical words are allowed where the audience uses them (block, module, surface, stylesheet) and each has one spelling, taken from [[Glossary]].

## Capitalisation

- Sentence case for all interface text: labels, buttons, menu items, tabs, titles, headings, tooltips, placeholders, helper text. Only the first word and proper nouns capitalise: "Apply as I edit", "Format file", "Reload shell", "Keep mine" (all shipped in the config app).
- Proper nouns, product names, acronyms and key names keep their form: Tesserae, KWin, PDF, `Ctrl+Shift+N`.
- A button that names a page keeps the page's own capitalisation: "Open Structure".
- All caps only for acronyms and for an overline label of at most 3 words (type role `label_small`); never for prose, buttons, errors or titles.
- This differs from the ux-writing skill, which sets title case for page titles, dialog titles, navigation items and field labels; the vault takes sentence case everywhere because every shipped string already does and Material Design components use sentence case in their sources #needs-verification. Recorded in Deviations below.

## Punctuation

- A text that is a complete sentence ends with a full stop. A fragment does not. Labels, button text, menu items, tabs, chips, column headers, titles, one-phrase tooltips and placeholders are fragments and have no trailing full stop.
- Helper text, error messages, confirmation text and empty-state text are sentences and end with a full stop on each sentence.
- No exclamation marks anywhere. No trailing colon on a field label (the layout separates label and control).
- The ellipsis character `…` (U+2026), never three full stops, ends a menu item or button that opens a dialog needing more input ("Save as…"). It is not used for progress ("Loading…" is not used; show the progress indicator and the word "Loading").
- A shortcut hint goes in parentheses at the end of a tooltip: "Remove the block (Delete)", written with `+` between keys and capitalised key names ([[11 Interaction]]).
- A user-supplied name in a message is set in plain quotation marks when it could be confused with the sentence: Cannot rename "layout.tdl".
- Lists of items in a sentence use a comma and no serial "and" ambiguity; avoid slashes ("and/or").

## Length limits

Limits are characters of the source string (not bytes) and are checked by a string scan; a string over the limit is a defect or carries a recorded reason.

| String | Target | Hard limit | Basis |
|---|---|---|---|
| Button, menu item, tab, chip label | 2 to 4 words, 15 to 25 characters | 30 characters | ux-writing benchmark (buttons 15 to 25 characters, 6 words) |
| Switch, checkbox, radio label | 3 to 6 words | 50 characters | design choice |
| Field label ([[Form Row]], [[Text Field]]) | noun phrase of 1 to 4 words | 40 characters; wraps at most 2 lines then ellipsis ([[Form Row]]) | Form Row |
| Title (page, dialog headline, panel) | 3 to 6 words | 40 characters | ux-writing benchmark |
| Plain tooltip ([[Tooltip]]) | 1 phrase | 60 characters (about 3 lines at the 200 dp maximum width) | design choice |
| Rich tooltip subhead, supporting text | subhead 1 phrase; text 1 or 2 sentences | 40 and 140 characters | design choice |
| Placeholder | an example value | 40 characters | design choice |
| Helper text | 1 sentence | 80 characters; wraps at most 2 lines ([[Text Field]]) | Text Field |
| Error message | what, why, what to do | 120 characters (12 to 18 words) | ux-writing benchmark |
| Empty-state text | 1 or 2 sentences | 140 characters | design choice |
| Status or success message | 2 to 6 words | 40 characters | design choice |
| Accessible name | the visible label | the visible label plus at most a shortcut hint | [[14 Accessibility Basics]] |

Sentences in running text: 8 to 14 words, never more than 25 (ux-writing benchmark: 8 words or fewer, 100 percent comprehension; 14 words or fewer, 90 percent).

## Labels and buttons

- A button is `[Verb] [object]` in the imperative: "Save changes", "Delete file", "Add a child block". The verb is specific: "Delete" when the data is destroyed, "Remove" when it can be undone or goes to the trash (the config app's "Remove the block" can be undone; "Delete the file" moves the file to the trash folder, which its own tooltip states).
- Banned as the whole label: "OK", "Submit", "Click here", "Yes", "No", "Done", "Continue" without an object, "Next" without a context ("Next" is allowed in a numbered flow). Dialog actions state the result: "Delete file" and "Cancel", not "Yes" and "No" ([[Dialog]]).
- A cancel action is "Cancel" or "Close"; a dismissive action never uses the same verb as the confirming action.
- An icon-only control has a name and a tooltip with the same text ([[Icon Button]], [[14 Accessibility Basics]]); the text is a verb phrase for an action ("Add a child block") and a noun phrase for a toggle of a state ("Apply as I edit").
- A label is the same everywhere for the same action: the button, its menu item, its tooltip and its accessible name carry one string with at most a shortcut hint added.
- Links say where they go ("Read the keyboard guide"), never "here".

## Titles and headings

- A noun phrase that orients: "Structure", "Problems", "Tesserae Shell configuration" (product names keep their capitals).
- A dialog headline is the question or the action at stake and states the object: "Delete layout.tdl?" or "Reload changed file"; supporting text gives the consequence ([[Dialog]]).
- No full stop; question marks only on a real question.

## Form fields

- The label is a visible noun phrase naming what is entered ("Email address", "Corner radius"). A placeholder is never the label ([[Text Field]], WCAG 2.2 SC 3.3.2).
- A placeholder is an example of a valid value, short and in the form the field accepts ("name@example.com", "Search applications"). It is never an instruction, never required information and never the only cue of a unit; the unit is a suffix beside the value (the config app puts the unit as a suffix).
- Helper text says what to enter or why it is needed, before an error occurs, in one sentence, verb first where it instructs ("Use letters, digits and underscores").
- A required or modified marker is a short word in the label column ("required", "modified by file", `label_small`), never only a colour or an asterisk without a legend.
- Units: a number field shows its unit; durations and sizes use the symbol ("200 ms", "16 dp").

## Error messages

Every error message answers three questions in this order: what happened, why when it is known, what to do now. Pattern (ux-writing skill): `[What failed]. [Why]. [What to do].`

| Type | Pattern | Example |
|---|---|---|
| Inline validation | `[Field] must ...` or `Use ...`; names the rule, not the person | "Name must start with a letter. Use letters, digits and underscores." |
| Value out of range | states the range; the typed text stays | "Enter a number from 0 to 100." |
| Action failed | `Cannot [action]. [Cause]. [Recovery].` | "Cannot save layout.tdl. The folder is read-only. Choose another folder and try again." |
| Nothing changed | says what is safe | "The old file is unchanged." |
| Blocking | what is blocked, why, the one action that fixes it | "Shell not found. Install the tesserae-shell command and start again." |

Rules:

- No codes alone ("Error 403"), no stack text, no blame words ("invalid", "illegal", "wrong", "bad", "you must"), no "Something went wrong", no "An error has occurred".
- Name the object the person touched ("layout.tdl", the field's label); a message without the object is a defect.
- The cause is the real cause in the user's words; the system error text follows only when it helps ("Permission denied").
- Every error offers a recovery step or says that nothing was lost; a message with neither is a dead end.
- A message that carries a place and a fix is formatted `file:line:column`, the message, then what to write instead (the Problems area of the config app).
- Severity is a word and an icon, not only a colour: "Error", "Warning", "Note" ([[14 Accessibility Basics]]). Words: Error blocks, Warning may cause trouble, Note informs.
- Error text is announced once through a polite live region and is the field's description while it shows ([[14 Accessibility Basics]]).
- Strings are never built by joining fragments in code for one sentence; messages have named placeholders so that word order can change.

Current shell config strings that already meet the pattern: "Cannot save {path}: {reason}. The old file is unchanged." (what, why, safety) and "Moved {file} to the trash folder: {path}. It is not removed." (result and safety); some messages lack the recovery step ("Cannot read {file}: {error}") and are the first candidates for the audit (`tess-ui:apps/shell_config/src/tess_shell_config/`).

## Confirmations and destructive actions

- The headline states the object and the action; the body states the consequence in one sentence and whether it can be undone ("You will lose unsaved changes. This cannot be undone.").
- The confirming button repeats the verb and the object ("Delete file"); the other is "Cancel". The destructive action is not the default focused one ([[Dialog]] AC-DLG-6).
- An action that can be undone does not ask; it succeeds and offers undo ([[Dialog]]; config app: delete moves to a trash folder and a rename keeps the old file there).

## Success and status messages

- Past tense, specific, short: "Changes saved", "File moved to the trash folder".
- Proportional: routine actions show no message beyond the changed state; the long action announces its end ([[14 Accessibility Basics]]).
- Status lines are facts without verbs of feeling: "Shell: running (Top_Bar shown)".

## Empty states

- Say why it is empty or what belongs here, then offer the next step: "No findings. Press F5 to run check." One or two sentences (`List` AC-LST-09 and `Tree` AC-TRE-16 test the text exists and is centred).
- Three kinds, three texts: first use ("No files yet. Create one with New."), cleared by the user ("All findings cleared."), no results ("No matches for "gap". Check the spelling or clear the search.").
- The text names the action using the same label as the control ([[Button]]).

## Tooltips

- A tooltip repeats or adds to the visible label; it never holds the only information ([[ADR-0004 Tooltip rule]], [[Tooltip]] AC-TIP-20).
- Icon-only control: the tooltip is the control's name (verb phrase, sentence case, no full stop), with the shortcut hint in parentheses.
- Labelled control: the tooltip adds the longer description, as a fragment or one sentence.
- No "Click to ...", "Press to ..." or "This button ..."; the role is already announced.
- A tooltip that explains disabled state names the reason ("Save is off: no changes yet") only where the control opts in ([[Tooltip]]).

## Numbers, dates and units

- Numerals, not words: "3 findings", "12 files".
- Dates spell the month: "21 November 2026" or "November 21, 2026"; never "21/11/2026". A project chooses one order and uses it everywhere. No ordinal suffixes. Times use the 24-hour or the 12-hour form of the user's locale.
- A number and its unit are separated by a non-breaking space (U+00A0): "200 ms", "16 dp". Ranges use an en dash without spaces: "2015–2016" (the ux-writing skill writes a hyphen; the vault prefers the dash #needs-verification-as-design-choice).
- Plural forms come from the count: "1 finding", "2 findings"; a message does not write "(s)".

## Localisation and inclusion

- Strings live in one place per project, not inside layout code; a message is one string with named placeholders, never assembled from fragments.
- Layout assumes longer text: a label that is 30 percent longer still ends in an ellipsis or wraps and never overflows its container (chapter 10, [[10 Layout Overflow and Scrolling]]) #needs-verification-as-design-choice.
- No idioms, sports or cultural metaphors, ableist or gendered wording ("sanity check", "master", "blacklist"); prefer "check", "primary", "blocklist".
- Left-to-right assumptions (arrows in words such as "see the table on the right") are avoided; use names.

## Accessibility of text

- The accessible name begins with the visible label text (WCAG 2.2 SC 2.5.3); added shortcut hints follow it.
- Do not use all caps in strings (a screen reader may spell it); the overline style uppercases by rendering, not in the string #needs-verification.
- Link and button text makes sense out of context ("Read the keyboard guide", not "Read more").
- Status messages use polite announcements and are short enough to hear once ([[14 Accessibility Basics]]).

## Status in code

| Project | Where | Status |
|---|---|---|
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` and its strings | Partly meets. Sentence case and no trailing full stop on labels hold (about 35 labels read: "Format file", "Keep mine", "Apply as I edit"); labels carry the shortcut in parentheses as the accessible name; messages follow what and why, some lack the recovery step (AC-WRT-8, AC-WRT-9); the toolkit has no string lint and no length limits; empty-state text exists for `SearchView` and trees through a slot, not tested. |
| tess-shell | `shell-vault:40 Specifications/Runtime/Validation and Errors.md`, `tess-shell:src/tess_shell/shipped/Applications/` (placeholder "Search applications") | Partly meets. Validation messages name the nearest valid name (`difflib` suggestions), which supports the "what to do" rule; the placeholder is an example phrase; no string lint; no length limits checked. Not otherwise audited. |
| tre | `tre:docs/` | Not applicable. The engine holds no interface strings except its documentation and error texts for developers; those are outside this chapter. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Sentence case for titles and dialog headlines where the ux-writing skill sets title case | every shipped string uses sentence case; one rule is easier to lint | none; recorded here and in [[Deviations from MD3]] #needs-verification-as-design-choice |
| Hard character limits on labels, tooltips and messages | testable rule; Material Design gives guidance, not limits | none; design choice |
| Keyboard shortcut hint in the tooltip and label | desktop keyboard-first use ([[11 Interaction]]) | none |
| Material Design writing guidance for components is script-rendered and not read by tools | the rules above come from the ux-writing skill, WCAG and project strings | #needs-verification |

## Acceptance criteria

Check type "token test" here means a string scan over the strings in the project's views, stylesheets and message tables (the same kind of read as other token tests); a project may implement the scan as a lint script.

- [ ] AC-WRT-1 (token test, string scan): no label, button text, menu item text, tab text, chip text, title, placeholder or one-phrase tooltip ends with a full stop. Pass: zero strings in those fields end with `.`.
- [ ] AC-WRT-2 (token test, string scan): sentence case. For every label, button, menu item, tab, title and tooltip string, the second and later words are lower case unless the word is on the project's proper-noun and acronym list. Pass: zero violations; the list is in the audit.
- [ ] AC-WRT-3 (token test, string scan): no string contains an exclamation mark, three consecutive full stops, "Oops", "Sorry", "Something went wrong" or "An error has occurred". Pass: zero matches.
- [ ] AC-WRT-4 (token test, string scan): button, menu item, tab and chip labels are at most 30 characters; titles at most 40; plain tooltips at most 60; placeholders at most 40; helper text at most 80; error messages at most 120; empty-state text at most 140. Pass: zero over the limit, or each exception listed in the audit with a reason.
- [ ] AC-WRT-5 (token test, string scan): no button or dialog action label equals "OK", "Submit", "Click here", "Yes", "No" or "Done" (case-insensitive, whole label). Pass: zero matches.
- [ ] AC-WRT-6 (token test, string scan): a label ending in `…` opens a dialog or picker that needs more input; no string contains `...`. Pass: reviewer confirms each `…` item; scan finds zero `...`.
- [ ] AC-WRT-7 (AT tree assertion): for each icon-only control the accessible name equals the tooltip text, ignoring a trailing shortcut hint in parentheses, and starts with the visible label text where one exists. Pass: zero mismatches in the tree walk of each documented view.
- [ ] AC-WRT-8 (review): error messages. Every error message in the project's message table names the object, says what happened, and gives a recovery step or states that nothing was lost. Pass: reviewer sheet complete; messages failing any of the three are listed as defects.
- [ ] AC-WRT-9 (token test, string scan): no error message matches the banned list "invalid", "illegal", "wrong", "bad input", "you must", or consists only of a code or number. Pass: zero matches.
- [ ] AC-WRT-10 (AT tree assertion): a field with an error has the error text as its description, `invalid` true, and the text is announced once through a polite live region; the same text is visible within 0.5 s. Pass: description equals text; announcement count 1.
- [ ] AC-WRT-11 (review): a placeholder is never the only label: every text field has a visible label or an accessible name that is not the placeholder. Pass: zero fields fail (tess-shell `TextInput` uses `Placeholder` as the name when no label exists; an audit records it as a deviation, not a pass).
- [ ] AC-WRT-12 (token test, string scan): a shortcut hint in a string matches `\(([A-Z][A-Za-z0-9]*)(\+[A-Z][A-Za-z0-9]*)*\)$` (capitalised key names joined by `+`, in parentheses at the end). Pass: zero hints that do not match.
- [ ] AC-WRT-13 (review): the same action has one label string across its button, menu item, tooltip and accessible name, apart from a shortcut hint. Pass: reviewer finds zero conflicts in the documented views.
- [ ] AC-WRT-14 (token test, string scan): no message is built from concatenated fragments: every message template has named placeholders and no literal sentence is split across two strings. Pass: reviewer script finds zero templates ending or starting mid-sentence.
- [ ] AC-WRT-15 (review): an empty state of each list, tree and search shows a reason and a next step in one or two sentences; no empty area shows no text. Pass: every documented view checked.
- [ ] AC-WRT-16 (token test, string scan): dates contain no all-numeric day and month forms ("21/11/2026") and no ordinal suffixes; a number followed by a unit uses U+00A0 between them. Pass: zero matches.
- [ ] AC-WRT-17 (geometry check): a label string lengthened by 30 percent in the longest supported language is clipped by no container: it ends in an ellipsis or wraps, and its bounding box lies inside the container ([[10 Layout Overflow and Scrolling]] AC-LAY-1). Pass: zero overflow measured #needs-verification-as-design-choice.

## Sources

- ux-writing skill: `shell-vault:.claude/skills/ux-writing/SKILL.md` (four standards, patterns for buttons, errors, empty states, form fields, benchmarks for lengths and sentence length, capitalisation, numbers and dates, tense).
- Strings and shortcuts: `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, `tess-ui:apps/shell_config/README.md` (Problems format); tess-shell strings: `shell-vault:40 Specifications/Runtime/Validation and Errors.md`, `shell-vault:40 Specifications/Modules/Applications Module.md`.
- WCAG 2.2: SC 2.5.3 Label in Name, SC 3.3.1 Error Identification, SC 3.3.2 Labels or Instructions, SC 3.3.3 Error Suggestion, SC 4.1.3 Status Messages (`https://www.w3.org/TR/WCAG22/`; names checked in the fetched page, anchors not separately fetched).
- Material Design 3 writing guidance: not readable by tools #needs-verification. Material Web component demos are the visible sentence-case reference #needs-verification.
- Limits not in the skill (tooltip, placeholder, helper, empty state, status) are Tesserae design choices #needs-verification-as-design-choice.
