# Login512 Model Context Protocol (MCP) Server 🛡️⚡

[![MCP Standard](https://img.shields.io/badge/MCP-2024--11--05-blue.svg)](https://modelcontextprotocol.io)
[![Post-Quantum](https://img.shields.io/badge/Security-NIST_FIPS_204_PQC-emerald.svg)](https://login512.com/security.html)
[![Zero-Image Privacy](https://img.shields.io/badge/Privacy-Zero--Image_RAM_Only-purple.svg)](https://login512.com/legal/privacy.html)
[![License](https://img.shields.io/badge/License-MIT-gray.svg)](LICENSE)

Official Model Context Protocol (MCP) server for **Login512** — the Post-Quantum Biometric & Passkey Platform.
Enables AI Coding Agents (**Cursor**, **Claude Desktop**, **Windsurf**, **VS Code Cline**, **Claude Code CLI**, and **Google Antigravity**) to autonomously inspect codebases, install verified biometric SDKs for 28+ frameworks, and audit security compliance with Zero Hallucination.

---

## 🚀 Features

* **🔍 `login512_inspect_project`**: Auto-detects project language and framework (Next.js, React, Vue, Svelte, Angular, FastAPI, Django, Flask, Express, NestJS, Laravel, Symfony, Spring Boot, Go, Rust, .NET Core, Flutter, iOS, Android, WordPress, Shopify, Strapi).
* **⚡ `login512_get_instructions`**: Returns exact package URLs (`.tgz`, `.tar.gz`, `.zip`), CLI installation commands, and ready-to-run boilerplate code.
* **📦 `login512_list_sdks`**: Lists all 28 official Login512 client and server SDKs with live download endpoints.
* **🛡️ `login512_audit_code`**: Audits integration code to enforce Zero-Image camera privacy and prevent Secret Key (`l512_sk_...`) exposure in client-side code.
* **🔐 `login512_setup_2fa_and_genesis`**: Generates drop-in code for **2FA replacing 6-digit TOTP / Google Authenticator** (with Face Scan + Low-Light Fingerprint/Passkey fallback and **One-Click Primary Login512 Upgrade** to bypass legacy Password/LINE/Google next time) and **First-Time Genesis Mode** (100% passwordless initial Superadmin claim with One-Time Genesis Setup Key & auto-seal).

---

## 🛠️ Quick Installation

### 1. Cursor IDE
Add to your project's `.cursor/mcp.json` (or in Cursor Settings > Features > MCP Servers):
```json
{
  "mcpServers": {
    "login512": {
      "command": "python",
      "args": ["-c", "import urllib.request; exec(urllib.request.urlopen('https://login512.com/sdk-ai/mcp-server/server.py').read().decode('utf-8'))"]
    }
  }
}
```

### 2. Claude Desktop
Add to your `claude_desktop_config.json`:
* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "login512": {
      "command": "python",
      "args": ["-c", "import urllib.request; exec(urllib.request.urlopen('https://login512.com/sdk-ai/mcp-server/server.py').read().decode('utf-8'))"]
    }
  }
}
```

### 3. Windsurf Editor (Codeium Cascade)
Add to `~/.codeium/windsurf/mcp_config.json` (or `%USERPROFILE%\.codeium\windsurf\mcp_config.json` on Windows):
```json
{
  "mcpServers": {
    "login512": {
      "command": "python",
      "args": ["-c", "import urllib.request; exec(urllib.request.urlopen('https://login512.com/sdk-ai/mcp-server/server.py').read().decode('utf-8'))"]
    }
  }
}
```

### 4. Claude Code CLI (Terminal)
Run in your terminal:
```bash
claude mcp add login512 python -c "import urllib.request; exec(urllib.request.urlopen('https://login512.com/sdk-ai/mcp-server/server.py').read().decode('utf-8'))"
```

---

## 💬 Example Prompts for AI Agents

Once connected, simply prompt your AI agent:

> *"Please connect Login512 face and fingerprint biometric authentication to this application's login screen."*

The AI will automatically:
1. Call `login512_inspect_project` to identify your framework.
2. Install the matching package (e.g. `npm install https://login512.com/packages/nextjs.tgz`).
3. Generate the biometric component and backend token verification route.
4. Run `login512_audit_code` to verify that your secret keys are safe.

Or for **drop-in TOTP replacement & First-Time Genesis Mode**:

> *"Add Login512 2FA to replace Google Authenticator / TOTP alongside our existing Password/LINE/Google login with a one-click Primary Login512 Upgrade button, plus First-Time Genesis Mode for initial passwordless Superadmin setup."*

The AI will call `login512_setup_2fa_and_genesis` (with `mode: "2fa_upgrade"`, `"genesis_first_boot"`, or `"both"`) to generate ready-to-use `sdk.mount2FA()`, `sdk.shouldBypassLegacyLogin()`, and `sdk.mountGenesisSetup()` snippets wired to `/v1/2fa/*` and `/v1/genesis/*`.

---

## 📚 Official Resources

* **Platform Website**: [https://login512.com](https://login512.com)
* **Developer Portal**: [https://login512.com/portal/index.html](https://login512.com/portal/index.html)
* **Full MCP Documentation**: [https://login512.com/mcp.html](https://login512.com/mcp.html)
* **Integration Guide**: [https://login512.com/guide.html](https://login512.com/guide.html)
* **AI Context File**: [https://login512.com/llms.txt](https://login512.com/llms.txt)

---

## 📄 License
MIT License. Copyright © 2026 Login512 Engineering.

