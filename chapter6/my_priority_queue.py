# 6.5

from typing import List, Callable, Any


class PriorityQueue:
    '''Priority queue implementation'''

    def __init__(self,
                 index: Callable[[Any], Any] = lambda x: x,
                 key: Callable[[Any], Any] = lambda x: x,
                 reverse: bool = False,
                 compare: Callable[[Any, Any], bool] = None):
        '''Constructor of priority queue (max priority queue by default)
        
        :param index: callable to transform element into index
            in order to access element in queue with O(1) time
        :param key: callable to transform element into key 
            which represents "priority"
        :param reverse: will construct min priority queue if True
        :param compare: callable to compare two elements
        '''
        self.index = index
        self.key = key
        if compare is not None:
            self.compare = compare
        else:
            def compare(x: Any, y: Any) -> bool:
                if reverse:
                    return self.key(x) <= self.key(y)
                return self.key(x) > self.key(y)
            self.compare = compare
        self.heap = []
        self.position = {}

    def _swap(self, i: int, j: int) -> None:
        '''Swap i and j elements in heap with update to position record'''
        self.position[self.index(self.heap[i])] = j
        self.position[self.index(self.heap[j])] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _float(self, i: int) -> None:
        '''
        Maintain heap property by recursively float element
            to its correct place
        '''
        j = (i+1) // 2 - 1
        if j >= 0 and self.compare(self.heap[i], self.heap[j]):
            self._swap(i, j)
            if j != 0:
                self._float(j)

    def _sink(self, i: int) -> None:
        '''
        Maintain heap property by recursively sink element to its correct place
        aka MAX_HEAPIFY as in the book
        '''
        l = (i + 1) * 2 - 1
        r = l + 1
        target = i
        if l < len(self.heap) and self.compare(self.heap[l], self.heap[target]):
            target = l
        if r < len(self.heap) and self.compare(self.heap[r], self.heap[target]):
            target = r
        if target != i:
            self._swap(target, i)
            self._sink(target)

    def insert(self, x: Any) -> None:
        '''
        Insert element into priority queue
        ala INSERT as in the book
        '''
        if self.index(x) in self.position:
            raise Exception('new value has a duplicate index')
        self.position[self.index(x)] = len(self.heap)
        self.heap.append(x)
        self._float(len(self.heap) - 1)

    def peek(self) -> Any:
        '''
        Return the top element in the priority queue
        aka MAXIMUM as in the book
        '''
        return self.heap[0]

    def extract(self) -> Any:
        '''
        Return the top element and delete it in the priority queue
        aka EXTRACT_MAX as in the book
        '''
        result = self.heap[0]
        del self.position[self.index(result)]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sink(0)
        return result

    def update(self, index: Any, new_value: Any) -> None:
        '''
        Update element according to index
        aka INCREASE_KEY as in the book, but arbitrarily update
        '''
        new_index = self.index(new_value)
        if new_index != index and new_index in self.position:
            raise Exception("new value has a duplicate index")
        i = self.position.pop(index)
        self.heap[i] = new_value
        self.position[new_index] = i
        self._float(i)
        self._sink(i)


def main():
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
    q = PriorityQueue(index=lambda x: x[1], key=lambda x: x[0])
    for action in test_actions:
        if action[0] == 'insert':
            q.insert(action[1])
            expected = action[2]
        elif action[0] == 'extract':
            q.extract()
            expected = action[1]
        elif action[0] == 'update':
            q.update(action[1], action[2])
            expected = action[3]
        if q.peek()[0] != expected:
            print('Peek priority queue does not match expected: {} != {}'.format(
                q.peek()[0], expected))
            return
    print('All test cases passed')

if __name__ == '__main__':
    main()
