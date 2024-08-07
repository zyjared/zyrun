import typer
from typing import List, Optional, Annotated
from pathlib import Path
from time import time
from .app import app
from zyjared_color import Color
from zyjared_fs import clean_directory


@app.command()
def clean(
    dirpath: Annotated[
        str,
        typer.Argument(
            default=...,
            show_default=False,
            help="Specify the directory to clean up.",
        )
    ],
    include: Annotated[
        List[str],
        typer.Option(
            '-i',
            '--include',
            show_default=False,
            help="Regular expression to include files.",
        )
    ],
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
    # -> time
    start_time = time()

    # clean
    dirpath = Path(dirpath)
    removed = clean_directory(dirpath, include, exclude)

    # title
    pkg = Color(" zyjared-cli ").white().bg_blue().bold()
    title = Color(" clean ").white().bg_magenta()
    sep = " : "

    state = Color(" success ").green() if len(
        removed) != 0 else Color(" no files removed ").magenta()

    # -> time
    end_time = time()

    # info
    prefix_dir = Color("Dir").cyan()
    prefix_time = Color("Time").cyan()
    duration = f'{str(round((end_time - start_time) * 1000, 2))
                  } {Color("ms").green()}'

    # print

    print(f'\n{pkg}{title}{state}')
    print(f'    {prefix_dir:<16}{sep}{dirpath}')
    print(f'    {prefix_time:<16}{sep}{duration}')

    # removed files
    if len(removed) != 0:
        prefix = Color("Removed").yellow()
        print(f'\n    {prefix:<16}')
        for path in removed:
            print(f'{sep:>14}{path}')
