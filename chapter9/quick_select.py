# 9.2

from typing import List

from chapter7.quick_sort import partition

def quick_select(nums: List[int], i: int, reverse: bool = False) -> int:
    '''
    Implementation of quick select to select ith smallest number from a list

    :param nums: list of integers to select from
    :param i: ith smallest number (0-indexed)
    :param reverse: will select ith largest number if True
    '''
    l, r = 0, len(nums) - 1
    while l < r:
        j = partition(nums, l, r, reverse)
        if j == i:
            return nums[j]
        if j > i:
            if r == j:
                j -= 1
            r = j
        elif j < i:
            l = j
    return nums[l]  # probably will never hit here
