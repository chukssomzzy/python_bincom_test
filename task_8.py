#!/usr/bin/python3

"""Generate random 1 and 0 and convert to decimal"""
from random import randint


def rand_decimal():
    """convert binary generated from randint to decimal"""

    bin_num = ""
    for _ in range(4):
        bin_num += str(randint(0, 1))
    return(int(bin_num, 2))

print(rand_decimal())
