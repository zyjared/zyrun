import typer
from .clean import clean as zy_clean
from typing import List, Optional, Annotated

app = typer.Typer()


@app.callback()
def callback():
    """
    zyjared's tool
    """


@app.command()
def clean(
    dirpath: Annotated[
        str,
        typer.Option('-d', '--dirpath', help="Directory to clean")
    ],
    include: Annotated[
        List[str],
        typer.Option('-i', '--include', help="Include files")
    ],
    exclude: Annotated[
        Optional[List[str]],
        typer.Option('-e', '--exclude', help="Exclude files")
    ] = []
):
    """
    Clean up files in a directory with specified include.
    """
    zy_clean(dirpath, include, exclude)


@app.command()
def echo():
    """
    Echo 'hello world'.
    """
    typer.echo("hello world")

