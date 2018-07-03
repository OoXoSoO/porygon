from unittest import TestCase
from sys import maxsize
from porygon.randompoint import generate_random_point


class VerifyPointsTest(TestCase):
    NUMBER_OF_POINTS = 20

    def __create_polygon_generator(self, file):
        for line in file:
            yield [tuple(map(int, point.split(','))) for point in line[:-1].split(' ')]

    def setUp(self):
        self.file = open('input.txt', 'r')
        self.polygons = self.__create_polygon_generator(self.file)

    def tearDown(self):
        self.file.close()

    def test_point(self):
        for i, polygon in enumerate(self.polygons):
            with self.subTest(line=i):
                for _ in range(self.NUMBER_OF_POINTS):
                    p = generate_random_point(polygon)
                    self.assertTrue(self.is_inside(p, polygon))

    def is_inside(self, point, polygon):
        rect = (point, (maxsize, point[1]))
        sides = [(polygon[i], polygon[(i+1) % len(polygon)]) for i in range(len(polygon))]
        cuts = 0
        for side in sides:
            if self.__is_intersecting(rect[0], rect[1], side[0], side[1]) and self.__is_intersecting(side[0], side[1], rect[0], rect[1]):
                cuts += 1

        return cuts % 2 == 1

    def __is_intersecting(self, r1p1, r1p2, r2p1, r2p2):
        a = r1p2[1] - r1p1[1]
        b = r1p1[0] - r1p2[0]
        c = (r1p2[0] * r1p1[1]) - (r1p1[0] * r1p2[1])

        result1 = a*r2p1[0] + b*r2p1[1] + c
        result2 = a*r2p2[0] + b*r2p2[1] + c

        return result1 * result2 < 0



