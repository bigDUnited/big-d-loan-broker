#!/usr/bin/env python
# -*- coding: utf-8 -*-
from suds.client import Client
import logging

def getCreditScore(ssn='123456-1234'):
        client = Client('http://139.59.154.97:8080/CreditScoreService/CreditScoreService?wsdl')
        result = client.service.creditScore(ssn)
        logging.info("Answer from API:{0}".format(result))
        return result
