#!/usr/bin/env python
# -*- coding: utf-8 -*-
from suds.client import Client

def getCreditScore(ssn='123456-1234'):
	client = Client('http://139.59.154.97:8080/CreditScoreService/CreditScoreService?wsdl')
	# no idea why this doesn't work - Teo
	# Marek fixed it
	result = client.service.creditScore(ssn)
	# print "type of ",type(result)
        print "Answer from API:", result
	return result
