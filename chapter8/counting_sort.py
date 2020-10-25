# 8.2
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
