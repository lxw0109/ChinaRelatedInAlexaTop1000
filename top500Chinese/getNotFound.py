#!/usr/bin/python3
# FileName: getNotFound.py
# Author: lxw
# Date: 2016-01-19

def main():
    found = set([])
    with open("./resultChen1.csv") as f1:
        while 1:
            line = f1.readline().strip()
            if not line:
                break
            found.add(line.split(",")[0])

    with open("./top10k.csv") as f2:
        with open("./notFound.csv", "w") as f3:
            while 1:
                line = f2.readline().strip()
                if not line:
                    break
                lineList = line.split(",")
                if lineList[0] not in found:
                    f3.write("{0},{1}\n".format(lineList[0], lineList[1]))


if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

