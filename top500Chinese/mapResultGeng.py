#!/usr/bin/python3
# FileName: mapResultGeng.py
# Author: lxw
# Date: 2016-01-20

def main():
    rankDict = {}
    with open("./top10k.csv") as f1:
        while 1:
            line = f1.readline().strip()
            if not line:
                break
            lineList = line.split(",")
            rankDict[lineList[1]] =  lineList[0]

    with open("./resultGeng.csv") as f1:
        with open("./resultGengRank.csv", "w") as f2:
            while 1:
                domain = f1.readline().strip().lower()
                if not domain:
                    break
                f2.write("{0},{1}\n".format(rankDict[domain], domain))


if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

