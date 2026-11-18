---
name: browser
description: Control the user's existing Chromium browser through a WebSocket CDP connection, reusing its signed-in context and tabs. Use when a task requires the user's browser rather than a separate automated browser session.
---

# Browser

Read [the headless skill](../headless/SKILL.md) for the runtime, Playwright implementation, persistent session, browsing, and verification workflow. Apply the attachment differences below instead of launching a browser or initializing storage state.

## Attach to the user's browser

Use a browser-level CDP endpoint supplied by the user or environment (`BROWSER_CDP_URL`). Otherwise default to `ws://127.0.0.1:9222/devtools/browser`. Keep the `/devtools/browser` path: Chrome's settings-enabled remote debugging supports it without a browser ID, while the bare WebSocket root can return 403 without an approval prompt.

For an HTTP debugging address, request `/json/version` and use `webSocketDebuggerUrl`. If discovery returns 404, try `/devtools/browser` on the same host and port with `ws` (or `wss` for HTTPS). Preserve an explicitly supplied WebSocket path. Use Playwright's Chromium CDP attachment, not a page-level `/devtools/page/...` endpoint or a Playwright protocol connection. Browser binary installation is unnecessary.

Resolve only the supplied endpoint or the default; do not scan ports. Avoid exposing endpoint credentials. Chrome may request connection approval, but a 403 alone does not establish that approval is pending. If attachment fails, report the concrete error and request an updated endpoint when needed. Do not silently launch a separate browser or restart the user's browser.

## Reuse the user session

Inspect existing contexts and tabs to identify the requested page, limiting inspection to relevant URLs and avoiding sensitive values. Select the observed matching context and page; ask which to use only if the task cannot disambiguate matches. Create a task tab in an existing context when needed. If no contexts exist, report that the expected user session is unavailable rather than creating a replacement context. Reuse existing cookies; skip headless's storage-state initialization.

Follow headless's browsing and verification workflow. Actions affect the user's live browser and account. CDP has lower fidelity than Playwright's native connection; inspect current state after unsupported operations or connection failures before retrying. After reconnecting, enumerate contexts and tabs again rather than reusing stale objects or indices.

Keep the connection available for follow-up work as described in headless. When disconnecting is requested, stop the local Playwright connection without closing the user's browser, existing contexts, or existing tabs. Do not send CDP `Browser.close` or use headless's browser/context cleanup. Close a task-created tab only when it is no longer needed and the user does not need its result.
