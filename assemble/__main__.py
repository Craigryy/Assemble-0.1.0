import typer
from rich.traceback import install
from assemble import files,folder

app=typer.Typer()
app.add_typer(files.app , name="File")
app.add_typer(folder.app, name='Folder')
install()


if __name__=="__main__":
    app()
