from rmqConsume import Consumer
from rmqPublish import publish_to_bank
from queue_names import *
from json import loads
import translators as tr


def callback(ch, method, properties, body):
    print "nordea bank translator : ", body
    publish_to_bank(
        "datdb.cphbusiness.dk",
        'cphbusiness.bankXML',
        body,
        properties)

    

consumer = Consumer("localhost", NORDEA_TRANSLATOR_QUEUE)
consumer.on_receive = callback
consumer.consume()
