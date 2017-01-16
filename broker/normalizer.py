"""
Handles results from banks passing a message in 
internal message format to aggregation service.
"""
from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import dumps
import translators as tr


def callback(ch, method, properties, body):
    print "raw bank properties:", properties
    print "raw bank body:", body
    mtype = properties.correlation_id[8:]
    mid = properties.correlation_id[:8]
    properties.correlation_id = mid
    message = tr.loads(body, mtype)
    message["type"] = mtype
    publish_to_q("localhost",
                 AGGREGATOR_QUEUE,
                 dumps(message),
                 properties)
    

consumer = Consumer("datdb.cphbusiness.dk", NORMALIZER_QUEUE) 
consumer.on_receive = callback
consumer.consume()


