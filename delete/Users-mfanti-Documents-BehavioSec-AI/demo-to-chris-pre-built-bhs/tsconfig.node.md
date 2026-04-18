---
file_path: demo-to-chris-pre-built-bhs/finance-app/tsconfig.node.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Configures the TypeScript compiler options for a Node.js environment, enabling strict type checking and modern module resolution while preventing actual JavaScript output.

**What it does**:
- Enforces the strictest TypeScript type checking standards (`strict: true`) across the codebase.
- Configures the project to use modern JavaScript standards (ES2022/ES2023) and modern bundler module resolution.
- Ensures the compiler only *validates* types and does not generate output JavaScript files (`noEmit: true`).
- Includes specific linting flags (e.g., `noUnusedLocals`, `noFallthroughCasesInSwitch`) to improve code quality and safety.

**Gotchas**:
- **No Output:** The setting `"noEmit": true` means this configuration only validates the TypeScript code; it will not generate JavaScript files. A separate build step (like a bundler) must be used for compilation.
- **Strictness:** Due to `"strict": true` and numerous specific flags, the codebase must adhere to highly robust and meticulous typing practices.
- **Scope:** The configuration is designed for a node/bundler environment, specifically including `vite.config.ts`, indicating tight coupling with the Vite build system.