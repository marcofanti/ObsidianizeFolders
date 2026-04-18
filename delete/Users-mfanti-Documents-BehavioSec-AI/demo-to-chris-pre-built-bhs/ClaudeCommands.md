---
file_path: demo-to-chris-pre-built-bhs/ClaudeCommands.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file outlines a complex set of instructions for an AI to analyze, document, and modify a modern application codebase, resulting in detailed technical documentation and updated source files.

**What it does**:
- Generates a high-level documentation file (`CLAUDE.md`) detailing the project's architecture, purpose, and usage instructions while strictly adhering to length and content guidelines.
- Extracts reusable design conventions and patterns into a separate, dedicated architectural patterns file.
- Updates the application's landing page content to match a specified reference path.
- Adds a new demo bank accounts page within the application's structure.

**Key exports**:
- `CLAUDE.md`: The primary documentation file providing a concise overview (WHAT, WHY, HOW) of the project structure, utilizing progressive disclosure.
- `.claude/docs/architectural_patterns.md`: A dedicated file documenting cross-cutting architectural patterns, design decisions, and conventions observed across multiple project files.
- Updated Landing Page Code: The initial application page updated to reflect specific external content.
- New Dashboard Page Code: A newly added page designed to showcase demo bank accounts functionality.

**Gotchas**:
- The generated `CLAUDE.md` must be highly constrained, kept under 150 lines, and must use file:line references rather than code snippets.
- Documentation requires a focus on "universally applicable" information, prioritizing conciseness over comprehensive detail.
- Architectural patterns must be observed across *multiple* files to be included in the dedicated patterns file.
- All content modifications rely on specific external file paths for accurate replication.