"""
Enriches a message with available banks by calling
a rule base service.
"""
import requests
import pika
from rulebase import RuleBase
from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import loads, dumps


def callback(ch, method, properties, body):
    m = loads(body)
    req = "http://127.0.0.1:3001/score/{0}".format(m['score'])
    print "requesting bank credit score service for score:", m['score']
    response = requests.get(req)
    banks = response.json()
    m['banks'] = banks
    #prepare aggregator for new message
    await_message = {
        "banks": banks,
        "await_id": properties.correlation_id,
        "type": "await",
    }

    publish_to_q(
        'localhost',
        AGGREGATOR_QUEUE,
        dumps(await_message),
        pika.BasicProperties(
            correlation_id="{}await".format(properties.correlation_id)
    ))

    #send to list of banks through recepiant list
    print "received banks:", banks
    publish_to_q("localhost", RECIPIENT_LIST_QUEUE, dumps(m), properties)


consumer = Consumer("localhost", BANK_ENRICHER_QUEUE)
consumer.on_receive = callback
consumer.consume()
