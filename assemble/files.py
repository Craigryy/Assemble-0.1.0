import typer
from assemble.manager import fileManger
from assemble.database import get_file_table

app = typer.Typer(help="A Command line tool to assemble your files ")


@app.command()
def find(
        title: str = typer.Argument(
            ...,
            help="String that may match file entry description."
        )
):
    """
    List all file entries that match the argument.
    """
    manager = fileManger()
    file_entries = manager.find(title)

    if file_entries:
        typer.echo(get_file_table(file_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any title entries matching '
                f'"{title}" in your file folder.',
                fg=typer.colors.RED,
                bold=True
            )
        )


@app.command()
def list_files():
    """
    List all file entries tagged to a folder in a table,limit up to 40 file entries.
    """
    manager = fileManger()
    file_entries = manager.list()

    if file_entries:
        typer.echo(get_file_table(file_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any file entries.',
                fg=typer.colors.MAGENTA,
                bold=True
            )
        )


@app.command()
def add(ctitle, cnotes, clabel):
    """
    Add a file entry to a folder.
    """
    manager = fileManger()
    created, message = manager.addFile(ctitle, cnotes, clabel)
    if created:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


@app.command()
def edit_file(title, notes, label):
    """
    Update a file entry using its label.
    """
    manager = fileManger()
    updated, message = manager.update(
        title=title,
        notes=notes,
        label=label
    )
    if updated:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


if __name__ == "__main__":
    app()
