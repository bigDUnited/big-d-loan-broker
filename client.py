from rmqPublish import publish_to_q
from queue_names import CREDIT_ENRICHER_QUEUE
import json
import pika

message = {
    "ssn": "123456-3212", #social security number
    "amount": "300", #crowns
    "duration": "60", #days
    "timeout" : "900" #seconds
}

publish_to_q(
    'localhost',
    CREDIT_ENRICHER_QUEUE,
    json.dumps(message),
    pika.BasicProperties(
        correlation_id="12399942",
        reply_to="result",))
