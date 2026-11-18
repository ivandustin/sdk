---
name: wsl-browser
description: Control an existing Windows Chrome or Chromium session from WSL through CDP. Use when the browser is on Windows, especially when WSL localhost cannot reach it.
---

# Windows browser from WSL

Read [the browser skill](../browser/SKILL.md) for CDP attachment, endpoint resolution, tab selection, and preservation of the user's session. Read [the headless skill](../headless/SKILL.md) for the runtime, Playwright implementation, persistent session, browsing, and verification workflow. Apply the Windows execution differences below.

Run the chosen runtime and Playwright on Windows through WSL interop so Windows localhost reaches the browser's debugging listener. Check dependencies using Windows execution; an installation in WSL does not establish that they exist on Windows. Browser binary installation is unnecessary for CDP attachment. Keep the Windows process available for follow-up work, adapting interactive input to its console requirements.

Honor an explicit endpoint or `BROWSER_CDP_URL` before using browser's default Windows loopback endpoint. WSL environment variables are not necessarily inherited by Windows processes; transfer a configured value without exposing credentials. Perform HTTP endpoint discovery from Windows too.

WSL localhost may refer to Linux, and Windows loopback listeners may be unreachable through the WSL gateway. A failed Linux connection does not establish that Windows Chrome is unavailable. Prefer Windows execution over a network relay, firewall changes, or a browser restart.

Use Windows paths for screenshots, downloads, and other files accessed by the Windows process; do not depend on its working directory. Convert WSL output paths with `wslpath -w` when needed, and report artifacts through their accessible WSL paths.
