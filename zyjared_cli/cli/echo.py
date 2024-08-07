import typer
from .app import app


@app.command()
def echo():
    """
    Echo 'hello world'.
    """
    typer.echo("hello world!")
