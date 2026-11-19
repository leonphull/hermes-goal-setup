---
name: goal-prompt-compiler
description: Turn raw requests into verifiable Goal prompts.
license: MIT
---

# Goal prompt compiler

Use these instructions for Goal mode, worker prompts and raw requests with more than one part. Write an executable task, not a list of vague intentions. **Goal → current state → bridge.** First prove one small, complete run. Then scale.

## The five questions

| Keyword | Question |
| --- | --- |
| End | How do we know that it is done? |
| Limit | What must the agent not do? What needs approval? |
| Access | Which tools, sources and permissions does the agent need? |
| Split | Which parts have their own results or approvals? |
| Stall | When does the agent continue, and when does it stop? |

"Done when" and "Definition of Done" are the same field. Write three to seven verifiable criteria if the scope needs them. For each criterion, name the evidence: a file, a verifiable count, a test, a URL or a read-back state. A deadline is not an acceptance criterion.

## Task gate

- **Quick question:** Answer directly. Do not make a task record or a review slot.
- **Clear task:** Repeat the goal and the checkpoint in one line. Then start the safe work. If the user ordered only a prompt, deliver the prompt and do not start the task.
- **Large or unclear:** Read first. If the work takes more than one session or has more than three independent subtasks, give a plan for approval. Deliver a short brief: `Goal · Done when · Do not · Access · Report`. Ask only about decisions that change the result, the risk or the approval.

## Compile and execute

1. **Check what exists.** First, search for a matching task, project and existing artifacts. Before you write a task brief, also check the available sessions of the last 14 days. If a run exists, continue from the last verified point. Keep draft, verified and published separate.
2. **Test access first.** Name the permitted tools, the authoritative sources, the necessary permissions and the method for self-verification. If something important is missing, make the clarification the first subgoal, or define a small pilot case. Summarize real blockers.
3. **Split the work.** Give each independent part its own result, a write scope and a checkpoint. Name dependencies. For parallel work, the main agent merges the results and resolves conflicts.
4. **Set limits.** Keep money, sending, publishing, deletion and risky live changes behind a specific approval. Verify internal work without such side effects. Mark assumptions and optional integrations separately from hard blockers.
5. **Save progress.** After each phase, record `done / verified / open / blocker / next step`. Do not restart a stopped run blindly. Before a retry, check if a change already arrived.
6. **Accept.** Verify real results, not only worker statements. Repeat `verify → correct → verify` only as often as you set in advance. Report `done` or `blocked` one time, then `criterion · evidence · status`. For a real blocker, name exactly the missing decision or prerequisite.

Start with [GOAL-PROMPT.md](GOAL-PROMPT.md). For long-running or recurring work, also name the execution limit, the state store and the escalation threshold. The task for the worker contains the necessary context, not the full chat history.
