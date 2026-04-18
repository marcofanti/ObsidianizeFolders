---
file_path: stitch-mcp/logisticsdemo/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file serves as a root TypeScript configuration file that aggregates settings by referencing specialized configurations for the application and Node environments.

**What it does**:
- Sets up the primary project configuration by pointing to separate, dedicated configuration files for the main application logic (`tsconfig.app.json`) and server-side/build tooling logic (`tsconfig.node.json`).

**Key exports**:
- None (It does not define exports; it acts solely as a configuration reference hub).

**Gotchas**:
- This file is only a reference aggregator and contains no actual compiler options. Ensure that both `tsconfig.app.json` and `tsconfig.node.json` are correctly set up and exist in the project directory, as build tools will rely on these referenced files for compiler options.