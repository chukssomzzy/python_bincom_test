#!/usr/bin/env python3

"""Find the most worn"""

from table import week_color
from collections import Counter


def most_worn(week):
    unique_freq = Counter()

    for arr in week:
        for val in arr:
            unique_freq[val] += 1
    most_color, _ = unique_freq.most_common(1)[0]
    return (most_color)


print(f"Most Common {most_worn(week_color)}")
