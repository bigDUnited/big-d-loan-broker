from rulebase import RuleBase
from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import loads, dumps
import requests

def callback(ch, method, properties, body):
    m = loads(body)
    req = "http://127.0.0.1:3001/score/{0}".format(m['score'])
    response = requests.get(req)
    banks = response.json()
    m['banks'] = banks
    publish_to_q("localhost", RECIPIENT_LIST_QUEUE, dumps(m), properties)


consumer = Consumer("localhost", BANK_ENRICHER_QUEUE)
consumer.on_receive = callback
consumer.consume()
