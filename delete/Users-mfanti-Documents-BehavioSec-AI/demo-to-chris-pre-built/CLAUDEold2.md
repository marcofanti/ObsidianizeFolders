---
file_path: demo-to-chris-pre-built/CLAUDEold2.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file provides detailed documentation and architectural guidance for using reusable code templates to bootstrap secure, multi-platform financial demonstration applications (e.g., SecureBank).

**What it does**:
- Provides reusable, copy-paste source templates for a React/TypeScript/Auth0 financial demo application.
- Outlines the specific tech stack (React 19, TypeScript, Vite) and required dependencies for setting up the client-side application.
- Details the mandatory authentication flow using Auth0 Universal Login and implements view gating via `useAuth0()`.
- Guides the user through the setup process for two distinct architectures: the React/Auth0 web app and a standalone Java/Spring Boot backend.

**Key exports**:
- **Templates/**: Directory containing source files for the React frontend (e.g., `main.tsx`, `Dashboard.tsx`) that serve as project starting points.
- **React/Auth0 Stack**: The full implementation details for the web application, including the use of `Auth0Provider` and specific environmental variables (`VITE_AUTH0_DOMAIN`, `VITE_AUTH0_CLIENT_ID`).
- **Architecture Notes**: Defined components and patterns (e.g., conditional rendering, hardcoded demo data locations) necessary for maintaining the integrity of the demo application.

**Gotchas**:
- The templates are *starting points*, not runnable applications; manual setup using `npm create vite` and dependency installation is required.
- The front-end views must follow a strict conditional rendering pattern (`isLoading → isAuthenticated → render`) to correctly handle the multi-stage authentication lifecycle.
- The application requires both build-time environment variables (`.env`) and may need runtime configuration via `window.ENV_CONFIG` for deployment environments like Cloud Run.
- Demo data is hardcoded directly within `Dashboard.tsx` and should be noted when adapting the application for production use.