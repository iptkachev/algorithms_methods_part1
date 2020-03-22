from typing import Iterable
from numbers import Number


def quick_sort(array: Iterable[Number], start=None, end=None) -> Iterable[Number]:
    if start == None and end == None:
        start, end = 0, len(array) - 1
    if start < end:
        p_index = _partition(array, start, end)
        quick_sort(array, start, p_index - 1)
        quick_sort(array, p_index + 1, end)

    return array


def _partition(array: Iterable[Number], start: int, end: int) -> int:
    pivot = array[end]
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


if __name__ == '__main__':
    test = [1, 4, 2, 3, 32, 5, 9, 1,2, 35, 9, 3, 0]
    print(quick_sort(test))
