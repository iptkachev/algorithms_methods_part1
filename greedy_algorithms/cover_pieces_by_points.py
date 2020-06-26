from typing import Set


def cover_pieces_by_points(pieces: list) -> Set[int]:
    pieces = sorted(pieces, key=lambda tupl: tupl[1])
    cover_point_set = set()
    while pieces:
        cover_point = pieces[0][1]
        while pieces[0][1] >= cover_point >= pieces[0][0]:
            pieces.pop(0)
            if not pieces:
                break
        cover_point_set.add(cover_point)

    return cover_point_set


if __name__ =='__main__':
    input_pieces = []
    for i in range(int(input())):
        pair = tuple(map(int, input().split()))
        input_pieces.append(pair)

    decision = cover_pieces_by_points(input_pieces)
    print(len(decision))
    for point in decision:
        print(point, end=' ')
