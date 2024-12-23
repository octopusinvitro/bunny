import pika


class Connection:
    def __init__(self, hostname='localhost'):
        connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self._channel = connection.channel()

    def queue(self, queue, durable=True, exclusive=False):
        return self._channel.queue_declare(queue=queue, durable=durable, exclusive=exclusive)

    def exchange(self, exchange, type):
        self._channel.exchange_declare(exchange=exchange, exchange_type=type)

    def produce_with_message_persistance(self, routing_key, message):
        self._channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(
               delivery_mode=pika.DeliveryMode.Persistent
            )
        )

    def produce_with_rpc(self, routing_key, message, properties):
        self._channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(**properties)
        )

    def produce_with_exchange(self, exchange, message, routing_key=''):
        self._channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=message,
        )

    def consume_with_acknowledgement(self, queue, callback_with_acknowledgement):
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(
            queue=queue, on_message_callback=callback_with_acknowledgement
        )
        self._channel.start_consuming()

    def consume_with_exchange(self, exchange, callback, binding_keys=['']):
        result = self.queue(queue='', durable=False, exclusive=True)
        queue = result.method.queue

        for binding_key in binding_keys:
            self._channel.queue_bind(
                exchange=exchange, queue=queue, routing_key=binding_key
            )

        self._channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True
        )
        self._channel.start_consuming()

    def consume_with_rpc(self, callback):
        result = self.queue(queue='', durable=False, exclusive=True)
        queue = result.method.queue

        self._channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True
        )

        return queue

    def wait_for_response(self):
        self._channel.connection.process_data_events(time_limit=None)

    def acknowledge(self, channel, method):
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def delete(self, queue):
        self._channel.queue_delete(queue=queue)

    def close(self):
        connection = self._channel.connection

        if connection.is_open:
            connection.close()
