from typing import List, Optional, Annotated, Pattern
from pathlib import Path
import typer
import re
from .app import app
from ..utils.fs import rmpath
from ..helpers.log import log_measure_time
from ..helpers.config import resolve_config


def matches_path(path: Path, match: list[Pattern]):
    """
    检查路径是否匹配
    """
    if len(match) == 0:
        return False

    path_str = str(path)
    for pattern in match:
        if pattern.match(path_str):
            return True

    return False


def _clean_directory(dirpath: Path, include: list[Pattern], ignore: list[Pattern] = None, removed: list[Path] = [], root: Path = None):
    """
    递归删除目录下相匹配的文件或目录

    匹配规则:
        - 匹配 include 列表中的任意一个, 不包括 ignore 列表中的任意一个
        - 如果 root 为   None, 目标字符串为文件名
        - 如果 root 不为 None, 目标字符串为相对于 root 的相对路径
    """
    for path in dirpath.iterdir():
        relpath = path.relative_to(root if root is not None else dirpath)

        if ignore is not None and matches_path(relpath, ignore):
            continue

        if matches_path(relpath, include):
            rmpath(path)
            removed.append(relpath)

        if path.is_dir():
            _clean_directory(path, include, ignore, removed, root)

    return removed


def _clean(dirpath: str | Path, include: list[str], ignore: list[str] = None):
    """
    递归删除目录下相匹配的文件或目录
    """
    if isinstance(dirpath, str):
        dirpath = Path(dirpath)

    if not dirpath.is_dir():
        raise ValueError(f'{dirpath} is not a directory')

    if not include:
        raise ValueError('include list cannot be empty')

    return _clean_directory(
        dirpath,
        [re.compile(p) for p in include],
        [re.compile(p) for p in ignore] if ignore else None,
        [],
        root=dirpath
    )


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

    log_measure_time(
        lambda: _clean(
            config['dirpath'],
            config['include'],
            config['exclude']
        ),
    )
