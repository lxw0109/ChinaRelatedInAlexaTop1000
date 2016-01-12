#!/usr/bin/python3
# FileName: getIPNotGot.py
# Author: lxw
# Date: 2016-01-11

def main():
    f1 = open("./IPResult.csv")
    ipGetNum = set([])
    while 1:
        line = f1.readline().strip()
        if not line:
            break
        lineList = line.split(",")
        ipGetNum.add(lineList[0])
    f1.close()

    f2 = open("./top1000.csv")
    f = open("./toGetIP.csv", "w")
    while 1:
        line = f2.readline().strip()
        if not line:
            break
        lineList = line.split(",")
        if lineList[0] not in ipGetNum:
            f.write(line + "\n")
    f2.close()
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

