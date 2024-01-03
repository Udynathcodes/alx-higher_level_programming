#!/usr/bin/python3
for n in range(8):
    for i in range(1, 10):
        if n != i and n < i:
            print("{}{}".format(n, i), end=", ")
print(89)
