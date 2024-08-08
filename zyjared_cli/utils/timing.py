from typing import Literal
from zyjared_color import Color
import time


UNITS = ['s', 'ms', 'us', 'ns']


def measure_time(
        func,
        unit: Literal['s', 'ms', 'us', 'ns'] | Color = 'ms',
        precision=3
):
    start = time.time()
    result = func()
    end = time.time()

    duration = round(
        (end - start) * (1 * (1000 ** UNITS.index(unit))), precision
    )

    unit = unit if isinstance(unit, Color) else Color(unit).cyan()

    return {
        "time": duration,
        "duration": str(duration) + ' ' + unit,
        "result": result
    }
