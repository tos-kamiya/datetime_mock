import time as _time

_time_func = _time.time
_stat = []


def setup(start_time, time_tick):
    _stat[:] = [start_time, time_tick]


def time_mocked():
    if not _stat:
        return _time_func()

    t = _stat[0]
    _stat[0] += _stat[1]
    return t


_time.time = time_mocked
