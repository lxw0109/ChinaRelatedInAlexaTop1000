#!/usr/bin/python3
# FileName: filterLog.py
# Author: lxw
# Date: 2016-01-12

def main():
    domainDict = {}
    f1 = open("./top1000.csv")
    while 1:
        line = f1.readline().strip()
        if not line:
            break
        lineList = line.split(",")
        domainDict[lineList[1]] = lineList[0]
    #print(domainDict)
    f1.close()

    f2 = open("./logUTF8")
    f = open("./logResult.csv", "w")
    while 1:
        line = f2.readline().strip()
        if not line:
            break
        f.write(domainDict[line] + "," + line + ",Y\n")

    f2.close()
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")


