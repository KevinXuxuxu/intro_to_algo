# 6.1
from typing import List, Any, Callable

def heapify(heap: List[Any],
            i: int,
            reverse: bool = False,
            heap_size: int = None) -> None:
    '''
    Enforce heap property (max heap by default) on ith element of heap
    aka "sink" the element if heap property is violated

    :param heap: input heap as a list of object
    :param i: index of the target element
    :param reverse: will do min_heapify if True
    :param heap_size: size of heap within the list, will be list size if left blank
    '''
    if heap_size is None:
        heap_size = len(heap)
    compare = lambda x, y: x <= y if reverse else x >= y
    # +1 and -1 to transform from 0-index to 1-index
    l = (i + 1) * 2 - 1
    r = l + 1
    target = i
    if l < heap_size and compare(heap[l], heap[target]):
        target = l
    if r < heap_size and compare(heap[r], heap[target]):
        target = r
    if target != i:
        heap[target], heap[i] = heap[i], heap[target]
        heapify(heap, target, reverse, heap_size)


def build_heap(nums: List[int],
               reverse: bool = False) -> None:
    '''
    Build heap (max heap by default) for input list of objects

    :param nums: list of objects for the heap
    :param reverse: build min heap if True
    '''
    # +1 and -1 to transform from 0-index to 1-index
    mid = len(nums) // 2 - 1
    for i in range(mid, -1, -1):
        heapify(nums, i, reverse)
