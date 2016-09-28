# requires "requests"
import requests
import json
from datetime import datetime


def getStats():
    jsonSunStats = requests.get('http://api.sunrise-sunset.org/json?lat=36.720160x0&lng=-4.4203400&date=today').json()
    results = jsonSunStats['results']
    return results


def sunrise():
    return getStats()['sunrise']


def sunset():
    return getStats()['sunset']


def timeNow():
    
    nowFull = datetime.now().time()
    now = nowFull.strftime('%H:%M:%S.%2f')
    return now[:-3]


def parseTime(s):
    
print(sunrise())
print(sunset())
print(timeNow())
