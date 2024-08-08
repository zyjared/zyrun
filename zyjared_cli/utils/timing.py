from typing import Literal
from zyjared_color import Color
import time


UNITS = ['s', 'ms', 'us', 'ns']


def endow_unit(t: int, init_unit: Literal['s', 'ms', 'us', 'ns'] = 's'):
    i = UNITS.index(init_unit)

    for j in range(i, len(UNITS)):
        if t >= 1:
            break
        else:
            t = t * (1000 ** j)
            i = j

    return {
        "time": t,
        "unit": UNITS[i],
    }


def measure_time(
        func,
        precision=2
):
    start = time.time()

    try:
        result = func()
        sucess = True
    except Exception as e:
        result = str(e)
        sucess = False

    end = time.time()

    endowed = endow_unit(end - start)

    return {
        "sucess": sucess,
        "time": str(round(endowed['time'], precision)) + ' ' + Color(endowed['unit']).cyan().italic(),
        "result": result,
    }
