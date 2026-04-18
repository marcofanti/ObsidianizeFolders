---
file_path: stitch-mcp/.claude/settings.local.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file provides local, environment-specific configuration settings, governing the permissions and active servers for an AI agent (Claude) interacting with the `stitch-mcp` project.

**What it does**:
- Grants the agent permission to perform core project operations, such as listing all defined projects and screens within the `stitch-mcp` scope.
- Enables execution of various complex shell commands, including running linting checks (`eslint`), listing files (`ls`), and programmatically opening various design previews and documentation files (`open`).
- Establishes a whitelist of specific local directories and file paths that the agent can access.
- Globally activates all project MCP servers and specifically enables the `stitch` server.

**Key exports**:
- **stitch**: Activates the primary `stitch` module server within the MCP system, making its functions available to the AI agent.
- **mcp__stitch__list_projects**: Exposes a function allowing the agent to discover and list all available projects within the scope.
- **mcp__stitch__list_screens**: Exposes a function allowing the agent to discover and list all available screens/components within the scope.

**Gotchas**:
- **High Privilege Level**: The configuration grants very high system privileges by explicitly allowing complex shell commands (e.g., `Bash(...)` and `open (...)`), meaning the agent can interact with the file system and local operating system environment heavily.
- **Hardcoded Paths**: The permissions rely on numerous highly specific, hardcoded file paths, including temporary text/code snippets within the `additionalDirectories` list, which suggests these settings are extremely environment-dependent.