---
file_path: stitch-mcp/design-banking.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document serves as a comprehensive design specification for a single-page React application simulating a modern, mobile-first personal banking dashboard.

**What it does**:
- Simulates key banking operations, including account viewing, transaction tracking, funds transfer, and bill payments.
- Manages user authentication flows (Login, Sign Up, Password Reset) using client-side mock data.
- Presents a detailed financial dashboard summarizing net worth, spending habits (via donut chart), upcoming bills, and multiple linked accounts.
- Provides a structured UI using established industry best practices (e.g., using deep navy and gold for trust and premium service).

**Key exports**:
- **AccountCard**: A reusable component used to display core banking information, including account type, balance, and associated actions (View Details, Transfer).
- **BottomNavBar**: A persistent navigation component optimized for mobile usability, linking to primary views (Home, Accounts, Transfer, Cards, Profile).
- **Financial Dashboard Structure**: A comprehensive template incorporating quick actions, a summary donut chart, and segmented tab views (Overview, Accounts, Transactions).

**Gotchas**:
- **Client-Side Mocking**: The entire application, including all financial data and transactions, is hardcoded/demo and does not connect to a live backend API.
- **Authentication is Mocked**: The authentication process uses `localStorage` and is designed to simulate protected routes, but it is not secure in a production environment.
- **Mobile-First Design**: The layout and navigation (BottomNavBar) are specifically engineered for a 390px viewport width, requiring developers to maintain mobile constraints during implementation.