---
file_path: stitch-mcp/README_PROFILING.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document serves as a detailed setup guide for integrating the ThreatMetrix/BehavioSec Advanced Profiling toolkit into a React + Vite + TypeScript application using an automated, step-by-step runbook.

**What it does**:
- **Device Profiling**: Silently fingerprints the user's browser and device on critical pages (login, signup, password reset) and sends this data to the ThreatMetrix risk analysis network.
- **Session Risk Query**: Immediately following a successful login, it executes a non-blocking query to the BehavioSec API using the session ID and username to retrieve an instant risk decision for the session.
- **Automated Setup**: The integration process is executed by a specialized Claude Code CLI runbook, which handles script copying, modification of `index.html`, creation of TypeScript definitions, and implementation of specific React hooks.
- **Non-Blocking Operation**: The profiling and session query logic is designed to continue application functionality even if blocked by adblockers or if the external API is unreachable.

**Key exports**:
- **`useProfiling` hook**: A stable React hook responsible for generating a unique session UUID (`session_id`) and exposing a stable `profile(pageId)` function for tracking device activity on key pages.
- **`useSessionQuery` hook**: A hook that constructs the Session Query URL, optimistically writes the username to `sessionStorage`, and executes the API fetch request upon successful login.
- **`fp-clientlib-v6_0.js`**: The core, non-modifiable ThreatMetrix profiling library that is copied into the application's public directory.

**Gotchas**:
- **Prerequisite File**: The integration requires the specific file `ln/fp-clientlib-v6_0.js` to exist in the project root before the setup can begin.
- **Authentication Flow**: The session query hook must use `mode: 'no-cors'` when calling the BehavioSec API because the endpoint does not emit CORS headers that allow browser origins.
- **Data Persistence**: The username used for the session query is written to `sessionStorage` optimistically *before* the network request is made.
- **Technical Dependencies**: The entire process relies on running a specific Claude CLI runbook (`Follow AddProfiling.md`) to correctly modify multiple files and maintain complex hook dependencies (`useCallback` and `useEffect` dependency arrays).
- **Configuration Handling**: While the runbook checks both project-wide (`<root>/.env`) and app-specific (`{webdir}/.env`) environment files, the `api_key` is always mandatorily prompted during setup.