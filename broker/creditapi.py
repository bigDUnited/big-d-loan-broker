#!/usr/bin/env python
# -*- coding: utf-8 -*-
from suds.client import Client
import logging
import xml.etree.ElementTree as ET

def getCreditScore(ssn='123456-1234'):
        """
        Get credit score from third-party web service.
        Takes a social security number.
        """
        client = Client('http://139.59.154.97:8080/CreditScoreService/CreditScoreService?wsdl')
        result = client.service.creditScore(ssn)
        logging.info("Answer from API:{0}".format(result))
        return result

def getBanks(rate):
        client = Client('http://localhost:9999/ws/rule-base?wsdl')
        data = client.service.getBanksByCreditScoreJson(rate)
        root = ET.fromstring(data)
        result = []
        for bank in root.findall('bankElem'):
                name = bank.find("name").text
                result.append(name)
        return result
