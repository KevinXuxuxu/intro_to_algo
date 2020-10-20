# 6.4

from typing import List
from my_heap import build_heap, heapify

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


def main():
    test_cases = [
        ([4, 7, 1, 5, 8, 2, 6, 9, 10, 3], False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([7, 6, 5, 4, 3, 2, 1], False, [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7], True, [7, 6, 5, 4, 3, 2, 1])
    ]
    for nums, reverse, expected in test_cases:
        heap_sort(nums, reverse)
        if not expected == nums:
            print('{} != {}'.format(nums, expected))
            return
    print('All test cases passed')


if __name__ == '__main__':
    main()
