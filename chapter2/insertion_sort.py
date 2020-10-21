# 2.1

import json

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


def main():
    test_cases = [
        ([4, 7, 1, 5, 8, 2, 6, 9, 10, 3], False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([7, 6, 5, 4, 3, 2, 1], False, [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7], True, [7, 6, 5, 4, 3, 2, 1])
    ]
    for nums, reverse, expected in test_cases:
        result = insertion_sort(nums, reverse)
        if not expected == result:
            print('{} != {}'.format(result, expected))
            return
    with open('../random_sort_test_cases.json') as f:
        random_test_cases = json.load(f)
        for nums in random_test_cases:
            result = insertion_sort(nums)
            benchmark = sorted(nums)
            if result != benchmark:
                print('random test failed')
                print(result)
                print(benchmark)
                return
    print('All test cases passed')


if __name__ == '__main__':
    main()