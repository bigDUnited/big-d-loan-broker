from rmqPublish import publish_to_q
from queue_names import *
import json
import pika

message = {
    "ssn": "123456-3212", #social security number
    "amount": "3000", #crowns
    "duration": "7000", #days
    "timeout" : "900", #seconds
    "score": "3000",
}
publish_to_q(
    'localhost',
    DANSKEBANK_TRANSLATOR_QUEUE,
    json.dumps(message),
    pika.BasicProperties(
        correlation_id="12399942",
        reply_to="danskebank",
    ))
