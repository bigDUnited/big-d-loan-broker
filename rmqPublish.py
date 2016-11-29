#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika


def publish_to_q(host, queue, message, properties):
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
