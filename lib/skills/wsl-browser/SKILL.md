---
name: wsl-browser
description: Control the user's existing Windows browser from WSL. Use when the browser is on Windows, especially when WSL cannot reach it directly.
---

# Windows browser from WSL

Read [the browser skill](../browser/SKILL.md) for reuse and preservation of the user's existing session. Read [the headless skill](../headless/SKILL.md) for all implementation details, including tooling, runtime, connection setup, browsing, and verification.

Run the browser automation on Windows through WSL interop when needed to reach the Windows browser. Check dependencies in the Windows environment; a failed connection or an installed dependency in WSL does not establish the browser's availability or dependencies on Windows.

Account for Windows environment variables and file paths when crossing the WSL boundary. Report generated artifacts through paths accessible to the user.
