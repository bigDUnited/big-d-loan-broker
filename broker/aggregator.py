"""
Handles results from banks and produces a result message
listing results from qualified banks.
"""
from rmqConsume import Consumer
from rmqPublish import publish_to_bank
from queue_names import *
from json import loads
import translators as tr


awaiting = {}

def callback(ch, method, properties, body):
    print properties
    print body

    

consumer = Consumer("localhost", AGGREGATOR_QUEUE)
consumer.on_receive = callback
consumer.consume()

AGGREGATOR_QUEUE
