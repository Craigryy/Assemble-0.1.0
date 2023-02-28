import typer
import csv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from assemble.models import File
from assemble.manager import fileManger
from assemble.database import get_file_table,get_database_url


app = typer.Typer(help="Save your files to a folder ")

@app.command()
def Search(
        first_letter: str = typer.Argument(
            ...,
            help="String that may match file entry description."
        )
):
    """
    search and return matching file(s) .
    """
    manager = fileManger()
    file_entries = manager.search(first_letter)

    if file_entries:
        typer.echo(get_file_table(file_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any file entries matching '
                f'"{first_letter}" in your file folder.',
                fg=typer.colors.RED,
                bold=True
            )
        )

@app.command()
def View(
        title: str = typer.Argument(
            ...,
            help="String that may match file entry description."
        )
):
    """
    view and return matching file .
    """
    manager = fileManger()
    file_entries = manager.view(title)

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
def List():
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
def Add(ctitle, cnotes, clabel):
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


def Edit(title, notes, label):
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



@app.command()
def Delete(
        title: str ,
        yes : bool = typer.Option(False,"--yes","-y",help="skip confirmation prompt and delete the folder and all of its files.")
):
    """
    Delete a folder entry using its name and all of its file(s).
    """
    engine=create_engine(get_database_url())
    Session=sessionmaker(bind=engine)
    session=Session()

    filee = session.query(File).filter(File.title==title).first()
    if not filee:
        typer.echo(typer.style(f"No file with title {title} found in the database.",fg=typer.colors.RED,bold=True))
        return

    file = session.query(File).filter(File.title==title).first()

    if not yes:
        #prompt the user to confirm the deletion.
        confirm= typer.confirm(typer.style(f"Are you sure you want to delete file title: {title} and all of its files found in the database.",fg=typer.colors.MAGENTA,bold=True))
        if not confirm:
            return


    session.delete(file)
    session.delete(filee)
    session.commit()

    typer.echo(typer.style(f"File {title} have been deleted .",fg=typer.colors.GREEN,bold=True))


