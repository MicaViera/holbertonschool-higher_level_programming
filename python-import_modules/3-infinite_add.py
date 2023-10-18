#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = 0
    for index in range(len(sys.argv) - 1):
        num += int(sys.argv[index + 1])
    print("{}".format(num))
