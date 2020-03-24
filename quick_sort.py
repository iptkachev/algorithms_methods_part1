from typing import Iterable
from numbers import Number
import random
import time
from copy import deepcopy


def quick_sort(array: Iterable[Number], start=None, end=None) -> Iterable[Number]:
    if start is None and end is None:
        start, end = 0, len(array) - 1
    if start < end:
        p_index = _partition(array, start, end)
        quick_sort(array, start, p_index - 1)
        quick_sort(array, p_index + 1, end)

    return array


def _partition(array: Iterable[Number], start: int, end: int) -> int:
    random_pivot_index = random.randint(start, end)
    pivot = array[random_pivot_index]
    _swap(array, random_pivot_index, end)
    p_index = start
    for i in range(start, end):
        if array[i] <= pivot:
            _swap(array, i, p_index)
            p_index += 1
    _swap(array, end, p_index)
    return p_index


def _swap(array, first_index: int, second_index: int):
    first = array[first_index]
    second = array[second_index]
    array[first_index] = second
    array[second_index] = first


class Test:
    def __init__(self, array: Iterable[Number]):
        self.array = deepcopy(array)
        t1 = time.time()
        quick_sort(self.array)
        print(f'time: {time.time() - t1}')
        assert sorted(array) == self.array


if __name__ == '__main__':

    random.seed(13)

    test = [random.randint(0, 100) for _ in range(100)]
    Test(test)
    test = [random.randint(0, 4) for _ in range(10)]
    Test(test)
    test = [random.randint(0, 1000) for _ in range(10000)]
    Test(test)
    test = [random.randint(0, 5) for _ in range(10000)]
    Test(test)
    test = [random.randint(0, 1000) for _ in range(10000)]
    Test(test)
