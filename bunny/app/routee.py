class Routee:
    def __init__(self, connection, exchange, type, routing_keys):
        self._connection = connection
        self._exchange = exchange
        self._type = type
        self._routing_keys = routing_keys

    def consume(self):
        print(f' [*] Waiting for messages from {self._routing_keys}. To exit press CTRL+C')
        self._connection.exchange(self._exchange, self._type)
        self._connection.consume_with_exchange(self._exchange, self._fake_task, self._routing_keys)

    def _fake_task(self, channel, method, properties, body):
        print(f' [x] Received {body.decode("utf-8")}')
