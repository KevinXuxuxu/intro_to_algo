# 2.3.1

from typing import List

def merge_sort(nums: List[int], reverse: bool = False) -> List[int]:
    '''
    Implementation of merge sort on integer list
    Will sort input list in ascending order by default

    :param nums: list of integers to be sorted
    :param reverse: will sort in descending order if True
    '''
    compare = lambda x, y: x <= y if reverse else x >= y
    if len(nums) <= 1:
        return nums
    if len(nums) == 2:
        if compare(nums[0], nums[1]):
            # swap the 2 elements
            return [nums[1], nums[0]]
        else:
            return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid], reverse)
    right = merge_sort(nums[mid:], reverse)
    i, j = 0, 0
    result = []
    while i < len(left) or j < len(right):
        # pick right[j]
        if i == len(left) or (j < len(right) and compare(left[i], right[j])):
            result.append(right[j])
            j += 1
        # pick left[i]
        elif j == len(right) or (i < len(left) and compare(right[j], left[i])):
            result.append(left[i])
            i += 1
    return result
