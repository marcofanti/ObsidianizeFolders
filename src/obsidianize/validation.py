from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.table import Table
from rich import box

from obsidianize.config import Config

console = Console()

VALID_PROVIDERS = ("gemini", "ollama", "openai")


def validate_config(config: Config) -> list[str]:
    """Return a list of human-readable error messages. Empty list means config is valid."""
    errors: list[str] = []

    # ── Vault path ───────────────────────────────────────────────────────────
    if not config.vault_path.exists():
        errors.append(
            f"Vault path does not exist: [bold]{config.vault_path}[/bold]\n"
            f"  → Set OBSIDIAN_VAULT_PATH in your .env to a valid directory."
        )
    elif not config.vault_path.is_dir():
        errors.append(
            f"Vault path is not a directory: [bold]{config.vault_path}[/bold]\n"
            f"  → OBSIDIAN_VAULT_PATH must point to a folder, not a file."
        )

    # ── LLM provider ─────────────────────────────────────────────────────────
    if config.llm_provider not in VALID_PROVIDERS:
        errors.append(
            f"Unknown LLM provider: [bold]{config.llm_provider!r}[/bold]\n"
            f"  → LLM_PROVIDER must be one of: {', '.join(VALID_PROVIDERS)}"
        )
        return errors  # remaining checks are provider-specific, skip them

    # ── Model name ───────────────────────────────────────────────────────────
    if not config.llm_model:
        errors.append(
            "LLM_MODEL is not set.\n"
            f"  → Example for {config.llm_provider}: "
            + {"gemini": "gemini-2.0-flash", "openai": "gpt-4o-mini", "ollama": "llama3.2"}.get(
                config.llm_provider, "<model-name>"
            )
        )

    # ── API key (cloud providers) ─────────────────────────────────────────────
    if config.llm_provider in ("gemini", "openai") and not config.llm_api_key:
        errors.append(
            f"LLM_API_KEY is required for provider [bold]{config.llm_provider}[/bold] but is not set.\n"
            f"  → Add LLM_API_KEY=<your-key> to your .env file."
        )

    # ── Ollama-specific ───────────────────────────────────────────────────────
    if config.llm_provider == "ollama":
        if not config.ollama_model:
            errors.append(
                "OLLAMA_MODEL is not set.\n"
                "  → Example: OLLAMA_MODEL=llama3.2"
            )
        else:
            err = _check_ollama_connection(config)
            if err:
                errors.append(err)

    return errors


def _check_ollama_connection(config: Config) -> Optional[str]:
    """Return an error string if Ollama is unreachable or the model is not pulled."""
    try:
        import ollama as ol
        client = ol.Client(host=config.ollama_base_url)
        response = client.list()
        pulled = [m.model for m in response.models]
        # Check if configured model (or a prefix of it) is available
        model_base = config.ollama_model.split(":")[0]
        if pulled and not any(model_base in m for m in pulled):
            pulled_str = ", ".join(pulled) or "(none)"
            return (
                f"Ollama model [bold]{config.ollama_model}[/bold] is not available.\n"
                f"  → Pulled models: {pulled_str}\n"
                f"  → Run: ollama pull {config.ollama_model}"
            )
        return None
    except Exception as exc:
        return (
            f"Cannot reach Ollama at [bold]{config.ollama_base_url}[/bold]: {exc}\n"
            f"  → Is Ollama running? Start it with: ollama serve"
        )


def mask_key(key: Optional[str]) -> str:
    if not key:
        return "[dim](not set)[/dim]"
    if len(key) <= 8:
        return "[dim]***[/dim]"
    return f"{key[:4]}[dim]...{key[-4:]}[/dim]"


def print_config_summary(config: Config) -> None:
    """Print a formatted configuration summary, masking sensitive values."""
    table = Table(
        title="obsidianize configuration",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
        title_style="bold",
    )
    table.add_column("Setting", style="cyan", no_wrap=True)
    table.add_column("Value")

    table.add_row("Vault path", str(config.vault_path))
    table.add_row("LLM provider", config.llm_provider)

    if config.llm_provider == "ollama":
        table.add_row("Ollama URL", config.ollama_base_url)
        table.add_row("Ollama model", config.ollama_model)
    else:
        table.add_row("Model", config.llm_model)
        table.add_row("API key", mask_key(config.llm_api_key))

    table.add_row("Include extensions", ", ".join(config.include_extensions))
    table.add_row("Exclude dirs", ", ".join(config.exclude_dirs))
    table.add_row(
        "Max index entries",
        str(config.max_index_entries) if config.max_index_entries > 0 else "unlimited",
    )

    console.print(table)


def check_and_confirm(config: Config, db_path: Path) -> bool:
    """
    Validate config and, on first run, print a summary and ask for confirmation.
    Returns True if it's safe to proceed, False if the user should abort.
    """
    errors = validate_config(config)
    if errors:
        console.print("\n[bold red]Configuration errors:[/bold red]")
        for err in errors:
            console.print(f"  [red]✗[/red] {err}")
        console.print(
            "\n[dim]Fix the issues above in your [bold].env[/bold] file and try again.[/dim]\n"
        )
        return False

    first_run = not db_path.exists()
    if first_run:
        console.print("\n[bold yellow]First run detected — no database found.[/bold yellow]")
        console.print("Please confirm your configuration before proceeding:\n")
        print_config_summary(config)
        console.print()
        confirmed = console.input(
            "[bold]Proceed with this configuration?[/bold] [dim][y/N][/dim] "
        ).strip().lower()
        if confirmed != "y":
            console.print("[yellow]Aborted.[/yellow]")
            return False

    return True
