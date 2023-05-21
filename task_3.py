#!/usr/bin/env python3

"""Get the median from a 2D list of color"""
from collections import Counter
from table import week_color


def median_color(week):
    unique_freq = Counter([color for arr in week for color in arr])
    sorted_color = sorted(unique_freq, key=lambda color: unique_freq[color],
                          reverse=True)
    print(unique_freq.items())
    freq = sum(unique_freq.values())
    median = (freq + 1) / 2
    cumm_freq = 0
    median_color = None
    for color in sorted_color:
        cumm_freq += unique_freq[color]
        if cumm_freq >= median:
            median_color = color
            break
    return median_color


print(median_color(week_color))
