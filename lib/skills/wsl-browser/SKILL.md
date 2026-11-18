---
name: wsl-browser
description: Control an existing Windows Chrome or Chromium session from Codex running in WSL by launching Windows Python and attaching Playwright over CDP. Use when the browser is on Windows, especially when WSL localhost cannot reach it.
---

# Windows browser from WSL

Run Playwright in Windows through WSL interop so Windows localhost reaches the existing browser's debugging listener. Reuse its signed-in contexts and tabs. This works without a proxy, gateway connection, firewall change, or browser restart.

## Start Windows Python

Check Windows Python and Playwright using Windows execution; an installation in WSL does not establish that they exist on Windows:

```bash
powershell.exe -NoProfile -Command 'python -c "import sys; import playwright.sync_api; print(sys.executable)"'
```

If `python` is unavailable, check `py` or a user-provided Windows interpreter. If Playwright is missing, install it into the chosen Windows interpreter when permitted. Browser binary installation is unnecessary for CDP attachment.

Start a persistent interpreter with `exec_command`, `tty: true`, and retain its `session_id`:

```bash
powershell.exe -NoProfile -Command '$env:PYTHON_BASIC_REPL="1"; python -i -q'
```

`PYTHON_BASIC_REPL` avoids modern Python console editing and color sequences interfering with piped input. A UNC working-directory warning from a Python batch shim is harmless if the Python prompt appears. Use Windows paths for any files the interpreter needs; do not depend on its working directory.

Send subsequent Python commands through `write_stdin` to the same session, ending each submitted line with `\r` (carriage return) in the tool argument. With the Windows basic REPL, `\n` alone can concatenate input without executing it. For a multiline snippet, send one `exec("line1\nline2")` command followed by `\r`, or send individual lines and wait for their prompts. Wait for each operation to finish before sending another. Keep this interpreter and its objects available for follow-up work.

## Attach to Chrome

Honor an explicit endpoint or `BROWSER_CDP_URL` first. WSL environment variables are not necessarily inherited by Windows Python; transfer an explicitly configured value without exposing credentials in tool output. Otherwise use the Windows loopback endpoint below:

```python
import os
from playwright.sync_api import sync_playwright
endpoint = os.environ.get("BROWSER_CDP_URL", "").strip() or "ws://127.0.0.1:9222/devtools/browser"
pw = sync_playwright().start()
browser = pw.chromium.connect_over_cdp(endpoint, timeout=30000)
print("Browser contexts:", len(browser.contexts))
```

Use a browser-level CDP WebSocket URL, not a page-level `/devtools/page/...` URL or a Playwright protocol endpoint. Preserve an explicitly supplied WebSocket path.

For an HTTP debugging address, request its `/json/version` from Windows and use `webSocketDebuggerUrl`. Chrome's settings-enabled debugging can return HTTP 404 while `ws://127.0.0.1:9222/devtools/browser` works. On that 404, use `/devtools/browser` on the same host and port with `ws` (or `wss` for HTTPS). Do not treat HTTP discovery failure as proof that debugging is disabled.

WSL's localhost may refer to Linux, and Windows loopback listeners may be unreachable through the WSL gateway. A failed Linux connection does not establish that Windows Chrome is unavailable. Prefer Windows execution over creating a network relay. Probe only the configured endpoint or default port; do not scan ports. Chrome may show a connection approval prompt, but a 403 alone does not establish that approval is pending. Report concrete errors if attachment fails; do not silently launch a fresh browser or restart the user's browser.

## Select a tab and work

Inspect tabs only as needed to identify the requested site; avoid exposing unrelated URLs or sensitive query strings. For example, filter on the task's hostname:

```python
from urllib.parse import urlsplit
print([(ci, pi, tab.url) for ci, ctx in enumerate(browser.contexts)
       for pi, tab in enumerate(ctx.pages)
       if urlsplit(tab.url).hostname == "example.com"])
```

Select the observed context and page indices:

```python
context = browser.contexts[context_index]
page = context.pages[page_index]
page.set_default_timeout(15000)
page.set_default_navigation_timeout(30000)
print(page.title())
print(page.locator("body").inner_text()[:12000])
```

Use existing contexts and cookies; do not create a replacement context when none is available. Create a task tab with `context.new_page()` only when needed. Navigate with `wait_until="domcontentloaded"`, inspect visible state, and use locators derived from the actual page. Reinspect after navigation or errors. Before retrying a submission, verify whether it already succeeded.

Screenshots and downloads use Windows paths. To use a WSL output location, convert it with `wslpath -w` and pass the resulting path as a Python raw string or correctly escaped string. Report artifacts through their accessible WSL paths.

## Preserve the user session

Leave the browser, existing contexts, and existing tabs running. Never call `browser.close()`, `context.close()`, or CDP `Browser.close` as cleanup. Close a task-created tab only when it is no longer needed. When disconnecting, call `pw.stop()` and exit the interpreter; do not disconnect merely because a turn ends if follow-up work needs the session. After reconnecting, inspect contexts and tabs again rather than reusing stale indices.
