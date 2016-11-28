from rulebase import RuleBase
from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import loads, dumps
import requests

def callback(ch, method, properties, body):
    m = loads(body)
    print body

consumer = Consumer("localhost", RECIPIENT_LIST_QUEUE)
consumer.on_receive = callback
consumer.consume()
