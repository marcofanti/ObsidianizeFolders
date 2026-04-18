---
file_path: demo-stitch/package-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: This file serves as a comprehensive lock file, recording the exact versions and dependencies required for the `finance-app` project to ensure reproducible build environments across different machines and times.

**What it does**:
- Records the complete dependency graph, including nested packages, to guarantee that every component used during compilation and runtime is locked to a specific version.
- Defines the foundational structure of the application using key dependencies like React, React Router, and TypeScript.
- Manages build tooling versions (Vite, SWC, PostCSS, Tailwind CSS) and their required processors to ensure consistent compile-time behavior.

**Key exports**:
- **react**: Core library for building user interfaces (UI).
- **react-dom**: Provides DOM-specific utilities for React to render components in a web browser.
- **react-router-dom**: Handles client-side routing, allowing the application to manage different views within a single page structure.
- **vite**: The primary build tool/dev server used for bundling and optimizing the application assets.
- **tailwindcss**: A utility-first CSS framework used for rapid and constrained styling development.
- **typescript**: Provides static typing for the codebase, enhancing developer tooling and reliability.

**Gotchas**:
- **Mutability Risk**: This file must *never* be manually edited. Changes must only be applied through the package manager (`npm install` or `npm update`) to maintain the integrity of the dependency graph.
- **Verbosity**: The lock file is extremely verbose, listing every package (including numerous platform-specific binaries for build tools like `@esbuild` and `@swc/core`) and their full checksums/integrity hashes.
- **Build Tool Depth**: The presence of deeply nested, platform-specific packages (e.g., `@esbuild/linux-arm64`, `@rollup/rollup-darwin-x64`) indicates a complex, cross-platform build pipeline relying on compiled native code for optimal performance.