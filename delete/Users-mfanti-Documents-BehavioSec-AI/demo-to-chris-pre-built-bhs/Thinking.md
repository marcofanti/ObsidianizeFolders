---
file_path: demo-to-chris-pre-built-bhs/Thinking.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file outlines the architectural design and implementation plan for a full-stack, session-based personal banking web application, built using Spring Boot and React/TypeScript.

**What it does**:
- Manages user authentication through custom API endpoints for login, signup, and logout, utilizing Spring Security session cookies.
- Serves a dynamic Single Page Application (SPA) frontend (React/TypeScript) built into the Spring Boot static resources.
- Provides REST endpoints to fetch demo bank account and transaction data, simulating a core banking service.
- Implements protected routing logic on the frontend, ensuring access to sensitive features requires a valid user session.

**Key exports**:
- **Spring Boot Backend**: The secure API layer (Java/Spring Boot) handling authentication logic, user persistence, and data retrieval.
- **REST API Endpoints**: Includes core endpoints like `/api/auth/login`, `/api/auth/me` (current user), and data endpoints like `/api/accounts` and `/api/transactions`.
- **React Frontend**: The user interface built with TypeScript and Vite, encompassing the landing page, login, signup, and dashboard views.
- **Auth Context/Hook**: A React state management mechanism responsible for handling the user's session state and orchestrating API calls for authentication flow.

**Gotchas**:
- **Build Complexity**: The project requires a dual build pipeline: using the Maven Frontend Plugin to compile the React/Vite SPA and embedding the resulting static assets into the final Spring Boot JAR package.
- **Session Management**: Authentication is strictly session-based, relying on Spring Security to manage the `SecurityContext` and corresponding cookies.
- **Cross-Origin Handling**: Development requires configuring a Vite proxy to tunnel API calls to the backend (8080) to avoid complex CORS and SameSite cookie issues between the frontend (5173) and backend origins.
- **Security**: Passwords must be hashed using BCrypt, and while CSRF protection is initially disabled for the demo, the plan acknowledges the necessity of implementing proper cookie-based CSRF token handling in production.