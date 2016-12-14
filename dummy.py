"""
Dummy publisher.
"""
from rmqPublish import publish_to_q
from queue_names import *
import json
import pika

message = json.dumps({
    "ssn": "123456-3212", #social security number
    "amount": "3000", #crowns
    "duration": "7000", #days
    "timeout" : "900", #seconds
    "score": "3000",
})

# message = """
# <LoanRequest>
# <ssn>12345678</ssn>
# <creditScore>685</creditScore>
# <loanAmount>1000.0</loanAmount>
# <loanDuration>1973-01-01 01:00:00.0 CET</loanDuration>
# </LoanRequest>
# """


publish_to_q(
    'localhost',
    NORDEA_TRANSLATOR_QUEUE,
    message,
    pika.BasicProperties(
        correlation_id="12399942",
        reply_to="result",
    ))
