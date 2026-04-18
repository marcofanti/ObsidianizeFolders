---
file_path: testclaude3/CLAUDEold2.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file serves as a comprehensive guide and architectural specification for a template repository containing source code and prompts for a "SecureBank" financial demo application.

**What it does**:
- Defines the core components and relationships for a modern React/TypeScript application using Auth0 for authentication.
- Provides concrete setup instructions and necessary dependencies for bootstrapping the project into two distinct versions (React/Auth0 and Java/Spring Boot).
- Details the expected runtime behavior, required environment variables, and styling conventions for all included templates.

**Key exports**:
- **React/Auth0 Template**: A full-stack demo application built with React 19, TypeScript, Vite, and Auth0 for secure, authenticated access.
- **Java/Spring Boot Template**: A standalone demonstration version of the application that simulates functionality using an in-memory user store, bypassing the need for external identity providers like Auth0.
- **`main.tsx`**: The entry point responsible for setting up the Auth0 Provider and handling both runtime and build-time environment configurations.

**Gotchas**:
- The files in the `templates/` directory are reusable starting points, not runnable applications themselves.
- The application follows a strict conditional rendering pattern: all top-level components must check the sequence `isLoading → isAuthenticated → render`.
- The demo data (accounts and transactions) is hardcoded within `Dashboard.tsx` and must be updated if dynamic data fetching is required.
- Specific environment variables (`VITE_AUTH0_DOMAIN`, `VITE_AUTH0_CLIENT_ID`) must be correctly configured in the `.env` file for the Auth0 stack to function.
- The React/Auth0 development server is configured to run on port 8080, and this setting must be verified in `vite.config.ts`.