import time_mock  # replace time.time with its mock method.
import datetime_mock  # replace datetime.datetime.now with its mock method.

time_mock.setup(1520578800, 1)  # make time.time() return 16:00:00, 16:00:01, ...

import target
target.main()
