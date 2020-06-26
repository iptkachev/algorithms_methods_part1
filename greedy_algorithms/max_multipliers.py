from typing import List


def max_k_multiplies(n: int) -> List[int]:
    """
    Найти максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых.
    :param n:
    :return:
    """
    multipliers_k = []
    i = 1
    while n != 0:
        if n - i > i or n - i == 0:
            n -= i
            multipliers_k.append(i)
        i += 1

    return multipliers_k


if __name__ == '__main__':
    mults = max_k_multiplies(int(input()))
    print(len(mults))
    for i in mults:
        print(i, end=' ')