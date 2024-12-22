import time


def fake_slow_task(body):
    time.sleep(body.count(b'.'))


def fibonacci(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)
