# Calendar review slots

**One calendar block per task.** Suggest a slot when the work takes an estimated 30 minutes or when it has a review page. Change the calendar only after explicit approval. The task status stays in Notion.

## Suggest

1. Estimate the finish time, including worker time and verification time. The review starts 15 minutes after that at the earliest. It never starts in the past.
2. Check the relevant calendars only for busy/free. Also subtract the still-valid suggestions of other open runs. Do not count expired suggestions as busy.
3. Take the first start that fits on the 15-minute grid: `08:00–20:00` in `Europe/Berlin`, 20 minutes of review plus 10 minutes of free buffer after it. Search up to three days, including the start day. The buffer is not a second event.
4. If no slot fits, ask for a different day. Before each booking, show the title, start, end, time zone, calendar, visibility, availability, attendees and description. Mark the slot as **suggested, not booked**.

## After approval

- Check availability again directly before you write. If the slot is busy or expired, first show a new suggestion. Do not reschedule silently.
- Book `Review: <result title>` in the primary calendar, private and busy, with no invitations and no notifications. Refer to the task only if the calendar has the correct visibility for it.
- Read back the saved event. Check the calendar, title, time, visibility and attendees. On a retry, use the same event. Do not make a duplicate.
- If the result comes later, move the same event after approval. If the user accepts the result earlier, do not delete the event silently. Deletion needs its own approval.

## Check locally

[review-policy.json](review-policy.json) contains the values to port. The pure calculation module `review_slots.py` gets free time windows and held intervals as input. It does not access calendars, the network or profiles. It does not replace the server-side free/busy query. It does not replace additional capacity rules of the target installation.

```sh
python3 -B calendar/test_review_slots.py
```
