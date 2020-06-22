from typing import List, Tuple
from numbers import Number
import random


def gms_n2(array: List[int]) -> int:
    """
    Длина наибольшей кратнонеубывающей подпоследовательности O(n**2)
    :param array: List[int]
    :return: int
    """
    array_length_subs = [0 for _ in range(len(array))]
    for i in range(len(array)):
        array_length_subs[i] = 1
        for j in range(i):
            if array[i] % array[j] == 0 and array_length_subs[j] + 1 > array_length_subs[i]:
                array_length_subs[i] = array_length_subs[j] + 1
    return max([0] + array_length_subs)


def gns_n2(array: List[int]) -> Tuple[int, List[int]]:
    """
    Длина и индексы наибольшей невозрастающей подпоследовательности O(n**2)
    :param array: List[int]
    :return: tuple(int, List[int])
    """
    array_length_subs = [0 for _ in range(len(array))]
    for i in range(len(array)):
        array_length_subs[i] = 1
        for j in range(i):
            if array[i] <= array[j]:
                array_length_subs[i] = max(array_length_subs[j] + 1, array_length_subs[i])

    idx_max_length = 0
    for i in range(1, len(array_length_subs)):
        if array_length_subs[idx_max_length] < array_length_subs[i]:
            idx_max_length = i

    max_length_subseq = array_length_subs[idx_max_length]
    indexes_max_subseq = [0 for _ in range(max_length_subseq)]
    indexes_max_subseq[-1] = idx_max_length + 1

    j = idx_max_length
    current_max_length_subseq = max_length_subseq
    while j >= 0:
        if current_max_length_subseq == array_length_subs[j]:
            indexes_max_subseq[current_max_length_subseq - 1] = j + 1
            current_max_length_subseq -= 1
        j -= 1
    return max_length_subseq, indexes_max_subseq


def gns_nlog(array: List[int]) -> Tuple[int, List[int]]:
    """
    Длина и индексы наибольшей невозрастающей подпоследовательности O(nlog(n))
    по алгоритму https://www.youtube.com/watch?v=6NwNzEK1JNY
    :param array: List[int]
    :return: tuple(int, List[int])
    """
    def binary_search(array: List[Number], key_elem: int, start_i: int = 0, end_i: int = len(array) - 1) -> int:
        average_i = (start_i + end_i) // 2
        while start_i < end_i:
            current = array[average_i]
            next = array[average_i + 1]
            if current >= key_elem > next:
                break
            elif key_elem <= current:
                start_i = average_i + 1
            elif key_elem > current:
                end_i = average_i - 1
            average_i = (start_i + end_i) // 2
        return average_i

    last_elem_subseqs = [float('-inf') for _ in range(len(array) + 1)]
    last_elem_subseqs[0] = float('inf')
    last_elem_subseqs_indexes = [-1 for _ in range(len(array) + 1)]
    last_elem_subseqs_prev = [-1 for _ in range(len(array) + 1)]

    for i in range(len(array)):
        j = binary_search(last_elem_subseqs, array[i]) + 1
        if last_elem_subseqs[j - 1] >= array[i] > last_elem_subseqs[j]:
            last_elem_subseqs[j] = array[i]
            last_elem_subseqs_indexes[j] = i
            last_elem_subseqs_prev[i] = last_elem_subseqs_indexes[j - 1]

    # find last element most subseq
    last_elem_most_subseq = 0
    for i, index in enumerate(last_elem_subseqs_indexes[::-1]):
        if index > -1:
            last_elem_most_subseq = index
            length_most_subseq = len(array) - i
            break

    # recovery most subseq
    prev_index_most_subseq = last_elem_most_subseq
    most_subseq_indexes = []
    while prev_index_most_subseq != -1:
        most_subseq_indexes.append(prev_index_most_subseq + 1)
        prev_index_most_subseq = last_elem_subseqs_prev[prev_index_most_subseq]

    return length_most_subseq, most_subseq_indexes[::-1]


if __name__ == '__main__':
    # test1 = [3, 6, 7, 12]
    # assert gms(test1) == 3
    #
    # test2 = [3, 2, 3, 4, 4, 2, 1, 5, 5, 2, 3, 3, 3]
    # assert (4, [1, 3, 4, 5]) == gns_n2(test2)
    # assert (5, [3]*5) == gns_nlog(test2)

    test2 = [5, 3, 4, 4, 2]
    # assert (4, [1, 3, 4, 5]) == gns_n2(test2)
    # assert (4, [1, 3, 4, 5]) == gns_nlog(test2)
    random.seed(10)
    test3 = [7, 6, 1, 6, 4, 1, 2, 4, 10, 1]
    test4 = [random.randint(0, 1) for _ in range(20)]
    test5 = [random.randint(0, 10) for _ in range(20)]  # [10, 10, 10, 7, 7, 6, 0, 0]
    test6 = [random.randint(0, 100) for _ in range(20)]
    test7 = [0]
    test8 = [0, 0]
    tests = [test5, test6, test7, test8, test2]
    for i, test in enumerate(tests):
        print('test', test)
        nlogn = gns_nlog(test)
        n2 = gns_n2(test)
        assert nlogn == n2


    # def pass_interface_gms():
    #     n = input()
    #     array = list(map(int, input().split()))
    #     print(gms(array))

    # def pass_interface_gns():
    #     n = input()
    #     array = list(map(int, input().split()))
    #     result = gns_nlog(array)
    #     print(result[0])
    #     for obj in result[1]:
    #         print(obj, end=' ')
