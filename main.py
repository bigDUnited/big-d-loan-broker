#!/usr/bin/env python
# -*- coding: utf-8 -*-
from suds.client import Client

def getCreditScore():
	client = Client('http://139.59.154.97:8080/CreditScoreService/CreditScoreService?wsdl')
	# no idea why this doesn't work - Teo
	# Marek fixed it
	result = client.service.creditScore('123456-1234')
	# print "type of ",type(result)
	return "Anser from API: " + str(result)

print getCreditScore()
