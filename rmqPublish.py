#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika


def publish_to_q(host, queue, routing, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                   'localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='',
                          routing_key=routing,
                          body=message)
    print(" [x] Sent 'Hello World!'")
    connection.close()

if __name__ == '__main__':
    publish_to_q('localhost', 'hello', 'hello', 'Hello World!')
