from pathlib import Path


def rmpath(filepath: Path):
    """
    删除文件或目录
    """
    try:
        if filepath.is_dir():
            for child in filepath.iterdir():
                rmpath(child)
            filepath.rmdir()
        else:
            filepath.unlink()
    except PermissionError:
        print(f'[rm_path] Permission denied: {filepath}')
    except FileNotFoundError:
        print(f'[rm_path] File not found: {filepath}')
    except Exception as e:
        print(f'[rm_path] Error {filepath}: {e}')
