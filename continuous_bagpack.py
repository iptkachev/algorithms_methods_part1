
def greedy_fill_bagpack(parts: list, amount_bagpack: float):
    summary_value = 0.
    parts = sorted(parts, key=lambda x: x[0] / x[1])
    while amount_bagpack and parts:
        takein_part = parts.pop()
        if takein_part[-1] <= amount_bagpack:
            summary_value += takein_part[0]
            amount_bagpack -= takein_part[1]
        else:
            summary_value += (takein_part[0] / takein_part[1]) * amount_bagpack
            amount_bagpack -= amount_bagpack

    return summary_value


parts = []
count_parts, amount_bagpack = map(int, input().split())

for i in range(count_parts):
    pair = tuple(map(int, input().split()))
    parts.append(pair)

print(greedy_fill_bagpack(parts, amount_bagpack))
