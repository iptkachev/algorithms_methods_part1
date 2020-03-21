from typing import Iterable


class MergeSort:
    def __init__(self):
        self.inverses = 0
        self.sorted_array = None

    def _merge(self, first: Iterable, second: Iterable) -> list:
        len_first, len_second = len(first), len(second)
        counter_first, counter_second, counter_merged = 0, 0, 0
        merged_array = [0 for _ in range(len_first + len_second)]

        while counter_first < len_first and counter_second < len_second:
            if first[counter_first] <= second[counter_second]:
                merged_array[counter_merged] = first[counter_first]
                counter_first += 1
            elif first[counter_first] > second[counter_second]:
                merged_array[counter_merged] = second[counter_second]
                counter_second += 1
                self.inverses += (len_first - counter_first)
            else:
                break
            counter_merged += 1

        while counter_first < len_first:
            merged_array[counter_merged] = first[counter_first]
            counter_first += 1
            counter_merged += 1

        while counter_second < len_second:
            merged_array[counter_merged] = second[counter_second]
            counter_second += 1
            counter_merged += 1

        return merged_array

    def sort(self, array: Iterable):
        if len(array) == 1:
            return array

        middle = int(len(array) / 2)
        first, second = self.sort(array[:middle]), self.sort(array[middle:])

        return self._merge(first, second)


class Test:
    def __init__(self, array: Iterable, inverses: int):
        self.merge_unit = MergeSort()  # claim
        self.sorted_array = self.merge_unit.sort(array)  # when
        assert self.sorted_array == sorted(array)  # assert
        assert self.merge_unit.inverses == inverses  # assert


if __name__ == '__main__':
    Test([2, 3, 9, 2, 9], 2)
    Test([2], 0)
    Test([3, 9], 0)
    Test([9, 1], 1)
    Test([2, 3, 5, 7, 9], 0)
    Test([9, 7, 6, 3, 1], 10)
    Test([7, 6, 5, 4, 3, 2, 1], 21)
    Test([1, 2, 3, 5, 4], 1)
    Test([1, 3, 4, 5, 6, 2], 4)


    # _ = int(input())
    # array = list(map(int, input().split()))
    # merge_unit = MergeSort()
    # merge_unit.sort(array)
    # print(merge_unit.inverses)

