import pika


class Connection:
    def __init__(self, hostname='localhost'):
        connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
        self._channel = connection.channel()

    def queue(self, queue):
        self._channel.queue_declare(queue=queue, durable=True)

    def produce_with_message_persistance(self, routing_key, message):
        self._channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(
               delivery_mode=pika.DeliveryMode.Persistent
            )
        )

    def consume_with_acknowledgement(self, queue, callback_with_acknowledgement):
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(
            queue=queue, on_message_callback=callback_with_acknowledgement
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
