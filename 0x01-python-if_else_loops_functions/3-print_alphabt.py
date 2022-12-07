#!/usr/bin/python3

"""Print the alphabet in lowercase except q and e."""
for i in range(97, 123):
    if chr(i) is not 'q' and chr(i) is not 'e':
        print("{}".format(chr(i), end="")
