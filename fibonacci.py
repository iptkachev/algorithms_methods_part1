def fib(n: int) -> int:
    fib_array = [0, 1]
    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])
    return fib_array[-1]


def fib_last_digit(n: int) -> int:
    fib_array = [0, 1]
    for i in range(2, n + 1):
        fib_array.append((fib_array[i - 1] + fib_array[i - 2]) % 10)
    return fib_array[-1]


def fib_mod(n: int, m: int) -> int:
    fib_array = [0, 1]
    found_pizano = False
    for i in range(2, n + 1):
        fib_array.append((fib_array[i - 1] + fib_array[i - 2]) % m)
        if i >= 6 and fib_array[-3:] == fib_array[:3]:
            fib_array = fib_array[:-3]
            found_pizano = True
            break
    if found_pizano:
        return fib_array[n % len(fib_array)]
    else:
        return fib_array[-1]


def main():
    # n = int(input())
    # n = 696352
    # task 1
    # print(fib(n))
    # task 2
    # print(fib_last_digit(n))
    # task 3
    n, m = map(int, input().split())
    # n, m = 50, 6
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
