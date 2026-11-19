# Lavish: review and feedback

**One review page per task.** Lavish shows the plan, the filing preview or the verified result. Feedback updates the same page and the same session. Notion holds the task status. The calendar only reserves the review time.

## Prepare the page

Copy [template.html](review-page/template.html), [review.css](review-page/review.css) and [review.js](review-page/review.js) together into the task folder. The template is a neutral version of review page v2 with invented content. It needs no external fonts or assets. If the project already has a design, use that design. The review page follows light and dark mode.

Order: result and status → change → effect with evidence → open items → exactly one decision. Each card has one statement and 40 words maximum. Use three key figures and three open items maximum. If you did not measure an effect, write "not verified". Put the approval and the sources into collapsible sections.

## Open, listen, close

1. Open the page with `lavish-loop open <file>`. For the handover, use the private session URL that the command actually prints. Do not use a guessed address. In Hermes Desktop, open the session in the preview next to the chat. Check the page on desktop and phone, in light and dark mode.
2. In the same turn, start `lavish-loop wait <file>`. In Hermes, run it as a background process with `notify=true` and `persist_on_release=true`. Use `lavish-loop status` to make sure that exactly the correct listener runs. Do not use raw calls to open or poll. Do not share publicly. Do not bypass an existing stop hook.
3. When feedback arrives, read the full content. At the top, show "New in round N" with three "Your feedback / Changed" pairs maximum. Mark changed blocks with `rv-rev` and `data-lavish-revision`. Collapse the old state at the bottom. Update the header and the evidence. Start the listener again for the same session: `lavish-loop wait <file> --reply "<one line>"`.
4. After approval: change the same page into a result view without the old decision controls. Save the approved version and the evidence in the existing task. Close with `lavish-loop done <file> --reply "<one line>"`. Do not start follow-up work automatically.

## Approval limit

- The selection and the note stay local until the user clicks **Send**. Then the template uses the Lavish bridge. Only the receipt by the agent confirms the delivery. Without the bridge, the template shows text to copy and sends nothing.
- Bind the decision to the visible version and the visible scope. When the reviewed content changes, increase `data-rv-revision` and change the name of the selection fields. A plan approval does not start a live change. A filing approval allows only the exact Notion and calendar writes that were shown.
- For remote access, use only a private connection that you set up separately. Check the session URL from the intended environment before you share it. Do not distribute session data, local endpoints or connection data with the template.

**Requirement:** Lavish and `lavish-loop` are installed separately. This repo does not install them and does not change any approvals. You can also open the example page offline. The feedback channel is available only in a real session.
