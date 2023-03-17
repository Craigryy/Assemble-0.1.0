import typer


from assemble.manager import folder_manager
from assemble.utilis import get_folder_table
from assemble.models import Folder


app = typer.Typer(help='Create a folder to assemble your files')


@app.command()
def list():
    """
    list all Folder entries in a table, limits up to 40 Folder entries.
    """

    manager = folder_manager()
    folder_entries = manager.list()

    if folder_entries:
        typer.echo(get_folder_table(folder_entries))
    else:
        typer.echo(
            typer.style(
                ("You do not have any entries in your folder."),
                fg=typer.colors.MAGENTA,
                bold=True
            )
        )


@app.command()
def add(
        name: str = typer.Argument(
            ...,
            help="Name of the folder entry."
        ), notes: str = typer.Argument(
            ...,
            help="Note of a folder entry."
        )
):
    """
    add a folder entry.
    """
    manager = folder_manager()
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
        name: str = typer.Argument(
            ...,
            help="ID of a folder entry"
        ), yes: bool = typer.Option(False, "--yes", "-y",
                                    help="skip confirmation prompt and delete the folder and all of its files.")

):
    """
    delete a folder entry using its name.
    """
    manager = folder_manager()

    folder = manager.session.query(Folder).filter(Folder.name == name).first()
    if not folder:
        typer.echo(typer.style(
            f"No folder with the name: {name} found in the database.", fg=typer.colors.RED, bold=True))
        return

    folder = manager.session.query(Folder).filter(Folder.name == name).first()

    if not yes:
        # prompt the user to confirm the deletion.
        confirm = typer.confirm(typer.style(
            f"Are you sure you want to delete folder name: {name} and all of its files found in the database.", fg=typer.colors.MAGENTA, bold=True))
        if not confirm:
            return
        manager.session.delete(folder)
    manager.session.delete(folder)
    manager.session.commit()

    typer.echo(typer.style(
        f"Folder: {name} have been deleted .", fg=typer.colors.GREEN, bold=True))


@app.command()
def delete_all(
):
    """
    delete all folder entries.
    """
    confirmation = typer.confirm("Are you sure you want to delete all items")
    manager = folder_manager()
    deleted, message = manager.delete_all()
    if deleted and confirmation:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


if __name__ == "__main__":
    app()
