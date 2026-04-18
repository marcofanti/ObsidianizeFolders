---
file_path: stitch-mcp/ThingsToDo.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file serves as a checklist and reference guide demonstrating the initial setup, core commands, and major development tasks required for using the `stitch-mcp` tool.

**What it does**:
- Allows the user to configure a new transport connection for the `stitch` tool using specific HTTP endpoints and required API keys.
- Provides commands to list existing projects associated with the configured service.
- Enables serving a specified project locally using the configured CLI setup.
- Outlines a major development goal: converting a multi-page web application (`logisticsdemo`) into a modular React component system.

**Key exports**:
- `claude mcp add stitch`: Configures a new transport connection for the `stitch` CLI, specifying the API endpoint and authentication header.
- `stitch - list_projects`: Retrieves a list of all projects managed by the configured `stitch` instance.
- `stitch-mcp serve`: Initiates the local serving or deployment of a specified project ID.

**Gotchas**:
- **API Key Management**: The commands contain hardcoded Google API keys (`X-Goog-Api-Key`), indicating that secure handling and eventual replacement of these credentials are necessary.
- **Setup Dependency**: The core functionality relies on successful prior configuration of the transport layer using the `claude mcp add stitch` command.
- **Major Development Scope**: The listed project conversion task (logisticsdemo to React components) is a significant, multi-part development effort that requires adherence to mock authentication systems.