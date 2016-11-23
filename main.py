from rulebase import RuleBase
import requests
from creditapi import getCreditScore


score = getCreditScore()
response = requests.get("http://127.0.0.1:3001/score/" + str(score))
print response.json()


