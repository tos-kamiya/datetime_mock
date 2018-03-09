# datetime_mock

A proof of concept of mocking datetime and time modules.

`time.time` and `datetime.datetime.now` methods are replaced with their mock methods and return the times that are specified with `time_mock.setup`.

## Try it

```
$ python3 run_target_with_hooking.py
2018-03-09 16:57:48
2018-03-09 16:57:49
```
