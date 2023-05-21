#!/usr/bin/env python3

"""Calculate the mean color"""
from collections import Counter
from table import week_color


def get_mean_color(week):
    """Calculate the mean color from a 2D array of data

    Arg:
        color (list of list): 2d array of colors worn, each date representing
        a day of the week
    Returns:
        The mean color
    """
    unique_freq = Counter()
    freq = 0
    color_val = dict()
    i = 1

    for arr in week:
        for val in arr:
            unique_freq[val] += 1

    for color in sorted(unique_freq):
        color_val[color] = i
        i = i + 1

    freq = sum(num for _, num in unique_freq.items())
    mean_color = sum(color_val[col] * freq for col, freq in unique_freq.items()
                     ) / freq
    return (mean_color)


print(f"Mean_Color = {get_mean_color(week_color)}")
