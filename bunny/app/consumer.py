from .tasks import fake_slow_task


class Consumer:
    def __init__(self, connection, queue_name='hello'):
        self._connection = connection
        self._queue_name = queue_name

    def consume(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self._connection.queue(self._queue_name)
        self._connection.consume_with_acknowledgement(self._queue_name, self._faked_slow_task)

    def _faked_slow_task(self, channel, method, properties, body):
        print(f' [x] Received {body.decode("utf-8")}')
        fake_slow_task(body)
        print(' [x] Done')

        self._connection.acknowledge(channel, method)
