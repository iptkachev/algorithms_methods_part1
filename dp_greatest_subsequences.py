from typing import List, Tuple


def gms(array: List[int]) -> int:
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


def gns(array: List[int]) -> Tuple[int, List[int]]:
    """
    Длина и индексы наибольшей невозрастающей подпоследовательности
    :param array: List[int]
    :return: int
    """
    array_length_subs = [0 for _ in range(len(array))]
    for i in range(len(array)):
        array_length_subs[i] = 1
        for j in range(i):
            if array[i] <= array[j] and array_length_subs[j] + 1 > array_length_subs[i]:
                array_length_subs[i] = array_length_subs[j] + 1

    idx_max_length = 0
    for i in range(1, len(array_length_subs)):
        if array_length_subs[idx_max_length] < array_length_subs[i]:
            idx_max_length = i

    max_length_subseq = array_length_subs[idx_max_length]
    indexes_max_subseq = [0 for _ in range(max_length_subseq)]
    indexes_max_subseq[-1] = idx_max_length + 1

    j = idx_max_length - 1
    suffix_max_length_subseq = max_length_subseq - 1
    while j >= 0:
        if suffix_max_length_subseq >= array_length_subs[j]:
            indexes_max_subseq[suffix_max_length_subseq - 1] = j + 1
            suffix_max_length_subseq -= 1
        j -= 1
    return max_length_subseq, indexes_max_subseq


if __name__ == '__main__':
    # test1 = [3, 6, 7, 12]
    # assert gms(test1) == 3
    #
    # test2 = [5, 3, 4, 4, 2]
    # assert (4, [1, 3, 4, 5]) == gns(test2)

    # def pass_interface_gms():
    #     n = input()
    #     array = list(map(int, input().split()))
    #     print(gms(array))
    #
    def pass_interface_gns():
        n = input()
        array = list(map(int, input().split()))
        result = gns(array)
        print(result[0])
        for obj in result[1]:
            print(obj, end=' ')

    pass_interface_gns()