import time_mock  # replace time.time with its mock method.
import datetime_mock  # replace datetime.datetime.now with its mock method.

time_mock.setup(1520582268, 1)

import target
target.main()
