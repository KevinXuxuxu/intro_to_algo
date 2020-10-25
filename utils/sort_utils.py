from typing import Callable

def get_compare(reverse: bool) -> Callable[[int, int], bool]:
    # lambda x, y: x <= y if reverse else x >= y
    if reverse:
        return lambda x, y: x <= y
    return lambda x, y: x >= y
