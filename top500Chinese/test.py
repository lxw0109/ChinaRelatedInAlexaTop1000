#!/usr/bin/python3
# FileName: methodChen.py
# Author: lxw
# Date: 2016-01-18

import logging
from html.parser import HTMLParser

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        #print("End tag  :", tag)
        pass

    def handle_data(self, data):
        print("Data     :", data)

def logConfig():
    logging.basicConfig(level=logging.WARNING,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='monitor.log',
            filemode='w')

def process(lineList, handle):
    try:
        url = "http://www.alexa.com/siteinfo/" + lineList[1]

        parser = MyHTMLParser()
        parse.feed(sourceCode)


        content = "{0},{1},{2}\n".format(lineList[0], lineList[1], source.find("h4").find("a").text())
        handle.write(content)
        handle.flush()
    except Exception as e:
        logging.error(lineList[0] + "," + lineList[1] + ": " + str(e))

def main():
    line = "1,google.com"
    lineList = line.split(",")
    process(lineList, None)

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

