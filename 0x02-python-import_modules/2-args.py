#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    top1 = "arguments"
    no_args = 0
    if length == 0:
        print("{} {}.".format(no_args, top1))
    else:
        print("{} {}:".format(length, top1))

    for i in argv[1:]:
        print("{}: {}".format(argv.index(i), i))
