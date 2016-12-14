#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dummy service that provides a random credit score. 
"""
import json
from random import randint
from flask import Flask
from flask_restful import Resource, Api


def randit():
    if 1 == 1:
        print "DSDS"

    return randint(500, 1000)

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'creditScore': str(randit())}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=3000)

