from typing import Optional

import typer

from assemble import __app_name__,__version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
    
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--verison",
        "--v",
        help= "show the apllication's version and exit .",
        callback= _version_callback,
        is_eager=True,
    )
) -> None:
    return 

