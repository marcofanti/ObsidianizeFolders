---
file_path: testclaude3/ClaudeCommands.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: To establish the requirements, structure, and initial components for a modern financial application and generate comprehensive, highly structured technical documentation detailing the codebase's architecture and conventions.

**What it does**:
- Defines a constrained login flow for a financial application using Next.js and Auth0, adopting a specific professional aesthetic.
- Mandates the creation of a minimalist, high-level project overview document (`CLAUDE.md`) that focuses on essential information (WHAT, WHY, HOW) while using Progressive Disclosure techniques.
- Separates deep, reusable technical patterns and architectural decisions into a dedicated file (`.claude/docs/architectural_patterns.md`).
- Modifies application pages (landing page and dashboard) to use specific, predefined layouts and demo content, moving away from generic or original structures.

**Key exports**:
- `CLAUDE.md`: The central, summarized technical documentation file containing project overviews, tech stacks, and build instructions.
- `.claude/docs/architectural_patterns.md`: A specialized file documenting multi-file design patterns, conventions, and architectural decisions.
- Modified Landing Page (`src/app/page.tsx`): The application's entry point, updated to reflect a target structural template.
- Modified Dashboard Page (`src/app/dashboard/page.tsx`): The post-login page, updated to display demo bank accounts instead of generic profile information.

**Gotchas**:
- Documentation output must adhere strictly to a 150-line limit and cannot include formatting or code snippets, relying only on file:line references.
- Developers must assume the use of linting tools for code style, meaning no formatting guidelines should be documented.
- The process relies on referencing specific, potentially ephemeral, local file paths for required layout emulation and content sourcing.
- Architectural patterns must be patterns observed *across multiple files* to be eligible for extraction into the patterns document.