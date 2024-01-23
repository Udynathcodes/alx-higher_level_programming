#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    k = 0
    try:
        while k != x:
            print(my_list[i], end="")
            i += 1
            k += 1
        print("\n", end="")
        return x
    except IndexError:
        count = 0
        for i in my_list:
            count += 1
        print("\n", end="")
        return count
