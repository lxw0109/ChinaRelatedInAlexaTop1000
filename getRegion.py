#!/usr/bin/python3
#coding: utf-8
#如果想有中文注释就必须得有上面的语句
# FileName: getRegion.py
# Author: lxw
# Date: 2016-01-11

def main():
    f = open("./IPRegion.csv")
    f1 = open("./regionResult.csv", "w")
    while 1:
        line = f.readline().strip()
        if not line:
            break
        lineList = line.split(",")
        if "中国" in lineList[3]:
            f1.write(line + "\n")

    f1.close()
    f.close()


if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

