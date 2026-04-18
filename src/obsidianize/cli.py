from pathlib import Path
from typing import Optional

import typer
from rich import box
from rich.console import Console
from rich.table import Table

from obsidianize.config import Config, load_config
from obsidianize.db import Database
from obsidianize.notes import archive_note, vault_folder_name
from obsidianize.sync import SyncResult, sync_project
from obsidianize.validation import check_and_confirm

app = typer.Typer(
    name="obsidianize",
    help="Document your project directories as distilled knowledge notes in Obsidian.",
    no_args_is_help=True,
)
console = Console()


def _load_config() -> Config:
    """Load config, exiting with a friendly message if OBSIDIAN_VAULT_PATH is missing."""
    try:
        return load_config()
    except ValueError as exc:
        console.print(f"\n[bold red]Configuration error:[/bold red] {exc}")
        console.print("[dim]Copy .env.example to .env and fill in your settings.[/dim]\n")
        raise typer.Exit(1)


def _db(config: Config) -> Database:
    return Database(config.vault_path / "obsidianize.db")


def _print_result(result: SyncResult) -> None:
    if result.added:
        console.print(f"  [green]+{len(result.added)} added[/green]")
    if result.updated:
        console.print(f"  [yellow]~{len(result.updated)} updated[/yellow]")
    if result.moved:
        console.print(f"  [blue]→{len(result.moved)} moved[/blue]")
    if result.archived:
        console.print(f"  [dim]-{len(result.archived)} archived[/dim]")
    if result.unchanged:
        console.print(f"  [dim]{result.unchanged} unchanged[/dim]")
    if result.failed:
        console.print(f"  [red]{len(result.failed)} failed[/red]")
        for path, err in result.failed:
            console.print(f"    [red]{path}: {err}[/red]")


@app.command()
def add(
    path: Path = typer.Argument(..., help="Project root path to register and sync"),
) -> None:
    """Register a project path and run an initial sync."""
    config = _load_config()
    db_path = config.vault_path / "obsidianize.db"

    if not check_and_confirm(config, db_path):
        raise typer.Exit(1)

    db = _db(config)
    root = path.resolve()

    if not root.exists():
        console.print(f"\n[red]Project path does not exist:[/red] {root}")
        raise typer.Exit(1)
    if not root.is_dir():
        console.print(f"\n[red]Project path is not a directory:[/red] {root}")
        raise typer.Exit(1)

    folder = vault_folder_name(root)
    if db.get_project(str(root)):
        console.print(f"[yellow]Already registered:[/yellow] {root}")
    else:
        db.add_project(str(root), folder)
        console.print(f"[green]Registered:[/green] {root} → [dim]{folder}/[/dim]")

    console.print(f"\n[bold]Syncing[/bold] {root}…")
    result = sync_project(root, db, config)
    _print_result(result)


@app.command()
def sync(
    path: Optional[Path] = typer.Argument(None, help="Project to sync (omit to sync all)"),
) -> None:
    """Sync one or all registered projects."""
    config = _load_config()
    db_path = config.vault_path / "obsidianize.db"

    if not check_and_confirm(config, db_path):
        raise typer.Exit(1)

    db = _db(config)

    if path:
        root = path.resolve()
        if not db.get_project(str(root)):
            console.print(f"[red]Not registered: {root}. Run 'obsidianize add' first.[/red]")
            raise typer.Exit(1)
        projects = [db.get_project(str(root))]
    else:
        projects = db.list_projects()
        if not projects:
            console.print("[yellow]No projects registered.[/yellow]")
            raise typer.Exit(0)

    for project in projects:
        console.print(f"\n[bold]Syncing[/bold] {project.root_path}…")
        result = sync_project(Path(project.root_path), db, config)
        _print_result(result)


@app.command()
def remove(
    path: Path = typer.Argument(..., help="Project root path to unregister"),
) -> None:
    """Unregister a project and archive all its notes."""
    config = _load_config()

    if not check_and_confirm(config, config.vault_path / "obsidianize.db"):
        raise typer.Exit(1)

    db = _db(config)
    root = path.resolve()

    project = db.get_project(str(root))
    if not project:
        console.print(f"[red]Not registered: {root}[/red]")
        raise typer.Exit(1)

    vault_folder = config.vault_path / project.vault_folder
    files = db.get_active_files(project.id)
    archived = 0
    for f in files:
        note_path = vault_folder / f.vault_subdir / f.note_filename \
            if f.vault_subdir else vault_folder / f.note_filename
        if note_path.exists():
            archive_note(note_path, vault_folder)
            archived += 1

    db.remove_project(str(root))
    console.print(f"[green]Removed[/green] {root} — {archived} notes archived")


@app.command()
def status() -> None:
    """Show all registered projects and their last sync time."""
    config = _load_config()

    if not check_and_confirm(config, config.vault_path / "obsidianize.db"):
        raise typer.Exit(1)

    db = _db(config)
    projects = db.list_projects()

    if not projects:
        console.print("[yellow]No projects registered.[/yellow]")
        return

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold")
    table.add_column("Project Root", style="cyan")
    table.add_column("Vault Folder", style="green")
    table.add_column("Files", justify="right")
    table.add_column("Last Sync", style="dim")

    for p in projects:
        files = db.get_active_files(p.id)
        last_sync = p.last_sync_at[:10] if p.last_sync_at else "never"
        table.add_row(p.root_path, p.vault_folder, str(len(files)), last_sync)

    console.print(table)


if __name__ == "__main__":
    app()
