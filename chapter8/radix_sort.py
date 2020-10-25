# 8.3

from typing import List


def _get_digit(num: int, digit: int) -> int:
    '''
    Get a certain digit from a number
    Will return None if the digit is larger than the number
    e.g. _get_digit(1234, 0) == 4, _get_digit(123, 5) == None

    :param num: the number to get digit from
    :param digit: the digit to get, 0-indexed from right to left
    :return: the wanted digit
    '''
    i = digit
    while i > 0:
        num //= 10
        i -= 1
    if num == 0:
        return None
    return num % 10


def radix_sort(nums: List[int], reverse: bool = False) -> List[int]:
    '''
    Implementation of radix sort on integer list
    Will sort input list in ascending order by default
    Note that this sort will also sort the input list in-place

    :param nums: list of integers to be sorted
    :param reverse: will sort in descending order if True
    '''
    digit = 0
    _min = min(nums)
    result = [num - _min for num in nums]
    while True:
        d = [[] for _ in range(10)]
        all_none = True
        for num in result:
            i = _get_digit(num, digit)
            if i is not None:
                all_none = False
                d[i].append(num)
            else:
                d[0].append(num)
        if all_none:
            break
        result = []
        for i in (range(9, -1, -1) if reverse else range(10)):
            for num in d[i]:
                result.append(num)
        digit += 1
    return [num + _min for num in result]
