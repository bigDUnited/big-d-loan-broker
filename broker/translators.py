"""
Message format translation utilities.
"""
import json
import datetime
import xml.etree.ElementTree as ET
from datetime import date

def dump_danskebank(message):
    """
    Example input: {
     "ssn": "123456-3212",
     "amount": "3000",
     "duration": "7000", 
     "timeout" : "900",
     "score": "3000",
    }
    """
    res = message
    res["loanAmount"] = float(res["amount"])
    del res["amount"]
    res["loanDuration"] = int(res["duration"])
    del res["duration"]
    del res["score"]
    res["ssn"] = long("".join(res["ssn"].split("-")))
    del res["timeout"]
    return json.dumps(res)

def load_danskebank(message):
    """
    Example input: {"interestRate":5.5,"ssn":1234563212}
    """
    res = json.loads(message)
    res["interest"] = float(res["interestRate"])
    del res["interestRate"]
    res["ssn"] = str(res["ssn"])
    newssn = "{}-{}".format(res["ssn"][:6], res["ssn"][6:])
    res["ssn"] = newssn
    return res

def dump_nordea(message):
    """
    Example input: {
     "ssn": "123456-3212",
     "amount": "3000",
     "duration": "7000", 
     "timeout" : "900",
     "score": "3000",
    }
    """
    res = ET.Element('LoanRequest')
    ssn = ET.SubElement(res, 'ssn')
    ssn.text = "".join(message["ssn"].split("-"))
    score = ET.SubElement(res, 'creditScore')
    score.text = str(int(message['score']))
    amount = ET.SubElement(res, 'loanAmount')
    amount.text = str(float(message['amount']))
    duration = ET.SubElement(res, 'loanDuration')
    d = date.fromtimestamp(0)
    end = d + datetime.timedelta(days=int(message['duration']))
    duration.text = '{0} 00:00:00.0 CET'.format(end.strftime('%Y-%m-%d'))
    return ET.tostring(res)

def load_nordea(message):
    """
    Example input: 
    <LoanResponse>
       <interestRate>4.5600000000000005</interestRate>
       <ssn>1234563212</ssn>
    </LoanResponse>
    """
    res = {}
    root = ET.fromstring(message)
    res["interest"] = float(root.find("interestRate").text)
    ssn = root.find("ssn").text
    res["ssn"] = "{}-{}".format(ssn[:6], ssn[6:])
    return res

"""
Tables for bi-directional translation.
Each translation type should have a "dump" and a "load"
that should point to corresponding translation functions
that take a message and return a translated message.
"""
translator_types = {
    "danskebank" : {"dump": dump_danskebank, "load": load_danskebank},
    "nordea" : {"dump": dump_nordea, "load": load_nordea},
    "nytkredit" : {"dump": dump_danskebank, "load": load_danskebank},
    "bdo" : {"dump": dump_danskebank, "load": load_danskebank},
}

def dumps(message, type):
    """
    Transforms internal messages to external formats for usage with
    third-party services.
    """
    return translator_types[type]["dump"](message)

def loads(message, type):
    """
    Transform external message formats to internal message format.
    """
    return translator_types[type]["load"](message)


if __name__ == '__main__':
    print load_nordea(
        """    
       <LoanResponse>
        <interestRate>4.5600000000000005</interestRate>
        <ssn>1234563212</ssn>
       </LoanResponse>
        """)
