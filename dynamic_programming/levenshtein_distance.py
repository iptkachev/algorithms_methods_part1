import numpy as np


def compute_levenshtein_distance(a: str, b: str) -> int:
    distance_table = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
    for j in range(len(b) + 1):
        distance_table[j][0] = j
    for i in range(len(a) + 1):
        distance_table[0][i] = i

    for j in range(1, len(b) + 1):
        for i in range(1, len(a) + 1):
            cur_diff = int(a[i - 1] != b[j - 1])
            prev_diag_value = distance_table[j - 1][i - 1] + cur_diff
            prev_up_value = distance_table[j - 1][i] + 1
            prev_left_value = distance_table[j][i - 1] + 1
            distance_table[j][i] = min(prev_diag_value, prev_up_value, prev_left_value)
    return distance_table[len(b)][len(a)]


if __name__ == '__main__':
    # tests
    assert compute_levenshtein_distance('bb', 'bab') == 1
    assert compute_levenshtein_distance('bab', 'bab') == 0
    assert compute_levenshtein_distance('bab', 'aab') == 1
    assert compute_levenshtein_distance('baab', 'aab') == 1
    assert compute_levenshtein_distance('bbb', 'aaa') == 3
    assert compute_levenshtein_distance('', 'aab') == 3
    assert compute_levenshtein_distance('', 'a') == 1
    assert compute_levenshtein_distance('', '') == 0
    assert compute_levenshtein_distance('111111', '22111111') == 2
    assert compute_levenshtein_distance('хлеб', 'пиво') == 4
    assert compute_levenshtein_distance('пив', 'пиво') == 1
    assert compute_levenshtein_distance('tport', 'potr') == 3

    # a = input()
    # b = input()
    # print(compute_levenshtein_distance(a, b))
