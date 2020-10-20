# 6.5

from typing import List, Callable, Any


class PriorityQueue:

    def __init__(self,
                 index: Callable[[Any], Any] = lambda x: x,
                 key: Callable[[Any], Any] = lambda x: x,
                 reverse: bool = False,
                 compare: Callable[[Any, Any], bool] = None):
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
        self.position[self.index(self.heap[i])] = j
        self.position[self.index(self.heap[j])] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _float(self, i: int) -> None:
        j = (i+1) // 2 - 1
        if j >= 0 and self.compare(self.heap[i], self.heap[j]):
            self._swap(i, j)
            if j != 0:
                self._float(j)

    def _sink(self, i: int) -> None:
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
        self.position[self.index(x)] = len(self.heap)
        self.heap.append(x)
        self._float(len(self.heap) - 1)

    def peek(self) -> Any:
        return self.heap[0]

    def extract(self) -> Any:
        result = self.heap[0]
        del self.position[self.index(result)]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sink(0)
        return result
