from rulebase import RuleBase
from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import loads, dumps
import requests

TRANSLATORS = [
    DANSKEBANK_TRANSLATOR_QUEUE,
    NORDEA_TRANSLATOR_QUEUE,
    NYTKREDIT_TRANSLATOR_QUEUE,
    BDO_TRANSLATOR_QUEUE,
]


def callback(ch, method, properties, body):
    m = loads(body)
    res = loads(body)
    del res["banks"]
    for t in TRANSLATORS:
        if t in m["banks"]:
            publish_to_q("localhost", t, dumps(res))
    

consumer = Consumer("localhost", RECIPIENT_LIST_QUEUE)
consumer.on_receive = callback
consumer.consume()
