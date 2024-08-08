from typing import Dict, Any


def has_true_value(dic: Dict[str, Any]):
    return any(dic.values())
