# Dry run: check an example file

This example uses invented data. It connects no service and books no event.

**Raw input:** "Turn my duplicated example table into a verified list and plan 20 minutes for the review."

1. **Compiler:** The goal is a local CSV from six synthetic rows. Done when five unique rows remain and the test reports exactly one duplicate. The source stays unchanged. No sending and no live writes.
2. **Routing:** For this small, mechanical test, work directly. If a separate parser becomes necessary later, `codex` can deliver the parser. The main agent verifies its output itself.
3. **Notion preview:** Title "Five unique example rows verified" in the existing "Test project". The page content contains the purpose, three steps and the verification evidence. Write nothing.
4. **Calendar preview:** If the work is done at 10:08, the earliest start is 10:23. With a free window from 10:00 to 11:00, the grid gives `10:30–10:50`, with free buffer until 11:00. Private and busy in the primary calendar, no attendees, not booked yet.
5. **Lavish and handback:** The [example review page](../lavish/review-page/template.html) shows the result, the evidence and the approval. Offline, **Send** gives only text to copy. BLUF after a real run: "Done: The CSV contains five unique rows. The test found one duplicate."
