import unittest

from typing import List

from chapter6.my_heap import build_heap
from utils.sort_utils import get_compare


def _verify_heap(heap: List[int], i: int, reverse: bool = False) -> bool:
    compare = get_compare(reverse)
    # +1 and -1 to transform from 0-index to 1-index
    l = (i + 1) * 2 - 1
    r = l + 1
    left_result, right_result = True, True
    if l < len(heap):
        if compare(heap[l], heap[i]):
            return False
        left_result = _verify_heap(heap, l, reverse)
    if r < len(heap):
        if compare(heap[r], heap[i]):
            return False
        right_result = _verify_heap(heap, r, reverse)
    return left_result and right_result


class MyHeapTest(unittest.TestCase):

    def test_my_heap(self):
        test_cases = [
            [4, 7, 1, 5, 8, 2, 6, 9, 10, 3],
            [7, 6, 5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 6, 7],
        ]
        for reverse in [True, False]:
            for nums in test_cases:
                build_heap(nums, reverse)
                self.assertTrue(_verify_heap(nums, 0, reverse))

if __name__ == '__main__':
    unittest.main()
