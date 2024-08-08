import typer
from typing import List, Optional, Annotated
from ..utils.fs import clean_directory
from .app import app
from ..helpers.config import resolve_config
from ..utils.timing import measure_time
from ..helpers.log import log


@app.command()
def clean(
    dirpath: Annotated[
        str,
        typer.Argument(
            show_default=False,
            help="Specify the directory to clean up.",
        )
    ] = None,
    include: Annotated[
        List[str],
        typer.Option(
            '-i',
            '--include',
            show_default=False,
            help="Regular expression to include files.",
        )
    ] = None,
    exclude: Annotated[
        Optional[List[str]],
        typer.Option(
            '-e',
            '--exclude',
            help="Regular expression to exclude files",
        )
    ] = []
):
    """
    Clean up files in a directory with specified include.
    """

    config = resolve_config(
        cli='clean',
        dirpath=dirpath,
        include=include,
        exclude=exclude
    )

    if not config['dirpath'] or not config['include']:
        log(
            'clean',
            'no files to clean up',
            dirpath=config['dirpath'],
            include=config['include'],
        )
        raise typer.Exit(1)

    measure = measure_time(
        lambda: clean_directory(
            config['dirpath'],
            config['include'],
            config['exclude']
        ),
        unit='ms'
    )

    if (len(measure['result'])):
        log(
            'clean',
            'success',
            time=measure['duration'],
            removed=measure['result'],
        )
    else:
        log(
            'clean',
            'fail',
            time=measure['duration'],
        )
