from typing import List
from numbers import Number


def insertion_sort(array: List[Number]) -> List[Number]:
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j]:
                i_elem = array[i]
                j_elem = array[j]
                array[j] = i_elem
                array[i] = j_elem

    return array
