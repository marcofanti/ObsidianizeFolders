---
file_path: demo-to-chris-pre-built/Thinking.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document outlines the architectural plan and implementation steps for a modern, full-stack "Secure Bank" application using React/TypeScript and a Spring Boot REST API, featuring session-based authentication and dummy data endpoints.

**What it does**:
- Implements a robust session-based authentication system using Spring Security (login, signup, logout) with BCrypt password hashing.
- Provides a multi-page Single Page Application (SPA) using React/Vite, which consumes the REST API for state management and protected routing.
- Serves the entire application by packaging and serving the compiled React assets as static files from the Spring Boot backend.
- Exposes REST endpoints for user authentication (`/api/auth/*`) and demo financial data (`/api/accounts`, `/api/transactions`).

**Key exports**:
- `POST /api/auth/login`: Authenticates user credentials and establishes a session cookie.
- `POST /api/auth/signup`: Registers a new user account.
- `GET /api/auth/me`: Retrieves and validates the details of the currently authenticated user.
- `GET /api/accounts`: Fetches demo bank account data.
- `GET /api/transactions`: Fetches demo transaction history.
- **Architecture**: A unified deployment model where Spring Boot serves both the backend API and the static React frontend.

**Gotchas**:
- **Auth/Dev Flow**: During development, the setup uses a Vite proxy to handle API calls, circumventing local Cross-Origin Resource Sharing (CORS) issues; this proxy must be removed or adjusted for production deployment.
- **Session/Security**: The system relies on session-based authentication, requiring careful handling of CSRF protection (though the plan temporarily disables it for the demo, noting that a production fix requires cookie-based tokens).
- **Deployment Artifact**: The final production deployment requires using the Maven frontend plugin to build the React SPA and copy all compiled assets into the Spring Boot static resources directory to ensure a single, executable JAR file.
- **SPA Routing**: Proper client-side routing requires configuring the Spring Boot backend with a fallback mechanism (e.g., a dedicated SPA controller) to ensure all non-API requests return `index.html`.