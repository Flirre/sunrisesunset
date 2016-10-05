import requests
from datetime import datetime

timeurl = 'http://api.sunrise-sunset.org/json?lat=36.720160x0&lng=-4.4203400&date=today'


def getStats():
    jsonSunStats = requests.get(timeurl).json()
    results = jsonSunStats['results']
    return results


def sunrise():
    return getStats()['sunrise']


def sunset():
    return getStats()['sunset']


def timeNow():
    nowFull = datetime.now().time()
    now = nowFull.strftime('%H:%M:%S.%2f')
    return now[:-4]


def parseJsonTime(s):
    slist = s[:-3]
    if(s[-2:] == 'PM'):
        x = int(s[:1]) + 12
        slist = str(x) + s[1:-3]  # Credits to @tairoman.
    return slist                  # He is 420 friendly.


# print(sunrise())
# print(sunset())
# print(timeNow())

print(parseJsonTime(sunrise()))
