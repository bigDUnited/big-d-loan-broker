"""
Dummy consumer for testing.
"""
from broker.rmqConsume import Consumer
from broker.rmqPublish import publish_to_q
from broker.queue_names import *
from json import loads, dumps
import requests
import broker.translators as tr

def callback(ch, method, properties, body):
    print body

consumer = Consumer("datdb.cphbusiness.dk", "result")
consumer.on_receive = callback
consumer.consume()
