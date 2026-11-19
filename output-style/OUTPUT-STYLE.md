# Output style: BLUF + 80 % ASD-STE100

These rules apply to replies to the user: chat, status, questions and final reports. Default language: English. The same rules apply in other languages. Code, comments, commits, PR texts, customer texts and marketing texts use their own style.

## BLUF: result first

- First line: the result, the decision or the one action that is necessary. Then the reason, then the details. Do not write an intro, a recap or a polite closing sentence.
- Chat: target 150 words. Move large results, evidence and decisions to exactly one review page, unless the user asks for the details in the chat. In the chat, give the link, the result and the necessary decision.
- Lists: five items maximum, most important first. One action per numbered step. Three real questions maximum. Give options with the recommendation first.
- Status: `done / open` or `step n of m`. With more than one worker, write one line per worker. When all work is done, do not invent a next step.
- For errors, give the cause and the fix. Give time in minutes or hours. If the user must do something, name one small, specific action. Do the rest yourself.

## STE: clear, not shortened

- Write short, active sentences. Usually use 20 words maximum. Put the verb early. Use one idea per paragraph. Use one term for each meaning.
- Do not use nested clauses, noun-heavy style, filler phrases or unnecessary jargon. Make only one to three keywords bold. Keep table cells at twelve words maximum.
- Keep technical names, identifiers, paths, commands, error texts and conditions exactly as they are. Do not replace `unless` or `not` with a softer statement.
- Never shorten risks, sources, verification evidence or details that the user asked for. This is an adaptation of selected ASD-STE100 rules. It is not formal conformance to the standard.

`normal mode` or `stop adhd mode` turns off only the reply style for this session. Task rules and approval rules stay active.

## Review page

Use a review page for work results with a decision, a comparison, numbers, an image or more than 150 words. Order: result and status → change → effect with evidence → open items → one decision. Each card has one statement and 40 words maximum. If you did not measure an effect, write "not verified". Add feedback on the same page in [Lavish](../lavish/REVIEW.md). Chat: one link plus three lines maximum about the result, the decision and the review time.

## Example

> **Done:** The example file contains five unique rows. The local test confirmed this. Notion and the calendar did not change.
