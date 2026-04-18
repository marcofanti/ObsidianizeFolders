---
file_path: testclaude/CLAUDE.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: Provides comprehensive guidance and architectural documentation for bootstrapping and running two versions of a SecureBank financial demo application (Auth0-based and standalone Spring Boot).

**What it does**:
- Details the required components, technologies, and workflow for setting up a React/TypeScript application secured by Auth0.
- Documents two complete, self-contained Spring Boot/React setups (`securebank/` and `securebank2/`) which use session cookies for authentication, requiring a two-terminal development setup (backend and frontend).
- Specifies critical architectural patterns, such as conditional rendering (`isLoading → isAuthenticated → render`) and the use of in-memory data stores for demo purposes.

**Key exports**:
- **Tech Stacks**: Defines three distinct technology stacks: React/TypeScript/Vite (for frontend), Java 21/Spring Boot 3.3.2 (for backend), and Auth0 (for OAuth authentication).
- **Development Workflows**: Provides specific `npm` and `mvn` command sequences for both Auth0 and standalone Spring Boot versions, detailing the necessary port configurations (8080/5173) and proxy settings.
- **Authentication Patterns**: Outlines advanced Spring Security patterns for programmatic session management (`SecurityContextRepository`) and efficient React state management (`useAuth.tsx` context).

**Gotchas**:
- **Development Complexity**: Both standalone Spring Boot versions require a two-terminal development process (one for the backend running `mvn spring-boot:run`, and one for the frontend running `npm run dev`).
- **Data Scope**: The application demo data (accounts, transactions) is hardcoded in the client-side components (`Dashboard.tsx`) or stored in an in-memory `ConcurrentHashMap` (`UserRepository.java`) and is not backed by a persistent database.
- **Auth vs. Standalone**: Users must differentiate between the Auth0 flow (which requires `VITE_AUTH0_DOMAIN` environment variables) and the standalone Spring Boot flow (which relies solely on Spring Security session cookies and internal logic).
- **Proxy Caveats**: For the standalone Spring Boot setup, the development environment relies on Vite proxies for API calls, which requires careful configuration to ensure session cookies are correctly forwarded (especially noting that the `credentials: true` option is *not* needed/valid for the Vite proxy).