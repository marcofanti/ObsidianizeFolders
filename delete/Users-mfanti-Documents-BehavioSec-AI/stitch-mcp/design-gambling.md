---
file_path: stitch-mcp/design-gambling.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document outlines the architecture for a client-side, single-page application (SPA) simulating an online gambling and sports betting dashboard using a mock authentication system and hardcoded demo data.

**What it does**:
- Simulates a full betting platform experience (Sports/Casino/Bet History) using a rich, multi-section dashboard layout.
- Handles client-side routing, providing public access pages (Login, Signup, etc.) and a protected dashboard area.
- Provides a mock authentication layer that manages session state using `localStorage` without connecting to a real backend.
- Displays complex, structured demo data for bankroll, active bets, and performance insights, mimicking real API responses.

**Key exports**:
- `App.tsx`: Manages the root routing structure, incorporating auth guard logic to redirect unauthenticated users from the `/dashboard` path.
- `useAuth.tsx`: Provides the central `AuthProvider` context, managing mock user session state (login, signup, logout) using `localStorage`.
- `Dashboard.tsx`: The main protected component that houses the layout, state management (`activeTab`), and display of all demo betting data.

**Gotchas**:
- **No Backend:** The entire application is client-side; all data (including user balances, bets, and odds) is hardcoded demo data.
- **Mock Auth Only:** The authentication system is a thin shim designed for quick iteration; real API swap points are explicitly marked for future integration.
- **State Management:** The tab state within the `Dashboard` is purely local (`useState`) and is not synchronized with the URL, meaning deep linking to specific tabs is not supported without enhancement.
- **Styling:** All styling is contained within a single `index.css` file, prohibiting the use of CSS modules or utility frameworks like Tailwind.