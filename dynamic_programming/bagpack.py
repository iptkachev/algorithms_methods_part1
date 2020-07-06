from typing import List


def knapsack_without_reps(amount_pack: int, weigths: List[int], values: List[int]) -> int:
    values_pack = [0 for _ in range(amount_pack + 1)]
    for w in range(1, amount_pack + 1):
        for i in range(1, len(weigths) + 1):
            if weigths[i - 1] <= w:
                values_pack[w] = max(values_pack[w], values_pack[w - weigths[i - 1]] + values[i - 1])

    return values_pack[amount_pack]


def knapsack_with_reps(amount_pack: int, weigths: List[int], values: List[int]) -> int:
    values_pack = [[0 for _ in range(len(weigths) + 1)] for _ in range(amount_pack + 1)]

    for w in range(amount_pack + 1):
        values_pack[w][0] = 0
    for i in range(len(weigths) + 1):
        values_pack[0][i] = 0

    for w in range(1, amount_pack + 1):
        for i in range(1, len(weigths) + 1):
            values_pack[w][i] = values_pack[w][i - 1]
            if weigths[i - 1] <= w:
                values_pack[w][i] = max(values_pack[w][i], values_pack[w - weigths[i - 1]][i - 1] + values[i - 1])

    return values_pack[amount_pack][len(weigths)]


if __name__ == '__main__':
    assert knapsack_without_reps(10, [6, 3, 4, 2], [30, 14, 16, 9]) == 48
    assert knapsack_without_reps(10, [1, 4, 8], [1, 4, 8]) == 10
    assert knapsack_with_reps(10, [1, 4, 8], [1, 4, 8]) == 9

    def pass_interface():
        W, n = map(int, input().split())
        weights = list(map(int, input().split()))
        print(knapsack_with_reps(W, weights, weights))


    pass_interface()
