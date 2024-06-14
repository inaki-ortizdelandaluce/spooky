import unittest
from spooky.utils.spice import Spice
import numpy as np
import os


class TestSpice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '../data/spice/kernels/mk/spooky_ops.tm')
        cls.mk = Spice.load_metakernel(path)

    @classmethod
    def tearDownClass(cls):
        # Unload the SPICE metakernel
        # Spice.unload_metakernel(cls.mk)
        pass

    def test_geo2enu_correctness(self):
        source = [[7.750, 46.017, 1.673]]  # Zermatt, Switzerland
        target = [[7.658, 45.976, 4.531]]  # Matterhorn
        expected_output = np.array([[-7.1348, -4.5563, 2.8524]])

        result = Spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=4)

        source = [[-3.1572, 55.9398, 0.251]]  # Arthur's Seat, Edinburgh
        target = [[-5.0362, 56.6657, 0.931]]  # Glen Coe, Three Sisters Beinn Fhada
        expected_output = np.array([[-115.2090, 82.4018, -0.8902]])

        result = Spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=3)

        source = [[-3.319995, 55.909723, 0.010]]  # HOGS, Heriot-Watt University, Edinburgh
        target = [[-5.0362, 56.6657, 0.931]]  # Glen Coe, Three Sisters Beinn Fhada
        expected_output = np.array([[-105.2305, 85.4909, -0.5178]])

        result = Spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=3)

        source = [[7.750, 46.017, 1.673],     # Zermatt, Switzerland
                  [-3.1572, 55.9398, 0.251]]  # Arthur's Seat, Edinburgh
        target = [[7.658, 45.976, 4.531],     # Matterhorn
                  [-5.0362, 56.6657, 0.931]]  # Glen Coe, Three Sisters Beinn Fhada
        expected_output = np.array([[-7.1348, -4.5563, 2.8524],
                                    [-115.2090, 82.4018, -0.8902]])

        result = Spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=3)

    def test_geo2enu_shape_mismatch(self):
        source = [[7.750, 46.017, 1673], [7.750, 46.017, 1673]]
        target = [[7.658, 45.976, 4531]]

        with self.assertRaises(TypeError):
            Spice.geo2enu(source, target)

    def test_geo2enu_invalid_shape(self):
        valid_source = [[7.750, 46.017, 1673]]  # Zermatt, Switzerland
        valid_target = [[7.658, 45.976, 4531]]  # Matterhorn

        invalid_source = [[7.750, 46.017]]  # missing altitude
        invalid_target = [[7.658, 45.976]]  # missing altitude

        with self.assertRaises(TypeError):
            Spice.geo2enu(invalid_source, valid_target)

        with self.assertRaises(TypeError):
            Spice.geo2enu(valid_source, invalid_target)


if __name__ == '__main__':
    unittest.main()
