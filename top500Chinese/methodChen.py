#!/usr/bin/python2
# FileName: methodChen.py
# Author: lxw
# Date: 2016-01-18

import threading
import logging
from pyquery import PyQuery
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def logConfig():
    logging.basicConfig(level=logging.WARNING,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='monitor.log',
            filemode='w')

def process(lineList, handle):
    try:
        url = "http://www.alexa.com/siteinfo/" + lineList[1]
        source = PyQuery(url=url)
        content = "{0},{1},{2}\n".format(lineList[0], lineList[1], source.find("h4").find("a").text())
        handle.write(content)
        handle.flush()
    except Exception as e:
        logging.error(lineList[0] + "," + lineList[1] + ": " + str(e))

def main():
    logConfig()
    handle = open("./resultChen.csv", "w")
    #f = open("./top10k.csv")
    f = open("./900.csv")

    while 1:
        line = f.readline().strip()
        if not line:
            break
        lineList = line.split(",")  #line:  "1,google.com"
        process(lineList, handle)

    f.close()
    handle.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

