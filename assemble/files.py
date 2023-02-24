import typer
import csv
from assemble.models import File
from assemble.manager import fileManger
from assemble.database import get_file_table,get_database_url


app = typer.Typer(help="Save your files to a folder ")


@app.command()
def search(
        first_letter: str = typer.Argument(
            ...,
            help="String that may match file entry description."
        )
):
    """
    search and return matching file(s) .
    """
    manager = fileManger()
    file_entries = manager.find(first_letter)

    if file_entries:
        typer.echo(get_file_table(file_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any title entries matching '
                f'"{first_letter}" in your file folder.',
                fg=typer.colors.RED,
                bold=True
            )
        )


@app.command()
def list():
    """
    List all file entries tagged to a folder in a table,limit up to 10 file entries.
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
def edit(title, notes, label):
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
