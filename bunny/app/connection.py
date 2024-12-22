import pika


class ExchangeTypes:
    DIRECT = 'direct'
    FANOUT = 'fanout'
    HEADER = 'headers'
    TOPIC = 'topic'


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

    def produce_with_exchange(self, exchange, message):
        self._channel.basic_publish(
            exchange=exchange,
            routing_key='',
            body=message,
        )

    def consume_with_acknowledgement(self, queue, callback_with_acknowledgement):
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(
            queue=queue, on_message_callback=callback_with_acknowledgement
        )
        self._channel.start_consuming()

    def consume_with_exchange(self, exchange, callback):
        result = self.queue(queue='', durable=False, exclusive=True)
        queue = result.method.queue

        self._channel.queue_bind(exchange=exchange, queue=queue)
        self._channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True
        )
        self._channel.start_consuming()

    def acknowledge(self, channel, method):
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def delete(self, queue):
        self._channel.queue_delete(queue=queue)

    def close(self):
        connection = self._channel.connection

        if connection.is_open:
            connection.close()
