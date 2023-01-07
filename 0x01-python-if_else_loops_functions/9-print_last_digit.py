#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number and return it."""
    ld = abs(number) % 10
    print("{:d}".format(ld), end="")
    return (ld)
