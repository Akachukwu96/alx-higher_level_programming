#!/usr/bin/python3

"""Print the alphabet in lowercase except q and e."""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{:s}".format(chr(i)), end="")
