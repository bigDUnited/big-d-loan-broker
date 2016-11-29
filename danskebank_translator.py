from rulebase import RuleBase
from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import loads, dumps
import requests
import translators as tr
import pika

def callback(ch, method, properties, body):
    m = loads(body)
    result = tr.dumps(m, "danskebank")
    print dumps(m)
    publish_to_q("datdb.cphbusiness.dk",
                 "",
                 dumps(m),
    pika.BasicProperties(
        correlation_id="12399942",
        reply_to="danskebank",
    ))
    

consumer = Consumer("localhost", DANSKEBANK_TRANSLATOR_QUEUE)
consumer.on_receive = callback
consumer.consume()
