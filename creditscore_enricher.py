from rmqConsume import Consumer
from rmqPublish import publish_to_q
from creditapi import getCreditScore
from queue_names import *
from json import loads, dumps

def callback(ch, method, properties, body):
    m = loads(body)
    score = getCreditScore(m['ssn'])
    m['score'] = str(score)
    publish_to_q("localhost", BANK_ENRICHER_QUEUE, dumps(m))


consumer = Consumer("localhost", CREDIT_ENRICHER_QUEUE)
consumer.on_receive = callback
consumer.consume()

