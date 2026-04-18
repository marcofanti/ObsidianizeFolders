---
file_path: demo-to-chris-pre-built/ClaudeCommands.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document provides a detailed set of instructions for an AI model to analyze a codebase, generate comprehensive project documentation, and implement specific front-end modifications.

**What it does**:
- Directs the creation of a compact and structured `CLAUDE.md` file containing essential project overview, tech stack, and command references.
- Requires the extraction of reusable architectural patterns into a dedicated file (`.claude/docs/architectural_patterns.md`).
- Mandates specific code modifications, including creating a backup of the landing page, updating the landing page content, and adding a new bank accounts dashboard page.

**Key exports**:
- `CLAUDE.md`: The primary documentation file, structured for quick onboarding and adhering to progressive disclosure principles.
- `.claude/docs/architectural_patterns.md`: A dedicated file detailing architectural patterns, design decisions, and conventions observed across the codebase.
- Updated Application Files: The landing page and the application structure will be modified to reflect a modern financial application flow, including a demo bank accounts page.

**Gotchas**:
- The resulting `CLAUDE.md` must be kept under 150 lines and must not include formatting guidelines, assuming external linters will handle styling.
- The process requires maintaining file:line references rather than including code snippets.
- The final structure requires the `CLAUDE.md` to self-reference the patterns documented in `architectural_patterns.md`.