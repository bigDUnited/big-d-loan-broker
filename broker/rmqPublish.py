#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
RabbitMQ publish utilities.
"""
import pika


def publish_to_bank(host, exchange, message, properties):
    """
    Publish to a third-party bank. Uses an exchange name.
    properties should be a pika properties object.
    """
    exchange_name = ""
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                   host))
    channel = connection.channel()

    channel.exchange_declare(
        exchange=exchange,
        exchange_type='fanout',
    )

    channel.basic_publish(exchange=exchange,
                          routing_key="",
                          body=message,
                          properties=properties)
    connection.close()



def publish_to_q(host, queue, message, properties):
    """
    Publishing function for the internal queues.
    A host address has to be provided as well as queue name to push to.
    properties should be a pika properties object.
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                   host))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=message,
                          properties=properties)
    connection.close()

if __name__ == '__main__':
    publish_to_q('localhost', 'hello', 'Hello World!')
