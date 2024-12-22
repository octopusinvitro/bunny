class Broadcastee:
    def __init__(self, connection, exchange, type):
        self._connection = connection
        self._exchange = exchange
        self._type = type

    def consume(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self._connection.exchange(self._exchange, self._type)
        self._connection.consume_with_exchange(self._exchange, self._fake_task)

    def _fake_task(self, channel, method, properties, body):
        print(f' [x] Received {body.decode("utf-8")}')
