import json
import datetime
import xml.etree.ElementTree as ET
from datetime import date

def dump_danskebank(message):
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
    pass

def dump_nordea(message):
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
    pass


translator_types = {
    "danskebank" : {"dump": dump_danskebank, "load": load_danskebank},
    "nordea" : {"dump": dump_nordea, "load": load_nordea},
}

def dumps(message, type):
    return translator_types[type]["dump"](message)

def loads(message, type):
    return translator_types[type]["load"](message)

