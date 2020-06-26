from typing import List, Tuple
from numbers import Number
import random
from copy import deepcopy

__all__ = ['quick3_sort']


def binary_search_tuples(array_sorted: List[Tuple[Number, Number]], point: Number, index_tuple: int,
                         mode: str) -> int:

    if not array_sorted:
        array.sort()
    start_i, end_i = 0, len(array) - 1

    search_index = -1
    while start_i <= end_i:
        average_i = (start_i + end_i) // 2
        if mode == 'greater':
            if array_sorted[average_i][index_tuple] <= point:
                start_i = average_i + 1
            else:
                search_index = average_i
                end_i = average_i - 1
        elif mode == 'less':
            if array_sorted[average_i][index_tuple] >= point:
                end_i = average_i - 1
            else:
                search_index = average_i
                start_i = average_i + 1

    return search_index


def quick3_sort_tuples(array: List[Tuple[Number, Number]], start: int = None, end: int = None,
                       index_tuple: int = None) -> List[Tuple[Number, Number]]:
    if start is None and end is None:
        start, end = 0, len(array) - 1
    if start < end:
        down_equal_index, up_equal_index = _partition(array, start, end, index_tuple)
        quick3_sort_tuples(array, start, down_equal_index - 1, index_tuple)
        quick3_sort_tuples(array, up_equal_index + 1, end, index_tuple)

    return array


def _partition(array: List[Tuple[Number, Number]], start: int, end: int, index_tuple: int) -> Tuple[int, int]:
    rand_index = random.randint(start, end)
    pivot = array[rand_index][index_tuple]
    _swap(array, rand_index, end)

    down_equal_index = start
    before_repeat_index = end - 1
    i = start
    while i <= before_repeat_index:
        if array[i][index_tuple] < pivot:
            _swap(array, i, down_equal_index)
            down_equal_index += 1
            i += 1
        elif array[i][index_tuple] == pivot:
            _swap(array, i, before_repeat_index)
            before_repeat_index -= 1
        else:
            i += 1

    up_equal_index = down_equal_index
    while before_repeat_index < end:
        before_repeat_index += 1
        _swap(array, before_repeat_index, up_equal_index)
        up_equal_index += 1

    return down_equal_index, up_equal_index - 1


def _swap(array: List[Tuple[Number, Number]], first_index: int, second_index: int):
    first = array[first_index]
    second = array[second_index]
    array[first_index] = second
    array[second_index] = first


if __name__ == '__main__':

    def pass_interface(array: List[Tuple[Number, Number]], points: List[Number]):
        sorted_by_start = deepcopy(quick3_sort_tuples(array, index_tuple=0))
        sorted_by_end = deepcopy(quick3_sort_tuples(array, index_tuple=1))
        count_pieces = len(array)
        counter = [0 for _ in range(len(points))]

        for i, point in enumerate(points):
            starts_less_equal_point = binary_search_tuples(sorted_by_start, point, 0, 'greater')
            finish_less_point = binary_search_tuples(sorted_by_end, point, 1, 'less')

            if starts_less_equal_point == -1:
                starts_less_equal_point = count_pieces - 1
                point_pieces = starts_less_equal_point - finish_less_point
            elif finish_less_point == -1:
                finish_less_point = 0
                point_pieces = starts_less_equal_point - finish_less_point
            else:
                point_pieces = starts_less_equal_point - finish_less_point - 1

            counter[i] = point_pieces

        return counter

    n, m = tuple(map(int, input().split()))
    array = [[0, 0] for _ in range(n)]
    for i in range(n):
        array[i] = tuple(map(int, input().split()))
    points = list(map(int, input().split()))
    print(' '.join(map(str, pass_interface(array, points))))

    # test1
    # array = [(0, 5)]
    # points = [1, 6, 11]
    # print(' '.join(map(str, pass_interface(array, points))))

    # test2
    # array = [(1, 5), (7, 10),(3,6), (5, 6)]
    # points = [0, 11, 6, 7, 5, 8]
    # print(' '.join(map(str, pass_interface(array, points))))

    # test3
    # random.seed(13)
    # index_tuple = 1
    # test = [(3, 6), (1, 3), (10, 2), (5, 9), (1, 1), (5, 9)]
    # Test(test, index_tuple)

