from numbers import Number
from typing import List
from divide_and_conquer.insertion_sort import insertion_sort


def count_sort(array: List[Number]) -> List[Number]:
    counter = {elem: 0 for elem in insertion_sort(list(set(array)))}
    for elem in array:
        counter[elem] += 1

    keys = list(counter.keys())
    for i in range(1, len(keys)):
        counter[keys[i]] += counter[keys[i - 1]]

    sorted_array = [0 for _ in range(len(array))]
    for i in range(len(array) - 1, -1, -1):
        elem_array = array[i]
        sorted_array[counter[elem_array] - 1] = elem_array
        counter[elem_array] -= 1

    return sorted_array


if __name__ == '__main__':
    # test1 = [10, 4, 2, 14, 6, 2, 1, 4, 0]
    # print(count_sort(test1))
    # test2 = [2, 3, 9, 2, 9]
    # print(count_sort(test2))

    def pass_interface():
        n = input()
        array = list(map(int, input().split()))
        sorted_array = count_sort(array)
        for elem in sorted_array:
            print(elem, end=' ')

    pass_interface()