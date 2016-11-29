from rulebase import RuleBase
from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import loads, dumps
import requests
import translators as tr

def callback(ch, method, properties, body):
    print body

consumer = Consumer("datdb.cphbusiness.dk", "danskebank")
consumer.on_receive = callback
consumer.consume()
