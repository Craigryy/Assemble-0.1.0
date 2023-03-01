import typer
from assemble.manager import folderManager
from assemble.database import get_folder_table

app = typer.Typer(help='Create a folder to assemble your files')


@app.command()
def List():
    """
    List all Folder entries in a table, limits up to 40 Folder entries.
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
def Add(
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
def Delete(
        name: str = typer.Argument(
            ...,
            help="ID of a folder entry"
        ),
):
    """
    Delete a folder entry using its ID or name.
    """
    manager = folderManager()
    deleted, message = manager.delete(name)
    if deleted:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


@app.command()
def Delete_all(

):
    """
    Delete all folder entries.
    """
    manager = folderManager()
    deleted, message = manager.delete_all()
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
