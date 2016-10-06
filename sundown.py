import requests
import datetime

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


def lightout():
    sunriseTime = parseJsonTime(sunrise()).split(':')
    sunsetTime = parseJsonTime(sunset()).split(':')
    nowTime = timeNow().split(':')
    print(nowTime[0])
    print(sunriseTime[0])
    print(nowTime[0] < sunriseTime[0])
    if(nowTime[0] > sunriseTime[0]):
        if(nowTime[0] < sunsetTime[0]):
            return True
        else:
            if(nowTime[0] == sunsetTime[0]):
                if(nowTime[1] < sunsetTime[1]):
                    return True
                if(nowTime[1] == sunsetTime[1]):
                    if(nowTime[2] < sunsetTime[2]):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    if(nowTime[0] == sunriseTime[0]):
        if(nowTime[1] > sunriseTime[1]):
            return True
        if(nowTime[1] == sunriseTime[1]):
            if(nowTime[2] >= sunriseTime[2]):
                return True
            else:
                return False
        else:
            return False

    else:
        return False
print(lightout())
