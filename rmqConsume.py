#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
from multiprocessing import Process, Manager
from time import sleep


_manager = None
_data = None

def get_manager(): # Note that you don't have to use a singleton here
    global _manager, _data
    if not _manager:
        _manager = Manager()
        _data = _manager.list()
    return _manager

def callback(ch, method, properties, body):
    global _data
    get_manager()
    _data.append(body)

def consume_from_q(host, queue, callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(
        callback,
        queue=queue,
        no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    get_manager()
    p = Process(
        target=consume_from_q,
        args=("127.0.0.1","hello",callback))
    p.start()
    while True:
        print _data
        sleep(1)
    p.join()
