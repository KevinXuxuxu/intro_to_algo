# 8.2

import json

from typing import List, Tuple

def counting_sort(nums: List[int],
                  num_range: Tuple[int, int],
                  reverse: bool = False) -> List[int]:
    '''
    Implementation of counting sort on integer list
    Will sort input list in ascending order by default

    :param nums: list of integers to be sorted
    :param num_range: range of input integers (inclusive)
    :param reverse: will sort in descending order if True
    '''
    _min, _max = num_range
    counter = [0] * (_max - _min + 1)
    for num in nums:
        counter[num - _min] += 1
    if reverse:
        for i in range(len(counter) - 2, -1, -1):
            counter[i] += counter[i+1]
    else:
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
    result = [None] * len(nums)
    for num in nums:
        result[counter[num - _min] - 1] = num
        counter[num - _min] -= 1
    return result

def main():
    test_cases = [
        ([4, 7, 1, 5, 8, 2, 6, 9, 10, 3], False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([7, 6, 5, 4, 3, 2, 1], False, [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7], True, [7, 6, 5, 4, 3, 2, 1])
    ]
    for nums, reverse, expected in test_cases:
        result = counting_sort(nums, (0, 12), reverse)
        if not expected == result:
            print('{} != {}'.format(result, expected))
            return
    with open('../random_sort_test_cases.json') as f:
        random_test_cases = json.load(f)
        for nums in random_test_cases:
            result = counting_sort(nums, (-10000, 10000))
            benchmark = sorted(nums)
            if result != benchmark:
                print('random test failed')
                print(result)
                print(benchmark)
                return
    print('All test cases passed')


if __name__ == '__main__':
    main()
