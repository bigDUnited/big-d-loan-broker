#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika


def callback(ch, method, properties, body):
    print "hello!!!" + body


class Consumer(object):

    def __init__(self, host, queue):
        self.host = host
        self.queue = queue
        self.on_receive = None

    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.host))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)
        channel.basic_consume(
            self.on_receive,
            queue=self.queue,
            no_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
        

if __name__ == '__main__':
    consumer = Consumer("127.0.0.1", "hello")
    consumer.on_receive = callback
    consumer.consume()
