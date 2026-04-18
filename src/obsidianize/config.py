from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import os

from dotenv import load_dotenv

load_dotenv()

DEFAULT_PROMPT = """\
You are a technical documentation expert. Analyze the following source file and produce a structured summary.

Return EXACTLY this format (omit a section only if it truly does not apply):

**Purpose**: One sentence describing what this file does.

**What it does**:
- bullet point describing key behavior

**Key exports**:
- name: brief description

**Gotchas**:
- any notable caveats, quirks, or important patterns

File: {file_path}
```
{content}
```"""


@dataclass
class Config:
    vault_path: Path
    llm_provider: str
    llm_model: str
    llm_api_key: Optional[str]
    ollama_base_url: str
    ollama_model: str
    include_extensions: list[str]
    exclude_dirs: list[str]
    max_index_entries: int
    summary_prompt_template: str


def load_config() -> Config:
    vault_path_str = os.getenv("OBSIDIAN_VAULT_PATH", "")
    if not vault_path_str:
        raise ValueError("OBSIDIAN_VAULT_PATH is not set. Add it to your .env file.")

    include_ext = os.getenv("INCLUDE_EXTENSIONS", ".py,.js,.ts,.md,.txt,.yaml,.toml,.json,.sh")
    exclude_dirs = os.getenv("EXCLUDE_DIRS", "node_modules,.git,__pycache__,.venv,dist,build")
    prompt = os.getenv("SUMMARY_PROMPT_TEMPLATE", "").strip() or DEFAULT_PROMPT

    return Config(
        vault_path=Path(vault_path_str),
        llm_provider=os.getenv("LLM_PROVIDER", "gemini"),
        llm_model=os.getenv("LLM_MODEL", "gemini-2.0-flash"),
        llm_api_key=os.getenv("LLM_API_KEY") or None,
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        ollama_model=os.getenv("OLLAMA_MODEL", "llama3.2"),
        include_extensions=[e.strip() for e in include_ext.split(",") if e.strip()],
        exclude_dirs=[d.strip() for d in exclude_dirs.split(",") if d.strip()],
        max_index_entries=int(os.getenv("MAX_INDEX_ENTRIES", "50")),
        summary_prompt_template=prompt,
    )
