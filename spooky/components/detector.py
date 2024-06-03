from spooky.units.magnitude import Magnitude
from spooky.utils.arrays import null_or_empty
from spooky.components.filter import SpectralFilter, IdealBandPassFilter
import json
import math
import numpy as np
import os.path


class DetectorPreset:

    def __init__(self,
                 name: str,
                 dark_count_rate: float,
                 dead_time: float,
                 jitter_histogram: np.ndarray,
                 histogram_bin_width: float,
                 wavelength_range: np.ndarray,
                 efficiencies: np.ndarray):
        self.name = name
        self.dark_count_rate = dark_count_rate  # counts/s
        self.dead_time = dead_time  # seconds
        self.jitter_histogram = jitter_histogram
        self.histogram_bin_width = histogram_bin_width
        self.wavelength_range = wavelength_range
        self.efficiencies = efficiencies

    @property
    def dark_count_rate(self):
        return self._dark_count_rate

    @dark_count_rate.setter
    def dark_count_rate(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Dark count rate must be numeric.")

        if not value >= 0:
            raise ValueError("Dark count rate must be greater or equals to zero.")

        self._dark_count_rate = value

    @property
    def dead_time(self):
        return self._dead_time

    @dead_time.setter
    def dead_time(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Dead time must be numeric.")

        if not value >= 0:
            raise ValueError("Dead time must be greater or equals to zero.")

        self._dead_time = value

    @property
    def jitter_histogram(self):
        return self._jitter_histogram

    @jitter_histogram.setter
    def jitter_histogram(self, values):
        if type(values) is not np.ndarray:
            raise TypeError("Jitter histogram must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Jitter histogram values must be numeric.")

        if not np.any(values >= 0):
            raise ValueError("Jitter histogram values must be positive.")

        self._jitter_histogram = values

    @property
    def histogram_bin_width(self):
        return self._histogram_bin_width

    @histogram_bin_width.setter
    def histogram_bin_width(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Histogram bin width must be numeric.")

        if not value > 0:
            raise ValueError("Histogram bin width must be positive.")

        self._histogram_bin_width = value

    @property
    def wavelength_range(self):
        return self._wavelength_range

    @wavelength_range.setter
    def wavelength_range(self, values):
        if type(values) is not np.ndarray:
            raise TypeError("Wavelength range must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Wavelength range must be numeric.")

        self._wavelength_range = values

    @property
    def efficiencies(self):
        return self._efficiencies

    @efficiencies.setter
    def efficiencies(self, values):
        if type(values) is not np.ndarray:
            raise TypeError("Efficiencies must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Efficiencies values must be numeric.")

        if np.any(values < 0) or np.any(values > 1):
            raise ValueError("Efficiencies values must be between 0 and 1.")

        self._efficiencies = values


class Detector:
    def __init__(self,
                 wavelength: float,
                 repetition_rate: float,
                 time_gate_width: float,
                 spectral_filter,
                 **kwargs):
        self.repetition_rate = repetition_rate
        self.time_gate_width = time_gate_width
        self.spectral_filter = spectral_filter
        self.wavelength_scale = kwargs.get("wavelength_scale", Magnitude.nano)
        # required for polarisation encoded QKD, default value modelled off Micius
        self.polarisation_error = kwargs.get("polarisation_error", math.degrees(math.asin(1 / 280)))
        self.preset = kwargs.get("preset", None)

        if self.preset is not None:
            self.dark_count_rate = self.preset.dark_count_rate
            self.dead_time = self.preset.dead_time
            self.jitter_histogram = self.preset.jitter_histogram
            self.histogram_bin_width = self.preset.histogram_bin_width
            self.wavelength_range = self.preset.wavelength_range
            self.efficiencies = self.preset.efficiencies
        else:
            self.dark_count_rate = kwargs.get("dark_count_rate", 0)  # counts/s
            self.dead_time = kwargs.get("dead_time", 0)  # seconds
            self.jitter_histogram = kwargs.get("jitter_histogram")  # counts/bin
            self.histogram_bin_width = kwargs.get("histogram_bin_width")  # seconds
            self.wavelength_range = kwargs.get("wavelength_range")
            self.efficiencies = kwargs.get("efficiencies")

        # convert wavelength to default scale (nanometers)
        self.wavelength = Magnitude.convert(self.wavelength_scale, Magnitude.nano, wavelength)

        # set spectral filter from spectral filter object or spectral width in nm
        if isinstance(spectral_filter, SpectralFilter):
            self.spectral_filter = spectral_filter
        elif np.issubdtype(type(spectral_filter), np.number):
            self.spectral_filter = IdealBandPassFilter(centre_wavelength=self.wavelength,
                                                       spectral_width=spectral_filter,
                                                       wavelength_scale=self.wavelength_scale)
        else:
            raise TypeError("Spectral filter can either be a SpectralFilter object or a filter width in nm")

        # set detection efficiency
        self.detection_efficiency = self.get_detection_efficiency(self.wavelength_range, self.efficiencies,
                                                                  self.wavelength)
        # set jitter CDF and PDF
        # self.cdf, self.pdf = self.get_jitter_density_functions(self)
        # set jitter QBER and loss
        # self.qber, self.loss = self.get_jitter_performance(self)

    @property
    def wavelength(self):
        return self._wavelength

    @wavelength.setter
    def wavelength(self, value):
        self._wavelength = value

    @property
    def repetition_rate(self):
        return self._repetition_rate

    @repetition_rate.setter
    def repetition_rate(self, value):
        self._repetition_rate = value

    @property
    def time_gate_width(self):
        return self._time_gate_width

    @time_gate_width.setter
    def time_gate_width(self, value):
        self._time_gate_width = value

    @property
    def spectral_filter(self):
        return self._spectral_filter

    @spectral_filter.setter
    def spectral_filter(self, value):
        self._spectral_filter = value

    @property
    def wavelength_scale(self):
        return self._wavelength_scale

    @wavelength_scale.setter
    def wavelength_scale(self, value):
        if not isinstance(value, Magnitude):
            raise TypeError("Wavelength scale is not an instance of Magnitude")
        self._wavelength_scale = value

    @property
    def polarisation_error(self):
        return self._polarisation_error

    @polarisation_error.setter
    def polarisation_error(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Polarisation error must be numeric.")

        if value < 0 or value >= 360:
            raise ValueError("Polarisation error must be between 0 and 360.")

        self._polarisation_error = value

    @property
    def preset(self):
        return self._preset

    @preset.setter
    def preset(self, value):
        if (value is not None) and (not isinstance(value, DetectorPreset)):
            raise TypeError("Preset is not instance of Detector Preset.")

        self._preset = value

    @property
    def dark_count_rate(self):
        return self._dark_count_rate

    @dark_count_rate.setter
    def dark_count_rate(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Dark count rate must be numeric.")

        if not value >= 0:
            raise ValueError("Dark count rate must be greater or equals to zero.")

        self._dark_count_rate = value

    @property
    def dead_time(self):
        return self._dead_time

    @dead_time.setter
    def dead_time(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Dead time must be numeric.")

        if not value >= 0:
            raise ValueError("Dead time must be greater or equals to zero.")

        self._dead_time = value

    @property
    def jitter_histogram(self):
        return self._jitter_histogram

    @jitter_histogram.setter
    def jitter_histogram(self, values):
        if values is None:
            raise ValueError("Jitter histogram is empty.")

        if type(values) is not np.ndarray:
            raise TypeError("Jitter histogram must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Jitter histogram values must be numeric.")

        if not np.any(values >= 0):
            raise ValueError("Jitter histogram values must be positive.")

        self._jitter_histogram = values

    @property
    def histogram_bin_width(self):
        return self._histogram_bin_width

    @histogram_bin_width.setter
    def histogram_bin_width(self, value):
        if value is None:
            raise ValueError("Histogram bin width is empty.")

        if not np.issubdtype(type(value), np.number):
            raise TypeError("Histogram bin width must be numeric.")

        if not value > 0:
            raise ValueError("Histogram bin width must be positive.")

        self._histogram_bin_width = value

    @property
    def wavelength_range(self):
        return self._wavelength_range

    @wavelength_range.setter
    def wavelength_range(self, values):
        if values is None:
            raise ValueError("Wavelength range is empty.")

        if type(values) is not np.ndarray:
            raise TypeError("Wavelength range must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Wavelength range must be numeric.")

        self._wavelength_range = values

    @property
    def efficiencies(self):
        return self._efficiencies

    @efficiencies.setter
    def efficiencies(self, values):
        if values is None:
            raise ValueError("Efficiencies is empty.")

        if type(values) is not np.ndarray:
            raise TypeError("Efficiencies must be a numpy array.")

        if not np.issubdtype(values.dtype, np.number):
            raise TypeError("Efficiencies values must be numeric.")

        if np.any(values < 0) or np.any(values > 1):
            raise ValueError("Efficiencies values must be between 0 and 1.")

        self._efficiencies = values

    @property
    def detection_efficiency(self):
        return self._detection_efficiency

    @detection_efficiency.setter
    def detection_efficiency(self, value):
        if not np.issubdtype(value.dtype, np.number):
            raise TypeError("Efficiency value must be numeric.")

        if value < 0 or value > 1:
            raise ValueError("Efficiency value must be between 0 and 1.")

        self._detection_efficiency = value

    @staticmethod
    def set_detection_efficiency(detector, **kwargs):
        if 'efficiency' in kwargs:
            detector.efficiency = kwargs['efficiency']
        elif 'wavelength' in kwargs:
            detector.efficiency = detector.get_detection_efficiency(detector.wavelength_range,
                                                                    detector.efficiencies,
                                                                    kwargs['wavelength'])
        else:
            raise TypeError("Either 'efficiency' or 'wavelength' arguments are expected")

    @staticmethod
    def get_detection_efficiency(wavelength_range: np.ndarray, efficiencies: np.ndarray, wavelength: float):
        if null_or_empty(wavelength_range):
            raise ValueError("Wavelength range is empty")
        if null_or_empty(efficiencies):
            raise ValueError("Efficiencies is empty")

        min_wavelength = min(wavelength_range)
        max_wavelength = max(wavelength_range)
        if not (wavelength >= min_wavelength) and (wavelength <= max_wavelength):
            raise ValueError(f"Wavelength must be in range {min_wavelength:.3f}:{max_wavelength:.3f}")
        else:
            from scipy.interpolate import CubicSpline
            cubic_spline = CubicSpline(wavelength_range, efficiencies, bc_type='natural')
            efficiency = cubic_spline(wavelength)
        return efficiency

    def get_jitter_density_functions(self):
        """
        Computes the probability density function and cumulative density function
        derived from the jitter histogram
        """
        total_counts = np.sum(self.jitter_histogram)
        n = len(self.jitter_histogram)

        cdf = np.zeros(n)
        pdf = np.zeros(n)

        pdf[0] = self.jitter_histogram[0] / total_counts
        for i in range(1, n):
            pdf[i] = self.jitter_histogram[i] / total_counts
            cdf[i] = np.sum(pdf[0:i])

        return cdf, pdf

    def get_jitter_performance(self):
        """
         Compute the QBER and loss due to jitter. Depending on the kind of source,
         the method to calculate the jitter and so the contribution it makes to the
         QBER is different.

         For weak coherent pulses we must assume that the repetition rate is equal
         to the incident photon rate where the average photon per pulse has been
         reduced due to loss.

         This is different to sources with continuous wave pumping where the only
         contribution to QBER from jitter can be from the photons that have arrived.

         Returns:
             tuple: A tuple with the jitter QBER and loss.
         """
        # convert time measures into index increments
        time_gate_width_idx = 2 * round(self.time_gate_width / (2 * self.histogram_bin_width))
        repetition_period_idx = round(1 / (self.repetition_rate * self.histogram_bin_width))

        # check rounding precision
        if time_gate_width_idx < 10:
            print('Warning: gate width is less than 10 histogram bins resulting in significant rounding errors')
        if repetition_period_idx < 10:
            print('Warning: repetition period is less than 10 histogram bins resulting in significant rounding errors')

        # compute mode point
        cdf, pdf = self.get_jitter_density_functions()
        mode_time_idx = np.argmax(pdf)

        n = len(self.jitter_histogram)
        half_idx = time_gate_width_idx // 2

        # compute loss
        loss = - cdf[max(mode_time_idx - half_idx, 0)] + cdf[min(mode_time_idx + half_idx, n-1)]

        # compute QBER by performing a discrete auto-correlation calculation
        # of the jitter PDF at delays equal to integer multiples of the photon arrival period
        qber = 0
        current_mode = mode_time_idx + repetition_period_idx
        while current_mode < n:
            qber += 0.5 * (cdf[min(current_mode + half_idx, n - 1)] - cdf[max(current_mode - half_idx, 0)])
            current_mode += repetition_period_idx

        # iterating over forward pulses (positive auto-correlation)
        current_mode = mode_time_idx - repetition_period_idx
        while current_mode >= 0:
            qber += 0.5 * (cdf[min(current_mode + half_idx, n - 1)] - cdf[max(current_mode - half_idx, 0)])
            current_mode -= repetition_period_idx

        # QBER cannot exceed 0.5
        return min(qber, 0.5), loss

    def plot(self):
        from ..plot.plotter import plot_detector
        plot_detector(self)


def load_preset_name(name):
    current_dir = os.path.dirname(__file__)
    file_name = name + '.json'
    file_path = os.path.join(current_dir, 'presets', file_name)
    return load_preset(file_path)


def load_preset(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            contents = json.load(file)
    else:
        raise FileNotFoundError("File " + file_path + " not found.")

    preset = DetectorPreset(name=contents["Name"],
                            dark_count_rate=contents["Dark_Count_Rate"],
                            dead_time=contents["Dead_Time"],
                            jitter_histogram=np.array(contents["Jitter_Histogram"]),
                            histogram_bin_width=contents["Histogram_Bin_Width"],
                            wavelength_range=np.array(contents["Wavelength_Range"]),
                            efficiencies=np.array(contents["Efficiencies"]))
    return preset
