def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    # a, b = 14159572, 63967072
    print(gcd(a, b))


if __name__ == "__main__":
    main()
