---
file_path: testclaude/ClaudeCommands.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file provides a multi-step set of directives to an AI model (Claude) instructing it to generate comprehensive technical documentation and execute specific code modifications for a financial application project.

**What it does**:
- Instructs the creation of a concise, structured `CLAUDE.md` document that serves as a progressive index for the entire project.
- Forces the extraction of reusable design decisions and conventions into a dedicated `architectural_patterns.md` file.
- Directs the modification of existing landing page content based on a specified local file path reference.
- Requires the addition of a new, functionally separate dashboard page to the application structure.

**Key exports**:
- `CLAUDE.md`: The primary project documentation detailing the architecture, tech stack, and basic usage instructions (WHAT, WHY, HOW).
- `.claude/docs/architectural_patterns.md`: A separate documentation file containing reusable architectural patterns and design conventions observed across the codebase.
- Updated Application Codebase: Includes the modified landing page (`/src/app/page.tsx`) and the newly added demo dashboard page.

**Gotchas**:
- The documentation creation is constrained by strict rules (e.g., under 150 lines, reliance on file:line references, use of Progressive Disclosure).
- The required code modifications rely on external, absolute local file paths (e.g., `/Users/mfanti/...`), which must be the source of truth for the content updates.
- The directives assume a functional relationship between the generated `CLAUDE.md` and the specialized documentation in the dedicated `.claude/docs/` directory.