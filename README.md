# obsidianize

An agentic CLI tool that documents your project directories as distilled knowledge notes in your [Obsidian](https://obsidian.md) vault. Point it at any project folder and it generates structured summaries for every important file, wires up dependency links between notes, and keeps everything in sync as your code changes.

---

## Features

- **AI-powered summaries** — Each file is summarized by an LLM into a structured note: Purpose, What it does, Key exports, and Gotchas.
- **Smart incremental sync** — MD5 hashing and SQLite tracking ensure only new or modified files are re-processed.
- **Move detection** — When a file is moved within a project, its vault note is renamed instead of re-generated.
- **Archival** — Deleted files have their notes moved to an `Archive/` subfolder, preserving your insights.
- **Dependency graph** — Python, JS, and TS imports are parsed and turned into Obsidian `[[wikilinks]]` between notes.
- **Mirrored vault structure** — Root subdirectories become vault subfolders, so the vault layout reflects your project's top-level structure.
- **Multi-provider LLM** — Works with Gemini, OpenAI, or a local Ollama model.
- **Streamlit UI** — Optional web dashboard for managing projects and settings without the terminal.

---

## Vault Structure

Given a project at `/Users/alice/Projects/MyApp`, obsidianize creates:

```
{vault_root}/
├── obsidianize.db
└── Users-alice-Projects-MyApp/
    ├── _index.md                  ← all notes, grouped by subfolder
    ├── main.md                    ← root-level files
    ├── Archive/
    │   └── old-module.md          ← notes for deleted files
    └── src/
        ├── _index.md
        ├── api.md
        └── utils.md
```

Each note contains YAML frontmatter and a structured summary:

```markdown
---
file_path: src/api.py
project: Users-alice-Projects-MyApp
last_updated: 2026-04-18
language: py
---

**Purpose**: Handles all REST API routing for the application.

**What it does**:
- Defines FastAPI routes for /users, /auth, and /data endpoints
- Validates request bodies using Pydantic models

**Key exports**:
- `router`: FastAPI APIRouter instance
- `get_current_user`: dependency injection helper

**Gotchas**:
- Auth middleware must be applied before mounting this router

## Dependencies
- [[models]]
- [[auth]]
```

---

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- An LLM provider: Gemini API key, OpenAI API key, or a running [Ollama](https://ollama.com) instance

---

## Installation

```bash
# Clone the repo
git clone https://github.com/marcofanti/ObsidianizeFolders.git
cd ObsidianizeFolders

# Install dependencies with uv
uv sync

# Or with pip
pip install -e .
```

---

## Configuration

Copy `.env.example` to `.env` and fill in your settings:

```bash
cp .env.example .env
```

```env
# Required
OBSIDIAN_VAULT_PATH=/path/to/your/obsidian/vault

# LLM provider: gemini | ollama | openai
LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.0-flash
LLM_API_KEY=your-api-key-here

# Ollama (only needed if LLM_PROVIDER=ollama)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Scanning
INCLUDE_EXTENSIONS=.py,.js,.ts,.md,.txt,.yaml,.toml,.json,.sh
EXCLUDE_DIRS=node_modules,.git,__pycache__,.venv,dist,build
MAX_INDEX_ENTRIES=50   # 0 = unlimited

# Optional: override the default summary prompt
SUMMARY_PROMPT_TEMPLATE=
```

### Provider setup

**Gemini**
1. Get an API key from [Google AI Studio](https://aistudio.google.com)
2. Set `LLM_PROVIDER=gemini`, `LLM_MODEL=gemini-2.0-flash`, `LLM_API_KEY=<key>`

**OpenAI**
1. Get an API key from [platform.openai.com](https://platform.openai.com)
2. Set `LLM_PROVIDER=openai`, `LLM_MODEL=gpt-4o-mini`, `LLM_API_KEY=<key>`

**Ollama (local, no API key)**
1. Install Ollama and pull a model: `ollama pull llama3.2`
2. Set `LLM_PROVIDER=ollama`, `OLLAMA_MODEL=llama3.2`

---

## CLI Usage

All commands are available via `obsidianize` (or `uv run obsidianize` if not installed globally).

### Register a project and generate notes

```bash
obsidianize add /path/to/your/project
```

Registers the project, scans all important files, sends each to the LLM, and writes notes to your vault. Safe to re-run — already-registered projects are synced instead.

### Sync all projects

```bash
obsidianize sync
```

Re-scans all registered projects. Only new or modified files are processed. Handles moves, deletes, and archival automatically.

### Sync a specific project

```bash
obsidianize sync /path/to/your/project
```

### Show all registered projects

```bash
obsidianize status
```

```
 Project Root                          Vault Folder                            Files  Last Sync
 /Users/alice/Projects/MyApp           Users-alice-Projects-MyApp              42     2026-04-18
 /Users/alice/Projects/OtherApp        Users-alice-Projects-OtherApp           17     2026-04-17
```

### Remove a project

```bash
obsidianize remove /path/to/your/project
```

Unregisters the project and moves all its notes to `Archive/`.

---

## Streamlit UI

For a visual interface, launch the dashboard:

```bash
uv run streamlit run src/obsidianize/ui/app.py
```

The UI provides:
- **Dashboard tab** — lists all registered projects with file counts and last sync time; add new projects; trigger syncs with one click.
- **Settings tab** — edit all `.env` configuration values through a form; changes are saved back to `.env`.

---

## Scanning Rules

- **Depth**: root-level files + files in immediate subdirectories + files one level deeper within those subdirectories (3 levels total from root).
- **Included extensions** (configurable): `.py .js .ts .md .txt .yaml .toml .json .sh`
- **Always excluded**: `node_modules .git __pycache__ .venv dist build`
- Root subdirectories become vault subfolders. Files deeper than one level within a subdir are placed flat inside that vault subfolder.

---

## How Sync Works

1. **Scan** — Walk the project directory and collect all important files with their MD5 hashes.
2. **Diff** — Compare hashes against the SQLite database to classify each file as new, modified, moved, deleted, or unchanged.
3. **Analyze**:
   - New/modified → sent to LLM for summarization; imports parsed into wikilinks.
   - Moved → vault note renamed; no LLM call needed.
   - Deleted → vault note archived to `Archive/`.
   - Unchanged → skipped.
4. **Document** — Notes written to vault, indices rebuilt.

If an LLM call fails, the file is skipped and logged. It will be retried on the next sync.

---

## Project Structure

```
obsidianize/
├── pyproject.toml
├── .env.example
├── DECISIONS.md          ← design trade-offs and open decisions
└── src/obsidianize/
    ├── cli.py            ← Typer CLI entrypoint
    ├── config.py         ← .env loading and Config dataclass
    ├── db.py             ← SQLite state management
    ├── scanner.py        ← directory walk, filtering, hashing
    ├── llm.py            ← Gemini / Ollama / OpenAI dispatch
    ├── imports.py        ← import parsing and wikilink resolution
    ├── notes.py          ← note writing, indexing, archival
    ├── sync.py           ← pipeline orchestration
    └── ui/
        └── app.py        ← Streamlit dashboard
```

---

## Inspiration & Prior Art

This project sits at the intersection of two ideas gaining traction in the AI-native productivity space:

**[Andrej Karpathy's llm-wiki](https://github.com/karpathy/llm-wiki)** — The concept of using an LLM to build a personal, queryable wiki from raw inputs. obsidianize applies this idea to source code: instead of ingesting notes and articles, it ingests project directories and distills them into structured knowledge.

**[Claudeopedia](https://x.com/alliekmiller) by [Allie K. Miller](https://x.com/alliekmiller)** — Miller's "second brain" system built inside Claude Code, combining Obsidian, GitHub, and AI skills to move from chat-style AI interaction to an always-on operating system for knowledge. Her `/wiki` skill for rapid knowledge capture and the master context document pattern directly influenced the design of obsidianize's vault structure and note format. The goal is the same: stop re-explaining context to your AI, and start building a persistent, structured layer it can always reference.

obsidianize takes these ideas and focuses them on a specific pain point: **your codebase**. Every project you work on deserves a distilled knowledge layer — one that travels with your vault, links to your other notes, and updates itself as your code evolves.

---

## Open Design Decisions

See [`DECISIONS.md`](DECISIONS.md) for documented trade-offs that may be revisited:

- **Subfolder depth** — currently mirrors one level; full recursion is possible.
- **Note naming collisions** — files with the same stem in different subdirs overwrite each other (last write wins).
- **Root index content** — currently lists all notes grouped by subfolder; could instead link only to subfolder indices.
