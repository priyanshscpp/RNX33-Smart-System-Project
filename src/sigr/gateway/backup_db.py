#!/usr/bin/env python
# 0:0:07 everyday upload gateway.db to server to backup
# gateway.db will save in server for 7 days, server will delete gateway.db older than 7 days
# Priyanshu Yadav 3rd ECE 220105038
# Mentor :- Prof. Kumar Gaurav Phd IIT Kanpur
# import time # F401: 'time' imported but unused
from datetime import datetime  # timedelta was F401
from time import sleep
# import requests # F401: 'requests' imported but unused (re-imported in doFunc)
SECONDS_PER_DAY = 24 * 60 * 60


def doFunc():
    import requests

    url = 'http://www.sips/gateway/123456/upload'
    files = {'file': open('/home/sips/123456/123456.db', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)
    print('upload gateway.db to server...')


def doFirst():
    curTime = datetime.now()
    print(curTime)
    desTime = curTime.replace(hour=0, minute=0, second=7, microsecond=0)  # 0:0:07
    print(desTime)
    delta = desTime - curTime
    sleeptime = delta.total_seconds()
    print("Now day must sleep %d seconds" % sleeptime)
    sleep(sleeptime)
    doFunc()


if __name__ == "__main__":
    doFirst()
