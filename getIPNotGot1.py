#!/usr/bin/python3
# FileName: getIPNotGot1.py
# Author: lxw
# Date: 2016-01-11

def main():
    f1 = open("./IPResult.csv")
    f = open("./toGetIP.csv", "w")
    while 1:
        line = f1.readline().strip()
        if not line:
            break
        if not line.endswith("/"):
            f.write(line + "\n")

    f1.close()
    f.close()

if __name__ == '__main__':
    main()
else:
    print("Being imported as a module.")

