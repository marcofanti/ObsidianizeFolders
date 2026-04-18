---
file_path: stitch-mcp/CLAUDE.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document serves as the comprehensive instruction manual and constraint guide for the `stitch-mcp` toolkit, detailing how to build, instrument, and maintain standardized React demo applications.

**What it does**:
- Provides two core runbooks (`Tasks.md` and `AddProfiling.md`) to drive the full application lifecycle, from initial creation to professional profiling integration.
- Defines a strict shared tech stack (Vite + React 19 + TypeScript) and standard component placement within the application structure.
- Enforces technical constraints, such as specific module import methods and external dependency loading, to ensure consistent build quality across all demo applications.

**Key exports**:
- `Tasks.md`: The step-by-step runbook used to build a new industry demo application from scratch.
- `AddProfiling.md`: The runbook used to incorporate ThreatMetrix / BehavioSec profiling into an existing application.
- `src/data/mockData.ts`: The designated location for all static application data and associated TypeScript types.

**Gotchas**:
- **TypeScript Imports**: Always use `import type { ... } from "..."` when importing interfaces or type-only values to prevent silent runtime `SyntaxError` failures caused by `verbatimModuleSyntax`.
- **Google Fonts**: Fonts must be loaded using a `<link>` tag in `index.html`; using `@import` in CSS will fail due to PostCSS limitations.
- **Modification Constraints**: Never modify files within the `ln/` directory, nor should `.md` files in the project root be modified unless explicitly instructed by the user.
- **Profiling Specifics**: The `page_id` for profiling must be handled as a numeric value cast to a `String` at the call site, and the package manager must always be `npm`.