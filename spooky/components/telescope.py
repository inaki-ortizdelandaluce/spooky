from spooky.units.magnitude import Magnitude
import math
import numpy as np


class Telescope:

    def __init__(self,
                 diameter: float,
                 wavelength: float,
                 wavelength_scale=Magnitude.nano,
                 optical_efficiency=(1 - 0.3 ** 2),
                 far_field_divergence_coefficient=1,
                 pointing_jitter=1e-6,
                 f_number=12,
                 eyepiece_focal_length=0.076,
                 **kwargs):
        """
        Creates a Telescope object characterized by various optical system properties

        :param diameter: Diameter of the telescope in meters
        :param wavelength: wavelength of the telescope in nm, set by the satellite it is mounted to
        :param optical_efficiency: Optical efficiency from Cassegrain telescope obscuration
        (see https://doi.org/10.1117/12.2573489)
        :param far_field_divergence_coefficient: ratio between theoretical and actual far field divergence angle
        :param pointing_jitter: root-mean-square error in pointing in radians
        :param f_number: ratio of focal length and diameter
        :param eyepiece_focal_length: eyepiece focal length to compute magnification
        :param kwargs:
            'fov' - Field of view in radians describing spread of photons as they propagate
            'focal_length' - focal length in meters of the telescope collecting optics
        """
        self.diameter = diameter
        self.wavelength = wavelength
        self.wavelength_scale = wavelength_scale
        self.optical_efficiency = optical_efficiency
        self.far_field_divergence_coefficient = far_field_divergence_coefficient
        self.pointing_jitter = pointing_jitter
        self.f_number = f_number
        self.eyepiece_focal_length = eyepiece_focal_length
        self.fov = kwargs.get('fov', None)
        self.focal_length = kwargs.get('focal_length', None)

        # convert wavelength to default scale (nanometers)
        self.wavelength = Magnitude.convert(self.wavelength_scale, Magnitude.nano, wavelength)

        # compute the actual field of view given the far-field divergence coefficient
        # or the far-field divergence coefficient from the input parameters
        if self.fov is None:
            self.fov = self.get_actual_fov()
        else:
            self.far_field_divergence_coefficient = self.fov / self.get_theoretical_fov()
            if self.far_field_divergence_coefficient < 1:
                print('Warning: Requested FOV is narrower than diffraction limit. Revering to diffraction limit')
                self.far_field_divergence_coefficient = 1
                self.fov = self.get_theoretical_fov()

        # compute F-number from focal length and diameter
        # or compute focal length from input F-number and diameter
        if self.focal_length is not None:
            self.f_number = self.focal_length / self.diameter
        else:
            self.focal_length = self.f_number * self.diameter

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Diameter must be numeric.")
        self._diameter = value

    @property
    def wavelength(self):
        return self._wavelength

    @wavelength.setter
    def wavelength(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Wavelength must be numeric.")
        self._wavelength = value

    @property
    def wavelength_scale(self):
        return self._wavelength_scale

    @wavelength_scale.setter
    def wavelength_scale(self, value):
        if not isinstance(value, Magnitude):
            raise TypeError("Wavelength scale is not an instance of Magnitude")
        self._wavelength_scale = value

    @property
    def optical_efficiency(self):
        return self._optical_efficiency

    @optical_efficiency.setter
    def optical_efficiency(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Optical efficiency must be numeric.")
        if value < 0 or value > 1:
            raise ValueError("Optical efficiency value must be between 0 and 1.")

        self._optical_efficiency = value

    @property
    def far_field_divergence_coefficient(self):
        return self._far_field_divergence_coefficient

    @far_field_divergence_coefficient.setter
    def far_field_divergence_coefficient(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Far-field divergence coefficient must be numeric.")
        if value < 0 or value > 1:
            raise ValueError("Far-field divergence coefficient value must be between 0 and 1.")

        self._far_field_divergence_coefficient = value

    @property
    def pointing_jitter(self):
        return self._pointing_jitter

    @pointing_jitter.setter
    def pointing_jitter(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Pointing jitter must be numeric.")

        if not value > 0:
            raise ValueError("Pointing jitter must be positive.")

        self._pointing_jitter = value

    @property
    def f_number(self):
        return self._f_number

    @f_number.setter
    def f_number(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("F-number must be numeric.")
        self._f_number = value

    @property
    def eyepiece_focal_length(self):
        return self._eyepiece_focal_length

    @eyepiece_focal_length.setter
    def eyepiece_focal_length(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Eyepiece focal length must be numeric.")
        self._eyepiece_focal_length = value

    def get_collecting_area(self):
        return math.pi / 4 * self.diameter ** 2

    def get_theoretical_fov(self):
        # twice the diffraction half-angle
        return 2.44 * (self.wavelength * 1e-9) / self.diameter

    def get_actual_fov(self):
        # the theoretical field of view times the far-field divergence coefficient
        return self.get_theoretical_fov() * self.far_field_divergence_coefficient

    def get_magnification(self):
        return self.focal_length / self.eyepiece_focal_length
