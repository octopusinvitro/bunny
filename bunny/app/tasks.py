import time


def fake_slow_task(body):
    time.sleep(body.count(b'.'))
