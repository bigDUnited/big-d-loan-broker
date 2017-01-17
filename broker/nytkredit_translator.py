from rmqConsume import Consumer
from rmqPublish import publish_to_q
from queue_names import *
from json import loads, dumps
import translators as tr
import random

def callback(ch, method, properties, body):
    properties.correlation_id += "nytkredit"
    properties.reply_to = NORMALIZER_QUEUE
    m = loads(body)
    
    print "Nytkredit: ", m
    
    #pretend to get a response, send to normalizer
    m = loads(tr.dumps(m, "nytkredit"))
    del m['loanAmount']
    del m['loanDuration']
    rating = random.randint(2, 50)
    m["interestRate"] = rating
    print m
    publish_to_q("datdb.cphbusiness.dk",
                 NORMALIZER_QUEUE,
                 dumps(m),
                 properties)
    

consumer = Consumer("localhost", NYTKREDIT_TRANSLATOR_QUEUE)
consumer.on_receive = callback
consumer.consume()
