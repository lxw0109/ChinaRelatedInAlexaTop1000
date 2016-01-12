#!/usr/bin/python2
# FileName: getIPRegion.py
# Author: lxw
# Date: 2016-01-11

import json
import urllib2
import threading
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

fileLock = threading.RLock()

class location_taobao(object):
    '''
    Build the map of IP and its location.
    The location info is from Taobao
    e.g. http://ip.taobao.com/service/getIpInfo.php?ip=218.211.14.165
    The getIpInfo API from Taobao returns a JSON object.
    '''
    def __init__(self, ip):
        self.ip = ip
        self.url = "http://ip.taobao.com/service/getIpInfo.php?ip={0}".format(self.ip)
        #NOTE: OK.
        #Call another method in the CONSTRUCTOR(__init__()).
        self.location = self.getLocation()

    def getLocation(self):
        '''
        Get the location info from self.url.
        The location info are involved in the JSON object returned.
        '''
        #"urlopen()" is like the built-in function "open()" for "file".
        urlobj = urllib2.urlopen(self.url)
        data = urlobj.read()    #str
        dataDict = json.loads(data, encoding="utf-8")     # dict
        return dataDict["data"]     #The type of dataDict["data"] is still dict.

    def getCountry(self):
        #self.location can be str("invalid Ip") or dict.
        try:
            result = self.location.get(u"country")
        except:
            pass
        else:
            return result

    def getRegion(self):
        try:
            result = self.location.get(u"region")
        except:
            pass
        else:
            return result

    def getCity(self):
        try:
            result = self.location.get(u"city")
        except:
            pass
        else:
            return result

    def getISP(self):
        try:
            result = self.location.get(u"isp")
        except:
            pass
        else:
            return result

def getCountry(lineList, handle):
    ipList = lineList[2].split("/")
    regionSet = set([])
    for ip in ipList:
        obj = location_taobao(ip)
        country = obj.getCountry()
        if country is not None:
            regionSet.add(country)
    content = "{0},{1},{2},".format(lineList[0], lineList[1], lineList[2])
    for region in regionSet:
        content += region + "/"

    fileLock.acquire()
    handle.write(content + "\n")
    handle.flush()
    fileLock.release()


def main():
    f = open("./IPResult.csv")
    f1 = open("./IPRegion.csv", "w")

    threads = []
    while 1:
        line = f.readline().strip()
        if not line:
            break
        lineList = line.split(",")
        getCountry(lineList, f1)

    f1.close()
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
