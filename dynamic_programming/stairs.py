from typing import List


def max_value_stairs_recursion(steps: List[int], max_value=0) -> int:
    """
    Рекурсия
    Вернуть максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки), 
    каждый раз поднимаясь на одну или две ступеньки.
    :param max_value:
    :param steps: List[int] - ценность ступенек
    :return: int - максимальная ценность, пройдя по всем ступенькам
    """

    if len(steps) == 1:
        return steps[0]
    if len(steps) == 0:
        return max_value
    max_value = max(max_value_stairs_recursion(steps[:-2]), max_value_stairs_recursion(steps[:-1])) + steps[-1]
    return max_value


def max_value_stairs_iterative(steps: List[int]) -> int:
    """
    Итеративный
    Вернуть максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки),
    каждый раз поднимаясь на одну или две ступеньки.
    :param steps: List[int] - ценность ступенек
    :return: int - максимальная ценность, пройдя по всем ступенькам
    """
    cum_values = [0] + steps
    for i in range(len(cum_values)):
        if i in [0, 1]:
            continue
        cum_values[i] = cum_values[i] + max(cum_values[i - 1], cum_values[i - 2])
    return cum_values[-1]


if __name__ == '__main__':
    assert max_value_stairs_recursion([-1, -2, 4]) == 3
    assert max_value_stairs_recursion([2, -1]) == 1
    assert max_value_stairs_recursion([1, 2]) == 3
    assert max_value_stairs_recursion([-1, 2, 1]) == 3

    assert max_value_stairs_iterative([-1, 2, 1, 2, 1, 2]) == 8
    assert max_value_stairs_iterative([2, -1]) == 1

    def pass_interface():
        _ = input()
        steps = list(map(int, input().split()))
        print(max_value_stairs_iterative(steps))
