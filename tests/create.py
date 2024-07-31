from pathlib import Path
# from ..zyjared_cli.clean import clean as zy_clean

def create_test():
    files = [
        '01.py',
        '02.py',
        '03.py',
    ]

    test = Path.cwd() / 'test'
    if not test.exists():
        test.mkdir()

    for file in files:
        test.joinpath(file).touch()
        print(f'created {file}')


if __name__ == '__main__':
    create_test()
