---
name: playwright
description: Browse and automate websites with Playwright in a persistent Python interactive session, launching headless Firefox by default. Use for navigation, page inspection, forms, screenshots, and web UI tasks that do not require attachment to the user's existing browser.
---

# Playwright

Use Playwright's Python synchronous API through a persistent `python -i` process. Default to Mozilla Firefox in headless mode unless the user requests another browser or a visible window. This launches a separate browser session; it does not inherit the user's signed-in browser profile.

## Start a persistent session

Check that the chosen interpreter can import `playwright.sync_api`. If needed, install Playwright in an appropriate virtual environment with `python -m pip install playwright`, then install Firefox with the same interpreter using `python -m playwright install firefox`. If launch reports missing system dependencies, use the reported dependency instructions when permitted, or report the concrete blocker.

Start `python -i -q` using `exec_command` with `tty: true` and retain the returned `session_id`. Send all subsequent Python commands to that session using `write_stdin`, including a trailing newline. Do not start a fresh interpreter for each action or use shell backgrounding with `&`: the persistent tool session provides stdin access.

Initialize in the REPL:

```python
import json
import os
from playwright.sync_api import sync_playwright
pw = sync_playwright().start()
browser = pw.firefox.launch(headless=True)
storage = os.environ.get("PW")
storage_state = json.loads(storage) if storage and storage.lstrip().startswith("{") else storage
context = browser.new_context(storage_state=storage_state or None)
page = context.new_page()
page.set_default_timeout(15000)
page.set_default_navigation_timeout(30000)
```

By default, load browser storage state from the `PW` environment variable when it is nonempty. Accept either a storage-state JSON object or a path to a storage-state JSON file. If `PW` is unset or empty, start with a fresh context. Use a different storage state when the user requests it, and do not print the environment value or its credentials.

Keep `pw`, `browser`, `context`, and `page` alive across calls. Avoid a `with sync_playwright()` block that would exit between actions. End interactive compound statements with a blank line, or send them through `exec()` with a multiline string. Wait for each command to finish before issuing the next browser action; poll the same session when an operation is still running. After an exception, inspect the current page state before retrying.

## Browse and verify

Navigate with `page.goto(url, wait_until="domcontentloaded")`, then inspect the URL, title, and relevant visible content. Prefer role, label, and text locators derived from the actual page. Use locator waiting or Playwright assertions for the needed state instead of fixed sleeps or assuming every site reaches network idle.

For example, adapt these commands to observed content:

```python
print(page.url, page.title())
print(page.locator("body").inner_text()[:12000])
page.get_by_role("link", name="Documentation", exact=True).click()
```

Inspect relevant page regions when the page is large. Verify the resulting URL, visible content, or UI state after meaningful actions. Reinspect after navigation or DOM changes. Before retrying a submission after an error, check whether it already succeeded.

Save screenshots and downloads to known task output paths. Use `page.screenshot(path="/absolute/output/path.png", full_page=True)` and view the saved image with the available image tool when visual inspection matters. Report useful artifact paths. Avoid printing credentials, cookies, or tokens. Keep account changes and communications within the user's authorization.

## Finish

When the browsing task is complete, close the owned context and browser, stop Playwright, and exit the interpreter:

```python
context.close()
browser.close()
pw.stop()
exit()
```

If the process exits unexpectedly, its Python objects are lost. Start a new session and inspect the website's current state before resuming actions that may already have taken effect.
