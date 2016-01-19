#!/usr/bin/python2
# FileName: methodChen.py
# Author: lxw
# Date: 2016-01-18

import threading
import logging
from pyquery import PyQuery
import sys
from myThread import MyThread
import time

reload(sys)
sys.setdefaultencoding("utf-8")

fileLock = threading.RLock()

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
        content = "{0},{1},{2}".format(lineList[0], lineList[1], source.find("h4").find("a").text())
        fileLock.acquire()
        handle.write(content)
        handle.flush()
        fileLock.release()
    except Exception as e:
        logging.error(lineList[1] + str(e))

def main():
    logConfig()
    handle = open("./resultChen.csv", "w")
    f = open("./top5k.csv")

    threads = []
    while 1:
        line = f.readline().strip()
        if not line:
            break
        lineList = line.split(",")  #line:  "1,google.com"
        if len(threads) < 10:
            mt = MyThread(process, (lineList, handle))
            mt.start()
            time.sleep(1)
            threads.append(mt)

        for thread in threads:
            if thread.isAlive():
                continue
            else:
                threads.remove(thread)

    for thread in threads:
        thread.join()
    f.close()
    handle.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

