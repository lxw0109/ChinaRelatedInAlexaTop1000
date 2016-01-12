#!/usr/bin/python3
#coding: utf-8
#如果想有中文注释就必须得有上面的语句
# FileName: getContent.py
# Author: lxw
# Date: 2016-01-11

import re
import urllib.request
import urllib.error
import threading
import logging
from MyThread.myThread import MyThread
import sys
reload(sys)
sys.setdefaultencoding('gbk')

fileLock = threading.RLock()

def ifZHStr(string):
    """
    string; the target string to be tested.
    """
    string = string
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    #match = zhPattern.search(unicode(string))
    match = zhPattern.search(string)
    #print(match)
    return match

def monitorPrefix(url):
    zhFlag = False
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/ 20100101 Firefox/23.0'};
        req = urllib.request.Request(url=url, headers=headers)
        sourceCode = urllib.request.urlopen(req).read().decode("utf-8")
    except Exception as e:
        logging.warning(url + ", Exception:" + str(e))
    else:
        codeList = sourceCode.splitlines()
        length = len(codeList)
        for index in range(length):
            string = str(codeList[index].strip())
            if ifZHStr(string):
                zhFlag = True
                break
    return zhFlag

def monitor(lineList, handle):
    """
    monitor each url.
    """
    content = "{0},{1},".format(lineList[0], lineList[1])
    url = "http://www." + lineList[1]
    if monitorPrefix(url):
        fileLock.acquire()
        handle.write(content + "Y\n")
        fileLock.release()
    else:
        fileLock.acquire()
        handle.write(content + "N\n")
        fileLock.release()

def logConfig():
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='monitor.log',
            filemode='w')

def main():
    #config the log.
    logConfig()

    #Chinese
    f = open("./top1000.csv")
    f1 = open("./contentResult.csv", "w")

    threads = []
    while 1:
        line = f.readline().strip()
        if not line:
            break
        lineList = line.split(",")  #line:  "1, google.com"
        if len(threads) < 300:
            mt = MyThread(monitor, (lineList, f1))
            mt.start()
            threads.append(mt)
        for thread in threads:
            if thread.isAlive():
                continue
            else:
                threads.remove(thread)

    for thread in threads:
        thread.join()

    f1.close()
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
