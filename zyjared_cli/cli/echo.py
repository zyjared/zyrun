import typer
from .app import app
from ..helpers.config import get_config


@app.command()
def echo():
    """
    Echo 'hello world'.
    """
    config = get_config()
    print(config)
    typer.echo("hello world!")
