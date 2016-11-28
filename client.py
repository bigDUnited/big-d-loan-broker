from rmqPublish import publish_to_q
from queue_names import CREDIT_ENRICHER_QUEUE
import json

message = {"ssn": "123456-3212", "amount": "300", "duration": "60"}
publish_to_q('localhost', CREDIT_ENRICHER_QUEUE, json.dumps(message))
