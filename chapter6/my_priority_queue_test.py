import unittest

from chapter6.my_priority_queue import PriorityQueue

class MyPriorityQueueTest(unittest.TestCase):
    test_actions = [
        ('insert', (1, '1'), 1),
        ('insert', (5, '5'), 5),
        ('insert', (2, '2'), 5),
        ('insert', (4, '4'), 5),
        ('insert', (7, '7'), 7),
        ('extract', 5),
        ('extract', 4),
        ('insert', (6, '6'), 6),
        ('update', '2', (8, '8'), 8),
        ('insert', (3, '3'), 8),
        ('extract', 6),
        ('extract', 4),
        ('extract', 3)
    ]

    def test_my_priority_queue(self):
        q = PriorityQueue(index=lambda x: x[1], key=lambda x: x[0])
        for action in self.test_actions:
            if action[0] == 'insert':
                q.insert(action[1])
                expected = action[2]
            elif action[0] == 'extract':
                q.extract()
                expected = action[1]
            elif action[0] == 'update':
                q.update(action[1], action[2])
                expected = action[3]
            self.assertEqual(q.peek()[0], expected)

if __name__ == '__main__':
    unittest.main()
