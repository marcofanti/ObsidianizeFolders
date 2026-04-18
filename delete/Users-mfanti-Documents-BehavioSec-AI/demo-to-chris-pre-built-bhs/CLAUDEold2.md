---
file_path: demo-to-chris-pre-built-bhs/CLAUDEold2.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document provides a technical guide and pre-built templates for bootstrapping a multi-technology "SecureBank" financial demo application.

**What it does**:
- Defines the source code structure for a React/TypeScript/Auth0 application, providing reusable UI templates.
- Outlines explicit setup steps, including required dependencies (`@auth0/auth0-react`) and environment variables for local development.
- Details two distinct architectural paths: a client-side React/Auth0 stack and a standalone Java/Spring Boot alternative.
- Specifies a multi-layered component pattern that manages view rendering based on authentication status and loading state (`isLoading → isAuthenticated → render`).

**Key exports**:
- **`templates/`**: A directory containing core source files (e.g., `Dashboard.tsx`, `App.tsx`) that serve as copy-paste starting points for the application UI.
- **React/Auth0 Stack**: A complete, structured implementation utilizing React 19, TypeScript, and the Auth0 client library for secure authentication flow.
- **Java/Spring Boot Stack**: Provides a reference for creating a standalone, non-Auth0 backend version of the demo application.

**Gotchas**:
- The templates stored in the repository are starting points only and do not constitute a runnable application in this file system.
- Running the application requires manual setup, including running `npm create vite`, installing specific dependencies, and manually copying template files.
- The architecture requires managing both build-time and runtime environment configurations (e.g., `VITE_AUTH0_DOMAIN` in `.env` vs. `window.ENV_CONFIG` for Cloud Run).
- The authentication view rendering must strictly follow the `isLoading → isAuthenticated → render` conditional pattern in top-level components.