---
file_path: stitch-mcp/geminitoday.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file provides a command script demonstrating various methods for initializing, authenticating, configuring, and testing the `stitch-mcp` service.

**What it does**:
- Allows the user to start the `stitch-mcp` server using different input formats for the project identifier (project title, ID, or fully qualified resource name).
- Provides methods for environment-dependent execution, including loading project context from `.env` files or explicitly setting API keys.
- Initializes and registers the Stitch Manifest Configuration Protocol (MCP) endpoint with the `claude` system for both user and project scopes.
- Offers utility commands to verify configuration health (`doctor`) and list available projects.

**Key exports**:
- `stitch-mcp serve`: Initiates the server process for a specified project.
- `stitch-mcp list projects`: Retrieves a list of projects available within the current environment context.
- `stitch-mcp doctor`: Runs a diagnostic check to ensure the local configuration is healthy and ready for operation.
- `claude mcp add stitch`: Configures the connection details for the Stitch MCP endpoint within the `claude` configuration system.

**Gotchas**:
- **Authentication Complexity**: Successful execution relies heavily on correct API key management; the `STITCH_API_KEY` must be correctly exported or set for the server to run successfully.
- **Project Identifier Format**: The project identifier (`-p`) can be passed in multiple formats (short title, raw ID, or `projects/<ID>`), requiring the user to know which format the system expects.
- **Chaining Commands**: Some commands require careful environment variable chaining (e.g., `export $(grep -v '^#' .env | xargs) && stitch-mcp list projects`) to load credentials and context correctly before execution.