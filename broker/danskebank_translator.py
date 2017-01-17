"""
Translator node for Danske Bank(bankJSON).
"""
from rmqConsume import Consumer
from rmqPublish import publish_to_bank
from queue_names import *
from json import loads
import translators as tr
import pika

def callback(ch, method, properties, body):
    m = loads(body)
    result = tr.dumps(m, "danskebank")
    properties.correlation_id += "danskebank"
    properties.reply_to = NORMALIZER_QUEUE
    print "danske bank translator: ", result
    publish_to_bank(
        "datdb.cphbusiness.dk",
        'cphbusiness.bankJSON',
        result,
        properties)


consumer = Consumer("localhost", DANSKEBANK_TRANSLATOR_QUEUE)
consumer.on_receive = callback
consumer.consume()
