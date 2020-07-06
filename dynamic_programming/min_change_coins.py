from typing import List


def min_change_coins(n: int, coins: List[int]) -> int:
    change_by_min_k_coins = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0:
                change_by_min_k_coins[i] = min(change_by_min_k_coins[i], 1 + change_by_min_k_coins[i - coin])

    return change_by_min_k_coins[n]


if __name__ == '__main__':
    assert min_change_coins(9, [1, 2, 3]) == 3
    assert min_change_coins(27, [1, 2, 3]) == 9
