---
file_path: Demo/gemini.md
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: md
---

**Purpose**: This document outlines the technical steps taken to scaffold, style, and populate a React/TypeScript web application using modern front-end techniques.

**What it does**:
- Initializes a React/TypeScript Vite project structure.
- Implements global, dark-mode styling using CSS variables and ambient gradients.
- Creates a reusable "glassmorphism" effect using the `.glass` utility class.
- Builds a complete landing page UI featuring a hero section, responsive feature grids, and animated Call-to-Action (CTA) components.
- Verifies the application's build integrity by running a successful build command (`npm run build`).

**Key exports**:
- `.glass` utility class: Provides a highly polished, translucent, and blurred "glassmorphism" aesthetic.
- `App.tsx` / Landing Page Structure: Custom React component that replaces boilerplate with a structured "Nova Platform" landing page, featuring three main value propositions.
- `.cta-button`: A styled, animated button component featuring a sliding gradient overlay on hover.
- Global CSS Variables: Establishes a consistent, themeable color palette (`--bg-color`, `--text-main`, etc.) across the entire application.

**Gotchas**:
- The initial Vite development server might temporarily switch ports (e.g., from 5173 to 5174) during the setup process.
- The structure relies heavily on modern CSS properties (like `backdrop-filter`) for its stylistic effects.