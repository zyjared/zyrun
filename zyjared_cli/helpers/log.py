from typing import Literal
from zyjared_color import Color


def log(cli: str, status: Literal['success', 'fail', 'warning'] | str, *args, **kwargs):
    # title
    pkgname = Color(' ZYCLI ').white().bold().bg_blue()
    cliname = Color(f' {cli} ').blue().bold().bg_white()
    _status = Color(f' {status} ').italic()
    if status == 'success':
        _status.green()
    elif status == 'fail':
        _status.red()
    else:
        _status.yellow()

    print(f'\n{pkgname}{cliname}{_status} ')

    prefix = Color(' · ').bold().yellow()

    # args
    for arg in args:
        if isinstance(arg, Color):
            print(f'  {prefix}{arg}')
        else:
            print(f'  {prefix}{Color(arg).cyan()}')

    # kwargs
    max_key = max([len(k) for k in kwargs.keys()])
    for k, v in kwargs.items():
        if isinstance(v, list):
            print(f'  {Color(k.capitalize()).cyan():<{max_key}}:')
            for item in v:
                print(f'{prefix:>{max_key + 4}}{item}')
        else:
            print(f'  {Color(k.capitalize()). cyan():<{max_key}}: {v}')
