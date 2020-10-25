import unittest
import json

from typing import Callable, List

from chapter2.insertion_sort import insertion_sort
from chapter2.merge_sort import merge_sort
from chapter6.heap_sort import heap_sort
from chapter7.quick_sort import quick_sort
from chapter8.counting_sort import counting_sort
from chapter8.radix_sort import radix_sort

RANDOM_SORT_TEST_INPUT = 'test/random_sort_test_cases.json'


class SortTest(unittest.TestCase):

    def _test_sort(self, sort: Callable[[List[int], bool], List[int]]):
        test_cases = [
            ([4, 7, 1, 5, 8, 2, 6, 9, 10, 3], False, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([7, 6, 5, 4, 3, 2, 1], False, [1, 2, 3, 4, 5, 6, 7]),
            ([1, 2, 3, 4, 5, 6, 7], True, [7, 6, 5, 4, 3, 2, 1])
        ]
        for nums, reverse, expected in test_cases:
            result = sort(nums, reverse)
            self.assertEqual(expected, result)
        with open(RANDOM_SORT_TEST_INPUT) as f:
            random_test_cases = json.load(f)
            for nums in random_test_cases:
                result = sort(nums, False)
                benchmark = sorted(nums)
                self.assertEqual(result, benchmark)

    def test_insertion_sort(self):
        self._test_sort(insertion_sort)

    def test_merge_sort(self):
        self._test_sort(merge_sort)

    def test_heap_sort(self):
        def sort(nums: List[int], reverse: bool) -> List[int]:
            heap_sort(nums, reverse)
            return nums
        self._test_sort(sort)

    def test_quick_sort(self):
        def sort(nums: List[int], reverse: bool) -> List[int]:
            quick_sort(nums, 0, len(nums) - 1, reverse)
            return nums
        self._test_sort(sort)

    def test_counting_sort(self):
        def sort(nums: List[int], reverse: bool) -> List[int]:
            return counting_sort(nums, (-10000, 10000), reverse)
        self._test_sort(sort)

    def test_radix_sort(self):
        self._test_sort(radix_sort)


if __name__ == '__main__':
    unittest.main()
