import requests
import datetime
# this program uses an API from http://sunrise-sunset.org/api

timeurl = 'http://api.sunrise-sunset.org/json?lat=57.708870&lng=11.974560&date=today' # might need adjustment for DST(sommartid)


def getStats():
    jsonSunStats = requests.get(timeurl).json()
    results = jsonSunStats['results']
    return results


def sunrise():
    return getStats()['sunrise']


def sunset():
    return getStats()['sunset']


def timeNow():
    nowFull = datetime.datetime.now()
    nowFull = nowFull.replace(year=1900, month=1, day=1) # scrub away the year for comparison
    return nowFull

def parseJsonTime(s):
    slist = s[:-3]
    if(s[-2:] == 'PM'):
        x = int(s[:1]) + 12
        slist = str(x) + s[1:-3]  # Credits to @tairoman.
    return slist                  # He is 420 friendly.


def lightout():
    sunriseTime = datetime.datetime.strptime(parseJsonTime(sunrise()), "%H:%M:%S")
    sunsetTime = datetime.datetime.strptime(parseJsonTime(sunset()), "%H:%M:%S")
    nowTime = timeNow()
    return (nowTime >= sunriseTime and nowTime <= sunsetTime)


lightout()
