#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
