import unittest
import numpy as np
from spooky.utils.geometry import *


class TestGeometry(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_earth_los_angle(self):
        angle = earth_los_angle(100, 15)
        expected_angle = 3.0107
        self.assertAlmostEqual(angle, expected_angle, places=3)

    def test_earth_los_distance(self):
        distance = earth_los_distance(100, 15)
        expected_distance = 334.774
        self.assertAlmostEqual(distance, expected_distance, places=2)

    def test_movel_along_earth(self):
        distance = 334.774
        lon, lat, alt = move_along_earth_surface(-3.319995, 55.909723, 0, distance, 0)
        coordinates = np.array((lon, lat, alt))
        expected_coordinates = np.array((-3.319995, 58.915760, 0))
        np.testing.assert_almost_equal(coordinates, expected_coordinates, decimal=3)


if __name__ == '__main__':
    unittest.main()
