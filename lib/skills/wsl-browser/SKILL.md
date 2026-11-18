---
name: wsl-browser
description: Connect from WSL to an existing Chrome or Chromium session on the Windows host using CDP, including a Caddy relay when remote debugging listens only on Windows loopback.
---

# Windows browser from WSL

Read [browser](../browser/SKILL.md) for persistent Playwright attachment, tab selection, and disconnect behavior. Use this skill to resolve the WSL-to-Windows transport before attaching. Reuse the live browser; do not launch or restart it.

## Choose the endpoint

Honor a user-supplied endpoint or `BROWSER_CDP_URL` first, without printing credentials. Preserve an explicitly supplied WebSocket path.

Without an endpoint, try `ws://127.0.0.1:9222/devtools/browser`. If this fails and the browser is on Windows, inspect the network rather than assuming Linux localhost reaches Windows:

```bash
wslinfo --networking-mode
ip route show default
```

In NAT mode, the default gateway is normally the Windows host address. Derive it from the current route; do not hardcode an address from a previous session. In mirrored mode, try localhost first. If `wslinfo` is unavailable, use the route and listener evidence rather than assuming a networking mode.

If Windows interop is available, inspect the configured debugging port (9222 by default):

```powershell
powershell.exe -NoProfile -Command 'Get-NetTCPConnection -LocalPort 9222 -State Listen -ErrorAction SilentlyContinue | Select-Object LocalAddress,LocalPort | ConvertTo-Json -Compress'
```

A Windows listener on `127.0.0.1` is loopback-only and cannot be reached through the Windows gateway address from WSL NAT. A refusal on WSL localhost does not establish that Windows remote debugging is disabled. A timeout through the gateway alone does not distinguish a loopback listener from a firewall block. Probe only the configured endpoint and derived host address, without scanning ports.

## Relay with Caddy when needed

When Chrome listens on Windows loopback, prepare this command for Windows PowerShell, replacing `<WINDOWS_HOST_IP>` with the observed WSL gateway. Use the actual debugging port if different; 9223 is a separate relay port:

```powershell
caddy reverse-proxy --from http://<WINDOWS_HOST_IP>:9223 --to http://127.0.0.1:9222 --change-host-header
```

Caddy handles WebSocket upgrades. The HTTP scheme avoids automatic HTTPS, and `--change-host-header` presents the upstream loopback address to Chrome. Bind to the Windows WSL interface as shown, rather than all interfaces. Keep the command running during use; Ctrl+C stops the relay. Do not install Caddy, change firewall rules, or reconfigure WSL merely to prepare this command.

After the user starts the relay, attach to:

```text
ws://<WINDOWS_HOST_IP>:9223/devtools/browser
```

For Chrome's settings-enabled remote debugging, retain `/devtools/browser` even without a browser ID. HTTP `/json/version` discovery may return 404 while this WebSocket endpoint works. For an explicitly supplied browser-ID path, preserve it. If HTTP discovery through a relay advertises a loopback WebSocket address, retain the returned browser path but use the reachable relay host and port.

Chrome may show a connection approval prompt; a 403 alone does not prove approval is pending. Report concrete connection errors. If the relay times out, check whether Caddy started successfully and whether Windows permits the connection before proposing a configuration change.

## Verify attachment

Use the persistent Python REPL from the browser skill, passing the resolved endpoint to `pw.chromium.connect_over_cdp(endpoint, timeout=30000)`. Verify that existing contexts are available and report the tab count without exposing unrelated URLs. Enumerate tabs only as needed to choose the user's requested page. Keep the interpreter session available for follow-up work, and never close the user's browser or existing tabs as cleanup.

References: [Caddy CLI](https://caddyserver.com/docs/command-line), [WebSocket proxy support](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy).
