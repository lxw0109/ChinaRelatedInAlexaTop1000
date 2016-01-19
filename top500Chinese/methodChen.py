#!/usr/bin/python3
# FileName: methodChen.py
# Author: lxw
# Date: 2016-01-18

import logging
from html.parser import HTMLParser
import urllib.request
import sys

def logConfig():
    logging.basicConfig(level=logging.WARNING,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='monitor.log',
            filemode='w')


class MyHTMLParser(HTMLParser):
    def __init__(self, lineList, handle):
        HTMLParser.__init__(self)
        self.lineList = lineList
        self.handle = handle
        self.isH4 = 0
        self.isRankIn = 0
        self.isA = 0

    def handle_starttag(self, tag, attrs):
        if tag == "h4":
            self.isH4 = 1
            return
        if self.isRankIn == 1:
            if tag == "a":
                self.isA = 1

    def handle_endtag(self, tag):
        if tag == "a":
            self.isA = 0
        if tag == "h4":
            self.isH4 = 0
            self.isRankIn = 0

    def handle_data(self, data):
        if self.isH4 == 1:
            if data.strip().lower() == "rank in":
                self.isRankIn = 1
                return
        if self.isA == 1:
            self.handle.write("{0},{1},{2}\n".format(self.lineList[0], self.lineList[1], data))
            self.handle.flush()


def process(lineList, handle):
    try:
        url = "http://www.alexa.com/siteinfo/" + lineList[1]
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/ 20100101 Firefox/23.0'};
        req = urllib.request.Request(url=url, headers=headers)
        sourceCode = urllib.request.urlopen(req).read().decode("utf-8")
    except Exception as e:
        logging.error(lineList[0] + "," + lineList[1] + ": " + str(e))
    else:
        parser = MyHTMLParser(lineList, handle)
        parser.feed(sourceCode)


def main():
    logConfig()
    handle = open("./resultChen.csv", "w")
    #f = open("./top10k.csv")
    f = open("./logFilterResult.csv")

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

