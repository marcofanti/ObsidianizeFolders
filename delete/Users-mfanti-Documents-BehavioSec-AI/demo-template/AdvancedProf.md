---
file_path: demo-template/AdvancedProf.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This file provides a detailed prompt and step-by-step guide for integrating an advanced user behavioral profiling service (ThreatMetrix/BehavioSec) into a functional React/Vite/TypeScript application.

**What it does**:
- Requires the user to first supply mandatory configuration values: a unique ThreatMetrix `org_id` and a descriptive application `page_id` prefix.
- Sets up the integration by copying a static profiling client library and loading it globally in the `index.html`.
- Creates a TypeScript ambient declaration to ensure type safety for the global profiling API (`threatmetrix`).
- Implements a custom `useProfiling` React hook that manages the generation of a stable, session-specific UUID (`session_id`) for the profiling calls.
- Wraps the core profiling call in a guarded function that prevents runtime errors if the profiling script is blocked (e.g., by an adblocker).
- Triggers the profiling process on the initial mount of critical application pages (login, signup, dashboard, etc.).

**Key exports**:
- **`useProfiling`**: A custom React hook used within application components to access profiling functionality.
- **`profile`**: The function exposed by `useProfiling` that calls the backend API, requiring the page-specific ID and the stable session UUID.
- **`ThreatMetrix`**: The global API interface used by the client library, defining the method signature for profiling.

**Gotchas**:
- **Mandatory Prerequisite**: The process cannot proceed until the user provides both the `org_id` and the `page_id` prefix; using placeholder strings is forbidden.
- **Session ID Stability**: The generated `session_id` must be stable across component re-renders but must be refreshed whenever the entire page is reloaded.
- **Defensive Coding**: The implementation of the `useProfiling` hook must include a runtime check (`typeof threatmetrix !== 'undefined'`) to prevent application crashes if the profiling script is inaccessible.
- **API Domain**: The default domain (`h.online-metrix.net`) must be manually replaced if the organization uses a self-hosted SSL domain for Enhanced Profiling.