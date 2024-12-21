class Producer:
    def __init__(self, connection, queue_name='hello'):
        self._connection = connection
        self._queue_name = queue_name

    def produce(self, message='Hello World!'):
        self._connection.queue(self._queue_name)
        self._connection.produce_with_message_persistance(self._queue_name, message)
        print(f' [x] Sent {message}')
