import typer
from assemble.manager import folderManager
from assemble.database import get_folder_table

app = typer.Typer(help='A command line tool to keep your folders')


@app.command()
def listFolders():
    """
    List all Folder entries in a table, limits up to 10 Folder entries.
    """
    manager = folderManager()
    folder_entries = manager.list()

    if folder_entries:
        typer.echo(get_folder_table(folder_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any entries in your folder.',
                fg=typer.colors.MAGENTA,
                bold=True
            )
        )


@app.command()
def add(
        name: str = typer.Argument(
            ...,
            help="Name of the folder entry."
        )
        , notes: str = typer.Argument(
            ...,
            help="Note of a folder entry."
        )
):
    """
    Add a folder entry.
    """
    manager = folderManager()
    created, message = manager.addFolder(name, notes)

    if created:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


@app.command()
def delete(
        id: int = typer.Argument(
            ...,
            help="ID of a folder entry"
        )
):
    """
    Delete a folder entry using its ID.
    """
    manager = folderManager()
    deleted, message = manager.delete(id)
    if deleted:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


if __name__ == "__main__":
    app()
