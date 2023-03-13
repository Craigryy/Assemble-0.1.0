import typer
from rich.traceback import install
from asseme import files, folder, docs

app = typer.Typer()
app.add_typer(folder.app, name="Folder")
app.add_typer(files.app, name="File")
app.add_typer(docs.app, name="Docs")
install()

if __name__ == "__main__":
    app()
