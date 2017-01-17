"""
Translator node for Nordea(bankXML).
"""
from rmqConsume import Consumer
from rmqPublish import publish_to_bank
from queue_names import *
from json import loads
import translators as tr


def callback(ch, method, properties, body):
    m = loads(body)
    result = tr.dumps(m, "nordea")
    properties.correlation_id += "nordea"
    properties.reply_to = NORMALIZER_QUEUE
    print "nordea bank translator: ", result
    publish_to_bank(
        "datdb.cphbusiness.dk",
        'cphbusiness.bankXML',
        result,
        properties)

    

consumer = Consumer("localhost", NORDEA_TRANSLATOR_QUEUE)
consumer.on_receive = callback
consumer.consume()
