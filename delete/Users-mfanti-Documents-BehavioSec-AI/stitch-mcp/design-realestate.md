---
file_path: stitch-mcp/design-realestate.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document outlines the architecture and design specifications for a client-side Single Page Application (SPA) simulating a real estate agent dashboard.

**What it does**:
- Provides a fully navigable, multi-page mock dashboard experience using React Router v6.
- Implements a comprehensive, mock authentication flow (`useAuth.tsx`) that uses `localStorage` for session persistence.
- Displays a structured main dashboard view combining property listings, market insights, and activity history, all using hardcoded demo data.
- Manages routing access, ensuring that the `/dashboard` page is protected and redirects unauthenticated users to the login screen.

**Key exports**:
- `useAuth.tsx`: Provides the authentication context and mock functions for login, signup, and logout.
- `App.tsx`: Serves as the root component, managing the routing structure and protecting key routes with auth guards.
- `DEMO_PROPERTIES`: Hardcoded constant array used to populate the property listing section of the dashboard.
- `AuthProvider`: Wraps the application to make the current authentication state globally accessible via React Context.

**Gotchas**:
- **Client-Only/No Backend**: All data (properties, activities) is hardcoded demo data; the application does not communicate with a real API.
- **Mock Authentication**: The authentication logic is a mock implementation. While structure-ready for a service like Auth0, it does not include real validation or backend storage.
- **Local Tab State**: The tab selection within the main dashboard (`Dashboard.tsx`) is managed only by local React state (`useState`) and is not linked to the URL, making deep linking to specific dashboard tabs impossible without modifications.