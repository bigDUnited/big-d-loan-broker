#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from random import randint
from flask import Flask
from flask_restful import Resource, Api
from queue_names import *

class RuleBase(object):

    def __init__(self, name, maxScore):
        self.name = name
        self.maxScore = maxScore

    def __str__(self):
        return "{0} {1}".format(self.name, self.maxScore)

    def __repr__(self):
        return self.__str__()

def calculate(score, banks):
    res = []
    for bank in banks:
        if bank.maxScore <= score:
            res.append(bank)
    return res

banks = [
    RuleBase(DANSKEBANK_TRANSLATOR_QUEUE, 200),
    RuleBase(NORDEA_TRANSLATOR_QUEUE, 400),
    RuleBase(NYTKREDIT_TRANSLATOR_QUEUE, 600),
    RuleBase(BDO_TRANSLATOR_QUEUE, 700)
]

def bankToJSON(bank):
    return bank.name

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, score):
        res = map(bankToJSON, calculate(int(score), banks))
        return res

api.add_resource(HelloWorld, '/score/<int:score>')

if __name__ == '__main__':
    app.run(debug=True, port=3001)
