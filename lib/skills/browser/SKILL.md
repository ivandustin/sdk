---
name: browser
description: Control the user's existing browser, reusing its signed-in session and tabs. Use when a task requires the user's browser rather than a separate automated browser session.
---

# Browser

Read [the headless skill](../headless/SKILL.md) for all implementation details, including tooling, runtime, connection setup, browsing, and verification. Attach to the user's existing browser instead of launching a separate session.

Use a browser-level WebSocket CDP endpoint supplied by the user or environment (`BROWSER_CDP_URL`). Otherwise default to `ws://127.0.0.1:9222/devtools/browser`. Keep the `/devtools/browser` path: Chrome's settings-enabled remote debugging supports it without a browser ID, while the bare WebSocket root can return 403 without an approval prompt. Preserve an explicitly supplied WebSocket path; do not use a page-level `/devtools/page/...` endpoint.

For an HTTP debugging address, request `/json/version` and use `webSocketDebuggerUrl`. If discovery returns 404, try `/devtools/browser` on the same host and port with `ws` (or `wss` for HTTPS). Resolve only the supplied endpoint or the default; do not scan ports or expose endpoint credentials. Chrome may request connection approval, but a 403 alone does not establish that approval is pending.

Select the existing tab relevant to the task and reuse its signed-in session. If attachment fails or the expected session is unavailable, report the blocker; do not silently substitute a fresh browser or restart the user's browser.

Keep the session available for follow-up work. When disconnecting is requested, leave the user's browser and existing tabs running. Close a task-created tab only when it is no longer needed and the user does not need its result.
