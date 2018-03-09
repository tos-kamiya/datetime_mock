import datetime as _datetime
from time_mock import time_mocked

class datetime_mocked(_datetime.datetime):
    @classmethod
    def now(cls, tz=None):
        t = time_mocked()
        return cls.fromtimestamp(t, tz)

_datetime.datetime = datetime_mocked
