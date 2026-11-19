# Subagent routing

**The main agent decides and verifies.** Each worker gets one limited task. Do not start a subagent for a single read tool, for simple mechanical work or for a task that needs a direct question to the user. Independent, reasoning-heavy or large parts can run in parallel.

| Option | Task |
| --- | --- |
| `claude` | Default: research, reading, writing and extraction. |
| `claude-deep` | Hard decisions, architecture, complex debugging or a second review. |
| `codex` | Code, repositories, tests and terminal-heavy work. |
| `glm` | Repeated, simple processing and many items of the same type. |
| `local` | Material that must not leave your own infrastructure. No cloud fallback. |

## Contract per worker

- Give the goal, the current state, the permitted sources, the write scope, the limits, the result format and the checkpoint. Do not give the raw chat. Do not give a general approval.
- Keep parts that can be done independently separate. For the same file or the same checkout, use one writing worker. State dependencies and order explicitly.
- Require `done` or `blocked` with the artifact, the evidence and any open limitation. Release the result only after your own check. A worker report alone does not prove an external change.
- Use temporary subagents for one limited run. Use a persistent worker or a queue only for a recurring responsibility, for necessary isolation or for work that must continue after the session ends.

## Setup

[delegation.example.yaml](delegation.example.yaml) is a configuration excerpt for the Hermes backend mode `model_map`. This mode needs the plugin `advanced-delegation`. The public model label is not the same as the model of the main session. The placeholders for installed adapters and for the local endpoint cannot resolve. This is intentional.

Copy only the routes whose adapters you set up in the target profile. Check the visible `option` values in a fresh session. Give each approved route a harmless test task. Test `local` without cloud fallback. If this route is not available, stop when the material is private. Also check additional tools for external data transfer. A local model alone does not prevent it.

In the base mode `default`, workers cannot select an option from this map. They start on the pinned delegation route, or they inherit the route of the main agent. A separate profile backend mode gives profile boundaries. It does not automatically give more compute capacity.
