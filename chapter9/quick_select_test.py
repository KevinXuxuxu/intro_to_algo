import json
import unittest

from random import randint

from chapter9.quick_select import quick_select

RANDOM_SORT_TEST_INPUT = 'test/random_sort_test_cases.json'

class QuickSelectTest(unittest.TestCase):

    test_cases = [
        (
            [3,5,4,2,6,8,1,9,7,10],
            [
                (0, False, 1),
                (3, False, 4),
                (7, False, 8),
                (0, True, 10),
                (4, True, 6),
                (8, True, 2)
            ]
        ),
        (
            [1,1,1,1,5,5,5,2,2,4,4,4,4,4,3],
            [
                (0, False, 1),
                (3, False, 1),
                (4, False, 2),
                (2, True, 5),
                (3, True, 4),
                (8, True, 3)
            ]
        )
    ]

    def test_quick_select(self):
        for nums, cases in self.test_cases:
            for i, reverse, expected in cases:
                self.assertEqual(quick_select(nums.copy(), i, reverse), expected)
        
        with open(RANDOM_SORT_TEST_INPUT) as f:
            random_number_lists = json.load(f)
            for nums in random_number_lists:
                n = len(nums)
                sorted_nums = sorted(nums)
                for _ in range(20):  # 20 select tests for each list
                    i = randint(0, n-1)
                    self.assertEqual(quick_select(nums.copy(), i), sorted_nums[i])


if __name__ == '__main__':
    unittest.main()
