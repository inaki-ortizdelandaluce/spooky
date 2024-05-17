import numpy as np
from ..units.magnitude import Magnitude


class SpectralFilter:

    def __init__(self,
                 wavelengths: np.ndarray,
                 transmission: np.ndarray,
                 wavelength_scale=Magnitude.nano):
        self.wavelengths = wavelengths
        self.transmission = transmission
        self.wavelength_scale = wavelength_scale
        # convert wavelength to default scale (nanometers)
        self.wavelengths = Magnitude.convert(self.wavelength_scale, Magnitude.nano, self.wavelengths)

    @property
    def wavelengths(self):
        return self._wavelengths

    @wavelengths.setter
    def wavelengths(self, values):
        if values is None:
            raise ValueError("Wavelengths is empty.")

        if type(values) is not np.ndarray:
            raise TypeError("Wavelengths must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Wavelengths must be numeric.")

        if not np.all(values >= 0):
            raise TypeError("Wavelengths must be positive.")

        self._wavelengths = values

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, values):
        if values is None:
            raise ValueError("Transmission is empty.")

        if type(values) is not np.ndarray:
            raise TypeError("Transmission must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Transmission must be numeric.")

        if not np.all((values >= 0) & (values <= 1)):
            raise TypeError("Transmission must be between 0 and 1.")

        self._transmission = values

    @property
    def wavelength_scale(self):
        return self._wavelength_scale

    @wavelength_scale.setter
    def wavelength_scale(self, value):
        if not isinstance(value, Magnitude):
            raise TypeError("Wavelength scale is not an instance of Magnitude")
        self._wavelength_scale = value


class IdealBandPassFilter(SpectralFilter):

    def __init__(self,
                 centre_wavelength: float,
                 spectral_width: float,
                 steepness=1e3,
                 max_wavelength=1e4,
                 wavelength_scale=Magnitude.nano):

        change_width = 1 / steepness
        if spectral_width < change_width:
            change_width = spectral_width / 10
        half_width = spectral_width / 2
        half_change = change_width / 2

        wavelengths = np.array([0,
                                centre_wavelength - half_width - half_change,
                                centre_wavelength - half_width + half_change,
                                centre_wavelength + half_width - half_change,
                                centre_wavelength + half_width + half_change,
                                max_wavelength])
        transmission = np.array([0, 0, 1, 1, 0, 0])

        SpectralFilter.__init__(self,
                                wavelengths=wavelengths,
                                transmission=transmission,
                                wavelength_scale=wavelength_scale)
