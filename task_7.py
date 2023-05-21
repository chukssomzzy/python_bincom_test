#!/usr/bin/env python3

#import pdb
#pdb.set_trace()

"""Recursively find a number from a list of numbers """


def find_number(numbers=[], num=0, i=0):
    """finds a number from a list of numbers

    Args:
        numbers (list): contains the lists of numbers to find the number in
        num (int): the number to find
        i (int): Used to index the array recursively
    """
    if numbers[i] == num:
        return (num, i)
    elif i >= len(numbers) - 1:
        return "not found in list"
    return(find_number(numbers, num, i + 1))


# Test

numbers = [5, 6, 7, 9, 10]
assert find_number(numbers, 10), (7, 2)
