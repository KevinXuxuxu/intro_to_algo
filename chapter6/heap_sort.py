# 6.4

from typing import List

from chapter6.my_heap import build_heap, heapify

def heap_sort(nums: List[int], reverse: bool = False) -> None:
    '''
    Implementation of heap sort on integer list
    Will sort input list in ascending order by default
    Note that this is an in-place sort

    :param nums: list of integers to be sorted
    :param reverse: will sort in descending order if True
    '''
    build_heap(nums, reverse)
    nums[0], nums[-1] = nums[-1], nums[0]
    for i in range(len(nums) - 1, 1, -1):
        heapify(nums, 0, reverse, i)
        nums[0], nums[i-1] = nums[i-1], nums[0]
