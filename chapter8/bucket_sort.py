# 8.4

from typing import List, Tuple

from chapter2.insertion_sort import insertion_sort

def bucket_sort(nums: List[int],
                _range: Tuple[int, int],
                reverse: False) -> List[int]:
    '''
    Implementation of bucket sort on integer list
    Will sort input list in ascending order by default
    Note that implementation assumes that `nums` is a integer list
        generated from a uniform probability distribution on `range`,
        otherwise it doesn't have an average O(n) time complexity

    :param nums: list of integers to be sorted
    :param range: range from which the input numbers are generated
    :param reverse: will sort in descending order if True
    '''
    n = len(nums)
    _min, _max = _range
    bucket_size = (_max - _min + 1) // n
    buckets = [[] for i in range(n + 1)]
    for num in nums:
        i = (num - _min) // bucket_size
        buckets[i].append(num)
    result = []
    for bucket in (buckets[::-1] if reverse else buckets):
        result += insertion_sort(bucket, reverse)
    return result
