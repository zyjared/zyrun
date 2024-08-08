from pathlib import Path
import toml
from ..utils.valid import has_true_value


default_config_path = Path.cwd() / 'zycli.toml'


def get_config(config_path=default_config_path, cli: str = None, ) -> dict:
    if not config_path.exists():
        return {}

    toml_string = config_path.read_text()
    config = toml.loads(toml_string)

    if cli:
        return config[cli] if cli in config else {}

    return config


def resolve_config(cli: str = None, config_path=default_config_path, **kwargs):
    """
    验证传入的配置, 如果有任何值为真则返回该配置,
    否则从指定路径和 cli 参数获取配置。

    参数:
        config: 配置
        cli: 命令名, 总配置的 key
        config_path: 配置路径

    返回:
        配置
    """
    if has_true_value(kwargs):
        return kwargs

    config = get_config(config_path, cli)
    return {**kwargs, **config}
