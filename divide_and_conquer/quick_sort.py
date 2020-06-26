from typing import List, Tuple
from numbers import Number
import random
import time
from copy import deepcopy

__all__ = ['quick_sort']


def quick_sort(array: List[Number], start: int = None, end: int = None) -> List[Number]:
    if start is None and end is None:
        start, end = 0, len(array) - 1
    if start < end:
        p_index = _partition(array, start, end)
        quick_sort(array, start, p_index - 1)
        quick_sort(array, p_index + 1, end)

    return array


def _partition(array: List[Number], start: int, end: int) -> int:
    median = _get_median_element(array, start, end)
    pivot = median[1]
    _swap(array, median[0], end)

    p_index = start
    for i in range(start, end):
        if array[i] <= pivot:
            _swap(array, i, p_index)
            p_index += 1
    _swap(array, end, p_index)

    return p_index


def _swap(array: List[Number], first_index: int, second_index: int):
    first = array[first_index]
    second = array[second_index]
    array[first_index] = second
    array[second_index] = first


def _get_median_element(array: List[Number], start: int, end: int) -> Tuple[int, Number]:
    mean_index = int((end - start) / 2)
    sub_array = [(start, array[start]), (mean_index, array[mean_index]), (end, array[end])]
    for i in range(len(sub_array)):
        for j in range(len(sub_array)):
            if sub_array[i][1] > sub_array[j][1]:
                i_elem = sub_array[i]
                j_elem = sub_array[j]
                sub_array[j] = i_elem
                sub_array[i] = j_elem

    return sub_array[1]


class Test:
    def __init__(self, array: List[Number]):
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
    test = [random.randint(0, 10) for _ in range(10000)]
    Test(test)
