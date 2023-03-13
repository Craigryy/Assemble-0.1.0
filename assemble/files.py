import typer
import csv
from assemble.models import File, Folder
from assemble.manager import fileManger, folderManager
from assemble.database import get_file_table
from typing import Optional


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
            typer.style((f'You do not have any file entries.'),
                fg=typer.colors.MAGENTA,
                bold=True
            )
        )


@app.command()
def Add(ctitle, cnotes, clabel: Optional[str] = typer.Argument(None)):
    """
    Add a file entry to a folder.
    """
    manager = fileManger() or folderManager()

    if clabel is None:
        clabel = "default"
        # query database for a default
        default_folder = manager.session.query(Folder).filter(
            Folder.name == "default_folder").first()
        if default_folder:
            # #create a file
            file = File(title=ctitle, notes=cnotes,
                        label=clabel, author=default_folder)
            manager.save(file)
            typer.echo(typer.style(
                f"Default folder created and file added to folder name: {default_folder.name}. ", fg=typer.colors.MAGENTA, bold=True))
        else:
            default_f = Folder(name="default", notes="have a nice day")
            manager.session.add(default_f)
            child = File(title=ctitle, notes=cnotes,
                         label=clabel, author=default_f)
            manager.save(child)
            typer.echo(typer.style(f"Default folder created and file  to folder name: {default_f.name}. with label : {child.label} ",
                                   fg=typer.colors.MAGENTA, bold=True))

    elif clabel is not None:
        # query the database folder that matches the file
        file_folder = manager.session.query(
            Folder).filter(Folder.name == clabel).first()
        # create a new file
        NewFile = File(title=ctitle, notes=cnotes,
                       label=clabel, author=file_folder)
        manager.save(NewFile)
        typer.echo(typer.style(
            f"file added to an existing folder name:{NewFile.label}", fg=typer.colors.MAGENTA, bold=True))

    else:
        # create a new folder.
        new_folder = Folder(name=clabel, notes="have a nice day")
        manager.session.add(new_folder)
        # craete a new file
        new_file = File(title=ctitle, notes=cnotes,
                        clabel=clabel, author=new_folder)
        manager.save(new_file)
        typer.echo(
            typer.style(f"a new file created and added to an existing folder name:{new_folder.name}", fg=typer.colors.MAGENTA, bold=True))
        return


@app.command()
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
        title: str,
        yes: bool = typer.Option(False, "--yes", "-y",
                                 help="skip confirmation prompt and delete the folder and all of its files.")
):
    """
    Delete a folder entry using its name and all of its file(s).
    """

    manager = fileManger()

    filee = manager.session.query(File).filter(File.title == title).first()
    if not filee:
        typer.echo(typer.style(
            f"No file with title {title} found in the database.", fg=typer.colors.RED, bold=True))
        return

    file = manager.session.query(File).filter(File.title == title).first()

    if not yes:
        # prompt the user to confirm the deletion.
        confirm = typer.confirm(typer.style(
            f"Are you sure you want to delete file title: {title}.", fg=typer.colors.MAGENTA, bold=True))
        if not confirm:
            return

    manager.session.delete(filee)
    manager.session.delete(file)
    manager.session.commit()

    typer.echo(typer.style(
        f"File {title} have been deleted .", fg=typer.colors.GREEN, bold=True))


@app.command()
def insert(csv_filename: str):
    """
    insert csv into model database
    """
    manager = fileManger()

    # Open the CSV file and insert its contents into the table
    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            data = File(title=row[0],
                        notes=row[1],
                        label=row[2]
                        )
            manager.save(data)

    typer.echo(typer.style((f"csv file added to file table ."),
               fg=typer.colors.GREEN, bold=True))


if __name__ == "_main_":
    app()
