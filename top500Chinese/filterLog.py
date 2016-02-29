#!/usr/bin/python2.7
# FileName: filterLog.py
# Author: lxw
# Date: 2016-01-19

def main():
    f = open("./monitor.log")
    f1 = open("./logFilterResult.csv", "w")
    """
    Tue, 19 Jan 2016 00:48:57 methodChen.py[line:29] ERROR 2,facebook.com: HTTPConnectionPool(host='www.alexa.com', port=80): Max retries exceeded with url: /siteinfo/facebook.com (Caused by <class 'socket.error'>: [Errno 104] Connection reset by peer)
    """
    while 1:
        line = f.readline().strip()
        if not line:
            break
        lineList = line.split(",")
        number = lineList[1].split()[6]
        url = lineList[2].split(":")[0]
        f1.write("{0},{1}\n".format(number, url))

    f1.close()
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")


