# 2.1

from typing import List

def insertion_sort(nums: List[int], reverse: bool = False) -> List[int]:
    '''
    Implementation of insertion sort on integer list
    Will sort input list in ascending order by default
    Note that this sort will also sort the input list in-place

    :param nums: list of integers to be sorted
    :param reverse: will sort in descending order if True
    '''
    compare = lambda x, y: x <= y if reverse else x >= y
    for i in range(1, len(nums)):
        x = nums[i]
        j = i
        while j-1 >= 0 and compare(nums[j-1], x):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = x
    return nums
