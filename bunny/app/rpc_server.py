from .tasks import fibonacci


class RPCServer:
    def __init__(self, connection, queue_name='rpc_queue'):
        self._connection = connection
        self._queue_name = queue_name

    def consume(self):
        print(" [x] Awaiting RPC requests")
        self._connection.queue(self._queue_name, durable=False)
        self._connection.consume_with_acknowledgement(self._queue_name, self._task)

    def _task(self, channel, method, properties, body):
        response = self._calculate_fibonnaci(body)

        self._connection.produce_with_rpc(
            properties.reply_to, str(response), {'correlation_id': properties.correlation_id}
        )
        print(f' [x] Sent {response}')

        self._connection.acknowledge(channel, method)

    def _calculate_fibonnaci(self, body):
        number = int(body)
        result = fibonacci(number)
        print(f' [.] Got {number}, fib({number}) = {result}')

        return result
