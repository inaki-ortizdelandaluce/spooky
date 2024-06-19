import unittest
import spooky.spice as spice
import numpy as np
import os
import tempfile
import math


class TestSpice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, '../data/spice/kernels/mk/spooky_ops.tm')
        cls.mk = spice.load_metakernel(path)

    @classmethod
    def tearDownClass(cls):
        # spice.unload_metakernel(cls.mk)
        pass

    def test_geo2enu_correctness(self):
        source = [[7.750, 46.017, 1.673]]  # Zermatt, Switzerland
        target = [[7.658, 45.976, 4.531]]  # Matterhorn
        expected_output = np.array([[-7.1348, -4.5563, 2.8524]])

        result = spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=4)

        source = [[-3.1572, 55.9398, 0.251]]  # Arthur's Seat, Edinburgh
        target = [[-5.0362, 56.6657, 0.931]]  # Glen Coe, Three Sisters Beinn Fhada
        expected_output = np.array([[-115.2090, 82.4018, -0.8902]])

        result = spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=3)

        source = [[-3.319995, 55.909723, 0.010]]  # HOGS, Heriot-Watt University, Edinburgh
        target = [[-5.0362, 56.6657, 0.931]]  # Glen Coe, Three Sisters Beinn Fhada
        expected_output = np.array([[-105.2305, 85.4909, -0.5178]])

        result = spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=3)

        source = [[7.750, 46.017, 1.673],     # Zermatt, Switzerland
                  [-3.1572, 55.9398, 0.251]]  # Arthur's Seat, Edinburgh
        target = [[7.658, 45.976, 4.531],     # Matterhorn
                  [-5.0362, 56.6657, 0.931]]  # Glen Coe, Three Sisters Beinn Fhada
        expected_output = np.array([[-7.1348, -4.5563, 2.8524],
                                    [-115.2090, 82.4018, -0.8902]])

        result = spice.geo2enu(source, target)
        np.testing.assert_almost_equal(result, expected_output, decimal=3)

    def test_geo2enu_shape_mismatch(self):
        source = [[7.750, 46.017, 1673], [7.750, 46.017, 1673]]
        target = [[7.658, 45.976, 4531]]

        with self.assertRaises(TypeError):
            spice.geo2enu(source, target)

    def test_geo2enu_invalid_shape(self):
        valid_source = [[7.750, 46.017, 1673]]  # Zermatt, Switzerland
        valid_target = [[7.658, 45.976, 4531]]  # Matterhorn

        invalid_source = [[7.750, 46.017]]  # missing altitude
        invalid_target = [[7.658, 45.976]]  # missing altitude

        with self.assertRaises(TypeError):
            spice.geo2enu(invalid_source, valid_target)

        with self.assertRaises(TypeError):
            spice.geo2enu(valid_source, invalid_target)

    def test_lla2enu_correctness(self):
        frame = 'HOGS'
        lla = [-5.0362, 56.6657, 0.931]  # Glen Coe, Three Sisters Beinn Fhada
        expected_enu = [-105.2305, 85.4909, -0.5178]

        result = spice.lla2enu(frame, lla)

        self.assertTrue(np.allclose(result, expected_enu, atol=1e-4))

    def test_write_spk09(self):
        # compute states for unequal time steps
        spice.load(['mar097.bsp'])
        et = spice.str2et("2018 Apr 03 08:35")
        time = et
        step = 60
        delta = 10.0
        steps = 800

        epochs = np.zeros(steps)
        states = np.zeros(shape=(steps, 6))
        for i in range(steps):
            pos, vel = spice.state("PHOBOS", time, "J2000", "MARS")
            states[i] = np.concatenate((pos, vel), axis=0)
            epochs[i] = time + 3600.0  # object follows phobos 1 hour later
            time = time + step + math.sin(0.5 * math.pi * i / 2.0) * delta
        spk_file = "spkw09_ex1.bsp"
        spice.write_spk09(spk_file, epochs, states, 403, "MARS", "J2000", 3)

        # load spk and validate interpolated state after 13 hours
        et = et + 46800.0
        spice.load([spk_file])
        pos, vel = spice.state("403", et, "J2000", "MARS")
        state = np.concatenate((pos, vel), axis=0)
        expected_output = np.array([-7327.26277, 2414.32655, 5207.10638, -0.94289, -1.89473, -0.39671])

        # remove spk
        os.remove(spk_file)

        np.testing.assert_almost_equal(state, expected_output, decimal=5)

    def test_llat2spk(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        llat_file = os.path.join(dir_path, '100kmSSOrbitLLAT.txt')

        spk_file = "spkw09_100kmSSOrbit.bsp"
        et0 = spice.str2et('2023-01-01T00:00:00')
        obj_id = -10000
        spice.llat2spk(obj_id, llat_file, spk_file, et0=et0)

        self.assertTrue(os.path.exists(spk_file))

        # load spk and validate initial state
        spice.load([spk_file])
        pos, vel = spice.state(str(obj_id), et0, 'ITRF93', 'EARTH')
        state = np.concatenate((pos, vel), axis=0)
        expected_output = np.concatenate((spice.geo2rec(75.77053312558824, 81.56912619027396, 0.1207842661159448),
                                          [0.0, 0.0, 0.0]), axis=0)

        os.remove(spk_file)

        np.testing.assert_almost_equal(state, expected_output, decimal=5)


if __name__ == '__main__':
    unittest.main()
