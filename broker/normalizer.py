"""
Handles results from banks passing a message in 
internal message format to aggregation service.
"""
from rmqConsume import Consumer
from rmqPublish import publish_to_bank
from queue_names import *
from json import loads
import translators as tr


def callback(ch, method, properties, body):
    print properties
    print body
    mtype = properties.correlation_id[8:]
    message = tr.loads(body, mtype)

    

consumer = Consumer("datdb.cphbusiness.dk", NORMALIZER_QUEUE)
consumer.on_receive = callback
consumer.consume()


