---
file_path: Demo/tsconfig.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file acts as a root TypeScript configuration aggregator, defining the structural dependencies and combining the compilation settings from separate configuration files for application and Node environments.

**What it does**:
- It uses the `references` property to specify that the compiler must load and synthesize settings from multiple separate configuration files.
- It effectively combines the rules defined in `./tsconfig.app.json` and `./tsconfig.node.json` into a single build context.

**Key exports**:
- `references`: An array that points to other `tsconfig` files, indicating required dependency configurations.
- `./tsconfig.app.json`: The configuration used for compiling the main application code base.
- `./tsconfig.node.json`: The configuration used for compiling or typing Node.js backend/server-side components.

**Gotchas**:
- The presence of an empty `files: []` array is expected, as the file's role is solely to define references, not to include source files itself.
- Changes made to the referenced files (`tsconfig.app.json` or `tsconfig.node.json`) will immediately impact the compilation rules defined by this root file.