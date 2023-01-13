import typer

app = typer.Typer()


@app.command()
def add():
    pass


@app.command()
def edit():
    pass


@app.command()
def delete():
    pass


if __name__ == "__main__":
    app()
