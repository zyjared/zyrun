from pathlib import Path
from typer.testing import CliRunner
from zyjared_cli.main import app

runner = CliRunner()


def create_files(files=[
    '01.py',
    '02.py'
]):

    test = Path.cwd() / 'test'
    if not test.exists():
        test.mkdir()

    for file in files:
        test.joinpath(file).touch()
        print(f'created {file}')


def test_app():

    create_files()

    result = runner.invoke(app, ['clean', 'test', '--include', r'\d+\.py'])
    assert result.exit_code == 0

    assert "1.py" in result.stdout
    assert "2.py" in result.stdout
