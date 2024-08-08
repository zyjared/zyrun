from zyjared_cli.helpers.config import resolve_config
from tests.test_clean import create_files

if __name__ == '__main__':
    create_files()

    dirpath = 'test'
    include = None
    exclude = None
    config = resolve_config(
        dirpath=dirpath, include=include, exclude=exclude,
        cli='clean',
        default_config={
            'dirpath': None,
            'include': None,
            'exclude': []
        })

    print(config)
