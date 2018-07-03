from unittest import TestCase
from porygon.utils import is_inside
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
                    self.assertTrue(is_inside(p, polygon))



