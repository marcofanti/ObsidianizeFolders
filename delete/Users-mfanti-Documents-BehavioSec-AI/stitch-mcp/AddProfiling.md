---
file_path: stitch-mcp/AddProfiling.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This runbook guides the integration of an Advanced Profiling tool (ThreatMetrix / BehavioSec) into an existing React/Vite/TypeScript application by implementing client-side JavaScript and TypeScript hooks.

**What it does**:
- Verifies and installs a required external profiling client library (`ln/fp-clientlib-v6_0.js`) as a static asset.
- Collects mandatory configuration parameters (`org_id`, `api_key`, `domain`, etc.) from environment files or user input.
- Creates a core `useProfiling` hook to initialize the profiling service with a unique, stable session ID and track page views.
- Implements `useSessionQuery` hook to execute the necessary API call after successful login to log the user's session credentials.
- Instruments key authentication pages (`LoginPage`, `SignUpPage`, `PasswordResetPage`) with hooks to ensure profiling runs on critical user paths.

**Key exports**:
- **`useProfiling`**: A React hook providing a `profile(pageId)` function to trigger page-specific profiling requests and managing the core session ID.
- **`getSessionId`**: A getter function that retrieves the current module-level, stable session ID.
- **`refreshSessionId`**: A function used to generate and assign a new unique session ID, ensuring freshness for subsequent profiling actions.
- **`useSessionQuery`**: A React hook exposing a `querySession(username)` function that sends the user credentials to the backend profile service via a secure API call.

**Gotchas**:
- **Environment Priority**: Configuration parameters must be sought in the application's `.env` file first, then the project root `.env` file, to respect app-specific overrides.
- **CORS and Fetch**: The Session Query endpoint does not support browser origins, so the fetch request must use `mode: 'no-cors'`, and error handling must be fire-and-forget (only logging errors, not blocking flow).
- **Session ID Stability**: The session ID must be generated and stored in a module-level variable within the hook to remain stable across React re-renders while still being reset on a full page load.
- **Dependencies**: The core profiling function (`profile`) must be wrapped in `useCallback` with an empty dependency array (`[]`) to ensure its reference is stable for inclusion in `useEffect` dependency arrays.
- **Page ID Usage**: The `page_id` is a mandatory string parameter for profiling and must be explicitly passed to the profile function in the page components' `useEffect`.
- **Directory Isolation**: All code changes must be strictly confined to the `{webdir}` and must not alter the application's layout, styles, or existing authentication logic.