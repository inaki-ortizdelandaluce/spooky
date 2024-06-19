import unittest
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
        self.assertAlmostEqual(angle, expected_angle, places=4)


if __name__ == '__main__':
    unittest.main()
