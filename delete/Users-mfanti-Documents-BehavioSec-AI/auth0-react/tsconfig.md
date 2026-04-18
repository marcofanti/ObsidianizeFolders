---
file_path: auth0-react/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file establishes the root TypeScript compiler configuration for the package by referencing specialized configuration files that handle different execution environments.

**What it does**:
- Acts as an index, compiling settings from multiple, segregated TypeScript configurations rather than defining settings itself.
- Ensures that the project uses distinct and optimized compiler rules for client-side code (applications) and server/build-tool code (Node.js environment).

**Key exports**:
- tsconfig.app.json: The configuration file for client-side, browser-based code (e.g., React components).
- tsconfig.node.json: The configuration file for environment-specific code that runs in a Node.js runtime (e.g., build scripts, server logic).

**Gotchas**:
- This file does not contain any compilation logic or options; it is purely structural.
- If either referenced configuration file (`tsconfig.app.json` or `tsconfig.node.json`) is missing or malformed, the overall project build will fail, as this file relies entirely on the existence of its references.
- The compilation settings for the entire package are determined by the combination of the referenced files, not by the settings within this root file.