import datetime_mock  # replace datetime.datetime.now with its mock method.
datetime_mock.setup(1520578800, 1)  # make now() return 16:00:00, 16:00:01, ...

import target
target.main()
