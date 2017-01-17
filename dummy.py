"""
Dummy publisher.
"""
from broker.rmqPublish import publish_to_q
from broker.queue_names import NORDEA_TRANSLATOR_QUEUE
from broker.queue_names import DANSKEBANK_TRANSLATOR_QUEUE
from broker.queue_names import NYTKREDIT_TRANSLATOR_QUEUE
from broker.queue_names import NORMALIZER_QUEUE
from broker.queue_names import AGGREGATOR_QUEUE
import json
import pika

# message = {
#     "ssn": "123456-3212", #social security number
#     "amount": "300", #crowns
#     "duration": "60", #days
#     "timeout" : "900" #seconds
# }

message = {
    "score": "303",
    "amount": "300",
    "ssn": "123456-3212",
    "timeout": "900",
    "duration": "60"
}

await_message = {
    # "banks": [u'danskebank_translator_queue',
    #           u'nordea_translator_queue'],
    "banks": [u'nytkredit_translator_queue', ],
    "await_id": "12399942",
    "type": "await",
}

publish_to_q(
    'localhost',
    AGGREGATOR_QUEUE,
    json.dumps(await_message),
    pika.BasicProperties(
        correlation_id="12399941",
    ))

# publish_to_q(
#     'localhost',
#     NORDEA_TRANSLATOR_QUEUE,
#     json.dumps(message),
#     pika.BasicProperties(
#         correlation_id="12399942",
#         reply_to=NORMALIZER_QUEUE,
#     ))

# publish_to_q(
#     'localhost',
#     DANSKEBANK_TRANSLATOR_QUEUE,
#     json.dumps(message),
#     pika.BasicProperties(
#         correlation_id="12399942",
#         reply_to=NORMALIZER_QUEUE,
#     ))

publish_to_q(
    'localhost',
    NYTKREDIT_TRANSLATOR_QUEUE,
    json.dumps(message),
    pika.BasicProperties(
        correlation_id="12399942",
        reply_to=NORMALIZER_QUEUE,
    ))
