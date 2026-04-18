---
file_path: demo-template/ClaudePrompt.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document serves as a prompt template designed to guide an AI (Claude) in generating a complete, multi-page Single Page Application (SPA) for a mock financial dashboard.

**What it does**:
- Initializes a new SPA using the React, Vite, and TypeScript stack.
- Ensures the project is housed in a conflict-aware folder structure (`/finance-app`), automatically incrementing the folder name if a previous version exists.
- Scaffolds six core pages (Landing, Login, Signup, Password Reset, Error, Dashboard) using specified template structures.
- Implements a functional, state-based mock authentication context designed to simplify future integration with Auth0.

**Key exports**:
- **Project Structure**: Creates the entire SPA scaffolding in the `/finance-app` directory.
- **Mock Auth Context**: Provides state management for simulating user login, designed to be easily replaced with real API calls later.
- **Templates**: Requires the use of pre-existing templates for the core UI components (e.g., `LoginPage.tsx`, `Dashboard.tsx`).

**Gotchas**:
- **Mock Authentication**: The application intentionally uses placeholder authentication logic and must not involve actual API calls or real user validation.
- **Folder Conflict Handling**: The AI must strictly adhere to the folder renaming logic (incrementing `/finance-app` to `/finance-app1`, etc.) if the project directory already exists.
- **Scope Limitation**: The prompt explicitly instructs the AI to ignore several directories and files to ensure that only the new, clean application structure is built.