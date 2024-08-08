from typing import Literal
from zyjared_color import Color
from ..utils.timing import measure_time

predot = Color(' · ').bold().cyan()


def _log_list(ls: list, preblank: int = 2, prefix=predot):
    if len(ls) == 0:
        print(f'{prefix.yellow():>{preblank}}{Color("empty".upper()).yellow().italic()}')
    for item in ls:
        print(f'{prefix:>{preblank}}{item}')

def _log_dict(d: dict, preblank: int = 2, prefix=predot):
    length = max([len(k) for k in d.keys()])
    for k, v in d.items():
        print(f'{" " * preblank}{Color(str(k).capitalize()).cyan():<{length}}: ', end='')
        if isinstance(v, list):
            print()
            _log_list(v, preblank + length + 2, prefix)
        elif isinstance(v, dict):
            _log(v, preblank + length + 2, prefix)
        else:
            print(v)


def _log(text: str | list | dict, preblank: int = 2, prefix=predot):
    if isinstance(text, list):
        _log_list(text, preblank, prefix)
    elif isinstance(text, dict):
        _log_dict(text, preblank, prefix)
    else:
        print(text)


def _log_title(cli: str, status: Literal['success', 'fail', 'warning'] | str):
    pkgname = Color(' ZYCLI ').white().bold().bg_blue()
    cliname = Color(f' {cli} ').blue().bold().bg_white()
    _status = Color(f' {status.upper()} ').bold()
    if status == 'SUCCESS':
        _status.green()
    elif status == 'FAIL':
        _status.red()
    else:
        _status.yellow()

    print(f'\n{pkgname}{cliname}{_status} ')


def alog(
    cli: str,
    status: Literal['success', 'fail', 'warning'] | str,
    *args,
    **kwargs
):
    _log_title(cli, status)

    if args:
        _log_list(args, preblank=2, prefix=predot)
    if kwargs:
        _log(kwargs, preblank=2, prefix=predot)


def log(
    status: Literal['success', 'fail', 'warning'] | str,
    cli: str = "tool",
    log_list: list = [],
    log_dict: dict = {},
):
    _log_title(cli, status)

    if log_list:
        _log_list(log_list, preblank=4, prefix=predot)
    if log_dict:
        _log(log_dict, preblank=2, prefix=predot)


def log_measure_time(func, precision=2, cli="tool", result_title="Result"):
    result = measure_time(func, precision)

    log(
        status='success' if result['sucess'] else 'fail',
        cli=cli,
        log_dict={
            'time': result['time'],
            'result': result['result'],
        }
    )
