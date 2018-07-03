from sys import maxsize


def is_inside(point, polygon):
    rect = (point, (maxsize, point[1]))
    sides = [(polygon[i], polygon[(i + 1) % len(polygon)]) for i in range(len(polygon))]
    cuts = 0
    for side in sides:
        if __intersects(rect[0], rect[1], side[0], side[1]) and __intersects(side[0], side[1], rect[0], rect[1]):
            cuts += 1

    return cuts % 2 == 1


def __intersects(r1p1, r1p2, r2p1, r2p2):
    a = r1p2[1] - r1p1[1]
    b = r1p1[0] - r1p2[0]
    c = (r1p2[0] * r1p1[1]) - (r1p1[0] * r1p2[1])

    result1 = a * r2p1[0] + b * r2p1[1] + c
    result2 = a * r2p2[0] + b * r2p2[1] + c

    return result1 * result2 < 0
