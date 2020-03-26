from typing import List, Tuple
from numbers import Number
import random
import time
from copy import deepcopy
from quick_sort import _get_median_element


__all__ = ['quick3_sort']


def quick3_sort(array: List[Number], start: int = None, end: int = None) -> List[Number]:
    if start is None and end is None:
        start, end = 0, len(array) - 1
    if start < end:
        down_equal_index, up_equal_index = _partition(array, start, end)
        quick3_sort(array, start, down_equal_index - 1)
        quick3_sort(array, up_equal_index + 1, end)

    return array


def _partition(array: List[Number], start: int, end: int) -> Tuple[int, int]:
    median = _get_median_element(array, start, end)
    pivot = median[1]
    _swap(array, median[0], end)

    down_equal_index = start
    before_repeat_index = end - 1
    i = start
    while i <= before_repeat_index:
        if array[i] < pivot:
            _swap(array, i, down_equal_index)
            down_equal_index += 1
            i += 1
        elif array[i] == pivot:
            _swap(array, i, before_repeat_index)
            before_repeat_index -= 1
        else:
            i += 1

    up_equal_index = down_equal_index
    while before_repeat_index < end:
        before_repeat_index += 1
        _swap(array, before_repeat_index, up_equal_index)
        up_equal_index += 1

    return down_equal_index,  up_equal_index - 1


def _swap(array: List[Number], first_index: int, second_index: int):
    first = array[first_index]
    second = array[second_index]
    array[first_index] = second
    array[second_index] = first


class Test:
    def __init__(self, array: List[Number]):
        self.array = deepcopy(array)
        t1 = time.time()
        quick3_sort(self.array)
        print(f'time: {time.time() - t1}')
        assert sorted(array) == self.array


if __name__ == '__main__':

    random.seed(13)
    test = [3,3,4,3,3,3,5,7,3]
    Test(test)
    test = [random.randint(0, 100) for _ in range(10)]
    Test(test)
    test = [random.randint(0, 5) for _ in range(30)]
    Test(test)
    test = [random.randint(0, 1000) for _ in range(10000)]
    Test(test)
    test = [random.randint(0, 10) for _ in range(10000)]
    Test(test)
