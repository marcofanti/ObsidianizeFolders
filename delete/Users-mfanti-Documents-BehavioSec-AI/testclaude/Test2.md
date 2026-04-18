---
file_path: testclaude/Test2.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file specifies the technical requirements and architecture for building a complete, modern single-page application (SPA) simulating a financial banking dashboard, including full user authentication and account management capabilities.

**What it does**:
- Initializes a multi-folder project structure containing dedicated frontend (React/TypeScript) and backend (Java/Spring Boot) modules.
- Implements a comprehensive user authentication flow (login, signup, password verification, and error handling) secured using Spring Security session cookies.
- Provides the UI structure for a financial dashboard, reusing component styles from existing template files.
- Manages user data using a simple in-memory database for development simplicity.
- Specifies build constraints and the required technology stack (Java/SpringBoot, React/TypeScript, Maven).

**Key exports**:
- **Architecture**: A decoupled application structure where Spring Boot serves the static React SPA content.
- **Authentication**: A session-based, standalone authentication system using Spring Security (no reliance on external identity providers like Okta or Auth0).
- **Initial Data**: The system must be initialized with a primary user account ('mfanti@behaviosec.com') and several other demo users.
- **Build Configuration**: Defines the use of Maven as the primary build tool, specifically omitting the `frontend-maven-plugin` and `maven-resources-plugin` blocks.

**Gotchas**:
- **Database Limitation**: Data storage must be limited to an in-memory database.
- **Build System Constraint**: When running the application, only `mvn spring-boot:run` should execute, avoiding plugins that complicate the build lifecycle.
- **Vite Configuration**: The `vite.config.ts` file must not include `credentials: true`, as cookie forwarding occurs automatically via the proxy mechanism.
- **Technology Scope**: The implementation must strictly exclude all references or dependencies on third-party identity management services (Auth0 and Okta).