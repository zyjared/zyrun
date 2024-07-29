from typing import List, Optional
from zyjared_fs import clean_directory
from zyjared_color import Color
from pathlib import Path
from time import time

def clean(
    dirpath: str,
    include: List[str],
    exclude: Optional[List[str]] = []
):
    # -> time
    start_time = time()

    # clean
    dirpath = Path(dirpath)
    removed = clean_directory(dirpath, include, exclude)

    # title
    pkg = Color(" zyjared-cli ").white().bg_blue().bold()
    t = Color(" clean ").white().bg_magenta()
    r = Color(" → ").green().to_str()

    state = Color(" success ").green() if len(
        removed) != 0 else Color(" no files removed ").magenta()

    # -> time
    end_time = time()

    # info
    prefix_dir = Color("Dir").cyan().to_str()
    prefix_time = Color("Time").cyan().to_str()
    duration = f'{str(round((end_time - start_time) * 1000, 2))
                  } {Color("ms").green()}'

    # print

    print(f'\n{pkg}{t}{state}')
    print(f'    {prefix_dir:<16}{r}{dirpath}')
    print(f'    {prefix_time:<16}{r}{duration}')

    # removed files
    if len(removed) != 0:
        prefix = Color("Removed").yellow().to_str()
        print(f'\n    {prefix:<16}')
        for path in removed:
            print(f'    {r:>19}{path}')
