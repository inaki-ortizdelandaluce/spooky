import numpy as np
from spooky.units.magnitude import Magnitude


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

    @staticmethod
    def compute_transmission(filters: list,
                             wavelengths: np.ndarray):
        """
        Compute transmission from a spectral filter list at the specified wavelengths.

        Args:
            filters (list): A list of spectral filters
            wavelengths (numpy.ndarray): A 1D array of wavelengths.

        Returns:
            numpy.ndarray: A 2D array of transmissions.
        """
        if not isinstance(filters, list) and not all(isinstance(item, SpectralFilter) for item in filters):
            raise TypeError("Filters must be a list of SpectralFilter objects")

        if not isinstance(wavelengths, np.ndarray) or wavelengths.ndim != 1:
            raise ValueError('Wavelengths must be formatted as a 1D numpy array')

        transmission = np.zeros((len(wavelengths), len(filters)))

        for i, f in enumerate(filters):
            if len(f.wavelengths) == 1 and np.array_equal(f.wavelengths, wavelengths):
                transmission[:, i] = f.transmission
            else:
                from scipy.interpolate import interp1d
                interp_func = interp1d(f.wavelengths,
                                       f.transmission,
                                       kind='linear',
                                       bounds_error=False,
                                       fill_value=0)
                transmission[:, i] = interp_func(wavelengths)

        return transmission


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
