---
name: browser
description: Browse and automate websites using Playwright from a persistent Python interactive session attached to the user's browser at 127.0.0.1:9222. Use for browser navigation, page inspection, forms, screenshots, and web UI tasks.
---

# Browser

Use Python Playwright through `python -i` and the user's running browser at `http://127.0.0.1:9222`, preserving their existing profile and signed-in session.

## Connect to the user's browser

- Check that the chosen Python interpreter can import `playwright.sync_api`. If missing, install with that interpreter's `python -m pip install playwright`, using a project virtual environment when appropriate. A bundled Playwright browser download is unnecessary for attachment.
- Attach directly to `http://127.0.0.1:9222` through Chrome DevTools Protocol (CDP). Do not detect the OS default browser or discover alternative endpoints.
- A Chromium-based browser must already expose remote debugging at that address. If attachment fails, report the concrete failure and ask the user to make that endpoint available. Do not terminate or relaunch the user's browser, copy profile data, or substitute another browser or profile.

## Keep one interactive Python process

Start `python -i` with a persistent terminal/PTY and retain its session ID. Send subsequent Python statements to that same process using terminal stdin. Do not run a new Python process for each action. In the interactive prompt, end compound statements with a blank line; use `exec()` with a multiline string when terminal input handling requires it.

Initialize in that REPL:

```python
import inspect
from playwright.sync_api import sync_playwright
pw = sync_playwright().start()
options = {"timeout": 15000}
if "no_defaults" in inspect.signature(pw.chromium.connect_over_cdp).parameters:
    options["no_defaults"] = True

browser = pw.chromium.connect_over_cdp("http://127.0.0.1:9222", **options)
context = browser.contexts[0]
[(i, tab.url) for i, tab in enumerate(context.pages)]
```

Keep `pw`, `browser`, `context`, and `page` alive across actions. Select the relevant existing tab after inspecting its URL; create a tab in the existing context when the task needs one. Do not create an isolated context when the task requires the user's authenticated session. Avoid a `with sync_playwright()` block that exits between actions.

## Work and verify

- Inspect the current page before acting. Prefer role, label, and text locators based on observed content; use Playwright's locator waiting and assertions instead of fixed sleeps.
- Keep browser operations within the user's requested task. Browser access does not grant permission for unrelated account changes or communications.
- After each meaningful action, verify the resulting URL, visible content, or relevant UI state. Reinspect after navigation or DOM changes rather than reusing stale element handles.
- Save screenshots or downloads to a known task output path when useful and report the artifact location. Avoid printing cookies, tokens, or unrelated private page content.
- If a connection drops, reconnect and enumerate tabs before retrying. Check whether a submitted action already succeeded before repeating it.
- At completion, detach using `pw.stop()` and exit the Python session. Leave the user's browser and existing tabs open; close only task-created tabs when appropriate. Do not call `browser.close()` or close the existing context.

See the [official Playwright Python CDP reference](https://playwright.dev/python/docs/api/class-browsertype#browser-type-connect-over-cdp) for installed-version compatibility and connection options.
