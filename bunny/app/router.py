class Router:
    def __init__(self, connection, exchange, type, routing_key):
        self._connection = connection
        self._exchange = exchange
        self._type = type
        self._routing_key = routing_key

    def produce(self, message='Hello World!'):
        self._connection.exchange(self._exchange, self._type)
        self._connection.produce_with_exchange(self._exchange, message, self._routing_key)
        print(f' [x] Sent "{message}" to -- {self._routing_key} --')
