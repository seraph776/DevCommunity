#!/usr/bin/env python3
"""
created: 2022-08-21 07:36:17
@author: seraph★776
contact: seraph776@gmail.com
"""


def binary_search(lst, target_number):
    """Binary Search Algorithm"""
    # 1. Define low_index & high_index:
    low_index = 0
    high_index = len(lst) - 1

    # 2. Start while loop:
    while low_index <= high_index:
        # 3. Define middle_index:
        middle_index = (low_index + high_index) // 2
        # 4. If target_number == middle_index, then return True:
        if target_number == lst[middle_index]:
            return True
        # 5. If target_number is less than middle_index,
        # then high_index becomes middle_index - 1:
        elif target_number < lst[middle_index]:
            high_index = middle_index - 1
        else:
            # 6. If target_number is greater than middle_index,
            # then the low_index-index becomes middle_index:
            low_index = middle_index + 1
    # 7. If NO target_number, then return False:
    return False
