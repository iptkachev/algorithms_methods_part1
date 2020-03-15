import random
import time


def binary_search(array: list, required_numb: int, array_sorted=False) -> int:
    if not array_sorted:
        array.sort()
    start_i, end_i = 0, len(array) - 1
    while start_i <= end_i:
        average_i = (start_i + end_i) // 2
        if array[average_i] == required_numb:
            return average_i + 1
        elif array[average_i] > required_numb:
            end_i = average_i - 1
        else:
            start_i = average_i + 1

    return -1


def simple_search(array: list, required_numb: int) -> int:
    for i, elem in enumerate(array):
        if elem == required_numb:
            return i + 1
    return -1


if __name__ == '__main__':
    # pass interface
    sorted_array = sorted(list(map(int, input().split()))[1:])
    numbers_to_find = list(map(int, input().split()))
    n, numbers_to_find = numbers_to_find[0], numbers_to_find[1:]
    found_indexes = [0 for _ in range(n)]

    for i, element in enumerate(numbers_to_find):
        found_indexes[i] = binary_search(sorted_array, element, array_sorted=True)

    for element in found_indexes:
        print(element, end=' ')

    # # my tests
    # random.seed(10)
    # rand_array = list(range(10000))
    # random.shuffle(rand_array)
    # rand_required_numb = [random.randint(0, 10) for _ in range(10000)]
    #
    # t1 = time.time()
    # sorted_rand_array = sorted(rand_array)
    # found1 = [0 for _ in range(10000)]
    # for i in rand_required_numb:
    #     found1[i] = binary_search(sorted_rand_array, i, array_sorted=True)
    # print(time.time() - t1)
    #
    # t1 = time.time()
    # found2 = [0 for _ in range(10000)]
    # for i in rand_required_numb:
    #     found2[i] = simple_search(sorted_rand_array, i)
    # print(time.time() - t1)
    # print(found1 == found2)
