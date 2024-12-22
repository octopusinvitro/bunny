class Broadcaster:
    def __init__(self, connection, exchange, type):
        self._connection = connection
        self._exchange = exchange
        self._type = type

    def produce(self, message='Hello World!'):
        self._connection.exchange(self._exchange, self._type)
        self._connection.produce_with_exchange(self._exchange, message)
        print(f' [x] Sent {message}')
