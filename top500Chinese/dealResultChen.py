#!/usr/bin/python3
# FileName: dealResultChen.py
# Author: lxw
# Date: 2016-01-20

def main():
    with open("./result.csv") as f1:
        with open("./resultChenRank.csv", "w") as f2:
            while 1:
                line = f1.readline().strip()
                if not line:
                    break
                lineList = line.split(",")
                f2.write("{0},{1}\n".format(lineList[0], lineList[1]))

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")


