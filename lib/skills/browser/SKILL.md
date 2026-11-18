---
name: browser
description: Control the user's existing browser, reusing its signed-in session and tabs. Use when a task requires the user's browser rather than a separate automated browser session.
---

# Browser

Read [the headless skill](../headless/SKILL.md) for all implementation details, including tooling, runtime, connection setup, browsing, and verification. Attach to the user's existing browser instead of launching a separate session.

Use the connection supplied by the user or environment. Select the existing tab relevant to the task and reuse its signed-in session. If attachment fails or the expected session is unavailable, report the blocker; do not silently substitute a fresh browser or restart the user's browser.

Keep the session available for follow-up work. When disconnecting is requested, leave the user's browser and existing tabs running. Close a task-created tab only when it is no longer needed and the user does not need its result.
