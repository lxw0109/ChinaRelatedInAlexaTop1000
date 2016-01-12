#!/usr/bin/python3
# FileName: getIP.py
# Author: lxw
# Date: 2016-01-11

import logging
import socket
import threading
from MyThread.myThread import MyThread

fileLock = threading.RLock()

def getIPSet(lineList, handle):
    """
    ipList is like the following format:
    [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('111.13.101.208', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('111.13.101.208', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_RAW: 3>, 0, '', ('111.13.101.208', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('123.125.114.144', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('123.125.114.144', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_RAW: 3>, 0, '', ('123.125.114.144', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('180.149.132.47', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('180.149.132.47', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_RAW: 3>, 0, '', ('180.149.132.47', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('220.181.57.217', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('220.181.57.217', 0)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_RAW: 3>, 0, '', ('220.181.57.217', 0))]
    """
    ipRes = set([])
    try:
        #ipList: a list of tuple. tuple[4] is also a tuple which store the IP result.
        ipList = socket.getaddrinfo(lineList[1], None)
        for item in ipList:
            ipRes.add(item[4][0])
    except Exception as e:
        #logging is thread safe in Python.
        logging.info(lineList[1] + ": " + str(e))
    content = "{0},{1},".format(lineList[0], lineList[1])
    for ip in ipRes:
        content += ip + "/"

    fileLock.acquire()
    handle.write(content + "\n")
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

    #IP Region
    f = open("./top1000.csv")
    f1 = open("./IPResult.csv", "w")

    threads = []
    while 1:
        line = f.readline().strip()
        if not line:
            break
        lineList = line.split(",")  #line:  "1, google.com"
        if len(threads) < 300:
            mt = MyThread(getIPSet, (lineList, f1))
            mt.start()
            threads.append(mt)
        for thread in threads:
            if thread.isAlive():
                continue
            else:
                threads.remove(thread)
    for thread in threads:
        thread.join()

    f.close()
    f1.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
