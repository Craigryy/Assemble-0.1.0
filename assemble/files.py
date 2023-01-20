import typer
from assemble.manager import fileManger
from assemble.database import get_file_table


app = typer.Typer(help="A Command line tool to assemble your files ")

@app.command()
def list_files():
        """
           List all files entries in a table, limits up to 40 folder entries.
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
def add(ctitle,cnotes,clabel):
    """
    Add a file entry to a folder.
    """

    manager = fileManger()
    created, message = manager.addFile(ctitle,cnotes,clabel)
    if created:
            typer.echo(
                typer.style(message, fg=typer.colors.GREEN, bold=True)
            )
    else:
            typer.echo(
                typer.style(message, fg=typer.colors.RED, bold=True)
            )




@app.command()
def edit_file(title,notes,label):
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
