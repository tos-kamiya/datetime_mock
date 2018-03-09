import importlib
import sys
import os.path as os_path

import time_mock
import datetime_mock

time_mock.setup(1520582268, 1)

import target
target.main()
