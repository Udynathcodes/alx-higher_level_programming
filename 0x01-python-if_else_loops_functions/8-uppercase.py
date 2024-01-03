#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            x = ord(i) - 32
            result += chr(x)
        else:
            result += i
    print("{}".format(result))
