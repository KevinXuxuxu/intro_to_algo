# 7.1

import json

from typing import List
from random import randint


def randomize(nums: List[int], l: int, r: int) -> None:
    '''
    Randomize pivot choosing process in partition
    by randomly picking an element from range and swap with last element
    '''
    i = randint(l, r)
    nums[i], nums[r] = nums[r], nums[i]


def partition(nums: List[int], l: int, r: int, reverse: bool = False) -> int:
    '''
    Select pivotal element and partition list with this element
        by arranging elements smaller than pivot before and vise versa
    
    :param nums: list of integers to be partitioned
    :param l: starting index of partitioning range
    :param r: ending index of partitioning range
    :param reverse: will put elements larger than pivot before if True
    :return: final index of pivot
    '''
    compare = lambda x, y: x <= y if reverse else x >= y
    randomize(nums, l, r)
    p = nums[r]
    i = l - 1
    for j in range(l, r):
        if compare(p, nums[j]):
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def my_partition(nums: List[int], l: int, r: int, reverse: bool = False) -> int:
    '''
    Select pivotal element and partition list with this element
        by arranging elements smaller than pivot before and vise versa
    This is my version of doing the partition.
    
    :param nums: list of integers to be partitioned
    :param l: starting index of partitioning range
    :param r: ending index of partitioning range
    :param reverse: will put elements larger than pivot before if True
    :return: final index of pivot
    '''
    compare = lambda x, y: x <= y if reverse else x >= y
    randomize(nums, l, r)
    p = nums[r]
    i, j = l, r-1
    while i < j:
        while i < j and compare(p, nums[i]):
            i += 1
        while i < j and compare(nums[j], p):
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    if compare(p, nums[j]):
        j += 1
    nums[j], nums[r] = nums[r], nums[j]
    return j


def quick_sort(nums: List[int], l: int, r: int, reverse: bool = False) -> None:
    '''
    Implementation of quick sort on integer list
    Will sort input list in ascending order by default

    :param nums: list of integers to be sorted
    :param l: starting index of sorting range
    :param r: ending index of sorting range (inclusive)
    :param reverse: will sort in descending order if True
    '''
    k = partition(nums, l, r, reverse)
    if l < k-1:
        quick_sort(nums, l, k-1, reverse)
    if k+1 < r:
        quick_sort(nums, k+1, r, reverse)


def main():
    test_cases = [
        ([4, 7, 1, 5, 8, 2, 6, 9, 10, 3], False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([7, 6, 5, 4, 3, 2, 1], False, [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7], True, [7, 6, 5, 4, 3, 2, 1])
    ]
    for nums, reverse, expected in test_cases:
        quick_sort(nums, 0, len(nums) - 1, reverse)
        if not expected == nums:
            print('{} != {}'.format(nums, expected))
            return
    with open('../random_sort_test_cases.json') as f:
        random_test_cases = json.load(f)
        for nums in random_test_cases:
            nums_copy = nums.copy()
            quick_sort(nums, 0, len(nums) - 1)
            benchmark = sorted(nums_copy)
            if nums != benchmark:
                print('random test failed')
                print(nums)
                print(benchmark)
                return

    print('All test cases passed')


if __name__ == '__main__':
    main()