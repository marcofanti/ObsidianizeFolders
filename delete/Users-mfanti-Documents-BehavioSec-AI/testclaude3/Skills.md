---
file_path: testclaude3/Skills.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file details the specific tools, technical skills, and architectural patterns used to successfully develop the FinanceApp project.

**What it does**:
- Documents best practices for file system interaction, including parallel reading of multiple components to optimize development time.
- Utilizes structured development flows by pre-emptively gathering user requirements and tracking progress across defined steps.
- Establishes a modern web application using React, TypeScript, and Vite for type safety and efficient component rendering.

**Gotchas**:
- Authentication is handled via a mock system using React Context combined with `localStorage`, designed as a drop-in replacement for external services like Auth0.
- Protected routes are implemented using the `<Navigate replace>` component to ensure proper client-side redirection upon unauthorized access.
- Error handling across the application relies on React Error Boundaries (implemented as class components) to capture and manage runtime component errors.
- The Dashboard component is designed to run using hardcoded, demo data, meaning no immediate backend API integration is required for initial functionality.