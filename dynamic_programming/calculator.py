from typing import Tuple, List


def calculate_least_calculator_operation(n: int) -> Tuple[int, List[int]]:
    min_multipliers = [i for i in range(n + 1)]
    min_multipliers_prev = [i for i in range(n + 1)]
    min_multipliers[1] = 0
    min_multipliers_prev[1] = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and 1 + min_multipliers[i // 3] < min_multipliers[i]:
            min_multipliers[i] = 1 + min_multipliers[i // 3]
            min_multipliers_prev[i] = i // 3
        if i % 2 == 0 and 1 + min_multipliers[i // 2] < min_multipliers[i]:
            min_multipliers[i] = 1 + min_multipliers[i // 2]
            min_multipliers_prev[i] = i // 2
        if 1 + min_multipliers[i - 1] < min_multipliers[i]:
            min_multipliers[i] = 1 + min_multipliers[i - 1]
            min_multipliers_prev[i] = i - 1
    intermediate_multipliers = [n]
    prev_k_multiplier = min_multipliers_prev[n]
    while prev_k_multiplier != 0:
        intermediate_multipliers.insert(0, prev_k_multiplier)
        prev_k_multiplier = min_multipliers_prev[prev_k_multiplier]
    return min_multipliers[n], intermediate_multipliers


if __name__ == '__main__':
    assert (14, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]) == \
           calculate_least_calculator_operation(96234)
    assert (3, [1, 2, 4, 5]) == calculate_least_calculator_operation(5)
    assert (0, [1]) == calculate_least_calculator_operation(1)
