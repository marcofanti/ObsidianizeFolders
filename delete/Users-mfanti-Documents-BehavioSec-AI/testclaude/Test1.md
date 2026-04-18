---
file_path: testclaude/Test1.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: To design and implement a modern, secure, standalone user authentication and financial dashboard application using Java Spring Boot, Spring Security, and a React SPA frontend.

**What it does**:
- Creates a complete user authentication flow including login, signup, password verification, and error handling.
- Provides a landing page styled like a modern financial application.
- Displays a demo bank account dashboard page upon successful login.
- Uses an in-memory database for user data storage.
- Implements session-based authentication utilizing Spring Security session cookies.

**Key exports**:
- **Application Structure**: A full-stack application served by Spring Boot (Java/Spring Boot) with a separate React/TypeScript SPA frontend.
- **Database**: Initialization of the in-memory database with specific demo users, including 'mfanti@behaviosec.com' and password '0cramItnaf!'.
- **Authentication**: A secure, session-based authentication mechanism managed by Spring Security.

**Gotchas**:
- The setup must explicitly use React SPA for the frontend (not Thymeleaf or Vaadin).
- The build tool must be Maven, and the project must run using `mvn spring-boot:run`.
- **Exclusions**: Do not include `frontend-maven-plugin` or `maven-resources-plugin` blocks in the `pom.xml`.
- **CORS/Proxy Warning**: For `vite.config.ts`, do not set `credentials: true`, as cookies are automatically forwarded by the proxy.
- **Constraint**: All references to external identity providers (Auth0 and Okta) must be removed, ensuring the application is standalone.