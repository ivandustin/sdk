---
name: browser
description: Use Playwright to control the user's existing Chromium browser through a WebSocket CDP connection, reusing its signed-in context and tabs. Use when a task requires the user's browser rather than a separate automated browser session.
---

# Browser

Read [the Playwright skill](../playwright/SKILL.md) and use its persistent Python REPL workflow, page inspection, locators, waiting, and verification guidance. Replace its browser launch, storage-state initialization, and cleanup with the attachment workflow below.

## Connect to the user's browser

Use a browser-level `ws://` or `wss://` Chrome DevTools Protocol endpoint supplied by the user or the environment. Use `BROWSER_CDP_URL` as the environment convention for this skill; do not print its value because it may contain credentials. Do not confuse a page-level `/devtools/page/...` endpoint or a Playwright protocol endpoint with a browser CDP endpoint.

If only a remote-debugging HTTP address is supplied, read that address's `/json/version` response and use its `webSocketDebuggerUrl`. Resolve only the supplied address; do not scan for debugging ports or guess endpoints. If no endpoint is available, ask for the user's browser WebSocket CDP URL. If connection fails, report the concrete blocker and request an updated endpoint when needed. Do not silently launch a separate browser or restart the user's browser.

CDP attachment supports Chromium-based browsers only. Check that `playwright.sync_api` is importable as described in the Playwright skill; browser binary installation is unnecessary for attachment.

Start `python -i -q` with `tty: true` and retain its `session_id`. Initialize in that persistent REPL:

```python
import os
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright
endpoint = os.environ.get("BROWSER_CDP_URL", "").strip()
# If supplied directly instead, assign that endpoint without printing it.
assert urlsplit(endpoint).scheme in ("ws", "wss"), "A WebSocket CDP URL is required"
pw = sync_playwright().start()
browser = pw.chromium.connect_over_cdp(endpoint, timeout=30000)
```

Do not use `launch()`, `launch_persistent_context()`, or the Playwright skill's `PW` storage-state initialization. Reuse the attached browser's contexts and cookies.

## Select a tab and work

Inspect available tabs before choosing one:

```python
tabs = [(ci, pi, tab.url) for ci, ctx in enumerate(browser.contexts)
        for pi, tab in enumerate(ctx.pages)]
print(tabs)
```

Keep tab inspection scoped to identifying the requested page; URLs can contain sensitive values. Select the context and page matching the user's task using the observed indices, rather than assuming the first tab is the intended target:

```python
context = browser.contexts[context_index]
page = context.pages[page_index]
page.set_default_timeout(15000)
page.set_default_navigation_timeout(30000)
```

If several tabs match and the task cannot disambiguate them, ask which to use. If the task needs a new tab, create it with `context.new_page()` in the appropriate existing context. If no contexts exist, report that the expected user session is unavailable rather than substituting a fresh context.

Follow the Playwright skill's browsing and verification instructions. Actions affect the user's live browser and account; keep them within the requested task. CDP has lower fidelity than Playwright's native connection, so inspect current state after unsupported operations or connection failures before retrying. On reconnect, enumerate tabs again because previous Python objects and indices may be stale.

## Disconnect

Leave existing contexts, tabs, and the browser running. Do not execute the Playwright skill's `context.close()` / `browser.close()` cleanup or send the CDP `Browser.close` command. Close a tab created for the task only when it is no longer needed and the user does not need its result. Stop the local Playwright connection and exit the interpreter:

```python
pw.stop()
exit()
```

API reference: [Playwright connect_over_cdp](https://playwright.dev/python/docs/api/class-browsertype#browser-type-connect-over-cdp).
