import uuid


class RPCClient:
    def __init__(self, connection, queue_name='rpc_queue'):
        self._connection = connection
        self._queue_name = queue_name

        self._response = None
        self._correlation_id = None

    def produce(self, message):
        queue = self._connection.consume_with_rpc(self._task)
        self._send_request(queue, message)
        self._connection.wait_for_response()

        print(f' [.] Got {self._response.decode("utf-8")}')

    def _send_request(self, queue, message):
        self._correlation_id = str(uuid.uuid4())
        properties = {'correlation_id': self._correlation_id, 'reply_to': queue}
        self._connection.produce_with_rpc(self._queue_name, str(message), properties)

        print(f' [x] Sent {message}')

    def _task(self, channel, method, properties, body):
        if self._correlation_id == properties.correlation_id:
            self._response = body
