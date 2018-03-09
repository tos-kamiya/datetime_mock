# datetime_mock

A proof of concept of mocking datetime and time modules.

`time.time` and `datetime.datetime.now` methods are replaced with their mock methods and return the times that are specified with `time_mock.setup`.

## Try it

```
$ python3 run_target_with_mocked_datetime.py
2018-03-09 16:00:00
2018-03-09 16:00:01
2018-03-09 16:00:02
2018-03-09 16:00:03
2018-03-09 16:00:04
2018-03-09 16:00:05
2018-03-09 16:00:06
2018-03-09 16:00:07
2018-03-09 16:00:08
2018-03-09 16:00:09
```
