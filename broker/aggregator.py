"""
Handles results from banks and produces a result message
listing results from qualified banks.
"""
from rmqConsume import Consumer
from rmqPublish import publish_to_bank
from queue_names import *
from json import loads
import translators as tr

type_to_bank = {
    "danskebank":"danskebank_translator_queue",
    "nordea":"nordea_translator_queue",
}

awaiting = {}

def callback(ch, method, properties, body):
    global awaiting
    print "for aggregator:", body
    m = loads(body)
    #empty container, awaiting messages from banks
    if m["type"] == "await":
        awaiting[m["await_id"]] = {"banks":m["banks"]}
    else: #add message to container by message type
        entry = awaiting[properties.correlation_id]
        entry[m["type"]] = m
        entry["banks"].remove(type_to_bank[m["type"]])
        if len(entry["banks"]) == 0:
            del entry["banks"]
            result = {"rates":{}}
            for k, v in entry.iteritems():
                result["ssn"] = v["ssn"]
                result["rates"][v["type"]] = v["interest"]
            print result


consumer = Consumer("localhost", AGGREGATOR_QUEUE)
consumer.on_receive = callback
consumer.consume()
