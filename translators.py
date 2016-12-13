import json
import xml.etree.ElementTree as ET

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
    res = json.loads(message)
    res["interest"] = float(res["interestRate"])
    del res["interestRate"]
    res["ssn"] = "{}-{}".format(res["ssn"][:6], res["ssn"][6:])
    return res

def dump_nordea(message):
    pass

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

