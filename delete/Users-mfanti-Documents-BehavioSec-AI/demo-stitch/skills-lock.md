---
file_path: demo-stitch/skills-lock.json
project: Users-mfanti-Documents-BehavioSec-AI
last_updated: 2026-04-18
language: json
---

**Purpose**: Defines a reproducible dependency graph (manifest) for required development skills, ensuring that the build uses exact, locked versions of external code components.

**What it does**:
- Registers component dependencies under the `skills` object, using scoped identifiers (e.g., `react:components`).
- Specifies the external `source` and `sourceType` (e.g., `github`) for the dependency.
- Locks the dependency version using a `computedHash`, guaranteeing that the build only proceeds if the source code matches this cryptographic hash.

**Key exports**:
- `react:components`: Defines a dependency on the React components skill, sourcing it from the `google-labs-code/stitch-skills` repository on GitHub.

**Gotchas**:
- The file is a strict lockfile; changing the source code in the defined repository requires manually updating the `computedHash` within this file to maintain build integrity.
- If the hash calculation fails to match the current state of the source repository, the build process will fail immediately, regardless of whether the source repository itself is technically functional.