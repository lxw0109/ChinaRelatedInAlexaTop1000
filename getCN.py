#!/usr/bin/python3
# FileName: getCN.py
# Author: lxw
# Date: 2016-01-11

def main():
    #".cn"
    f = open("./top1000.csv")
    f1 = open("./cnResult.csv", "w")
    while 1:
        line = f.readline().strip()
        if not line:
            break
        if line.endswith(".cn"):
            f1.write(line + ",.cn\n")
    f.close()
    f1.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")
