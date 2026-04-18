---
file_path: demo-stitch/scripts/validate.js
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: js
---

**Purpose**: This script validates a provided component file, ensuring it contains a required Props interface and does not use hardcoded hex color values in its JSX class names.

**What it does**:
- Reads and parses the contents of a TypeScript/TSX component file using `@swc/core`.
- Traverses the Abstract Syntax Tree (AST) to check for two specific code quality rules:
    - **Props Interface**: Verifies the existence of a `TsInterfaceDeclaration` whose identifier ends with the string "Props".
    - **Hardcoded Colors**: Detects any JSX attributes where the `className` value contains a pattern matching a six-digit hexadecimal color code (e.g., `#AABBCC`).
- Reports success or failure to the console based on whether both criteria are met, exiting with status code 0 on success and 1 on failure.

**Key exports**:
- None (This is a standalone CLI script that executes the `validateComponent` function on command line arguments.)

**Gotchas**:
- The script requires the file path to be passed as a command line argument (`process.argv[2]`).
- It relies on the `@swc/core` library and expects the target file to be valid TypeScript or TSX.
- The definition of a "Props interface" is strictly enforced: the interface must be a `TsInterfaceDeclaration` and its name must end exactly with the substring 'Props'.
- Only hardcoded hex color values (`#RRGGBB`) are flagged; other color formats (like `red` or `var(--color)`) are ignored.