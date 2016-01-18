#!/usr/bin/python2
# FileName: methodGeng.py
# Author: lxw
# Date: 2016-01-18

import logging
from pyquery import PyQuery
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def logConfig():
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='monitor.log',
            filemode='w')

def process(url, handle):
    source = PyQuery(url=url)
    siteList = source.find("li.site-listing").find("a")
    content = ""
    for data in siteList:
        domain = PyQuery(data).text()
        if domain.lower() == "more":
            continue
        else:
            #print domain
            content += domain + "\n"
    handle.write(content)

def main():
    logConfig()
    handle = open("./resultGeng.csv", "w")

    for pageNo in xrange(20):
        url = "http://www.alexa.com/topsites/countries;{0}/CN".format(pageNo)
        process(url, handle)

    handle.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

