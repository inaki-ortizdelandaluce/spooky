import numpy as np
from spooky.units.magnitude import Magnitude


class Source:

    def __init__(self,
                 wavelength: float,
                 wavelength_scale=Magnitude.nano,
                 repetition_rate=1e9,
                 efficiency=1.0,
                 mean_photon_number_signal=0.01,
                 mean_photon_number_vacuum=0,
                 state_preparation_error=0.01,
                 g2=0.01,
                 probability_signal=1,
                 **kwargs):
        self.wavelength_scale = wavelength_scale
        self.repetition_rate = repetition_rate
        self.efficiency = efficiency
        self.mean_photon_number_signal = mean_photon_number_signal
        self.mean_photon_number_vacuum = mean_photon_number_vacuum
        self.state_preparation_error = state_preparation_error
        self.g2 = g2
        self.probability_signal = probability_signal
        self.mean_photon_number_decoy = kwargs.get('mean_photon_number_decoy', None)
        self.probability_decoy = kwargs.get('probability_decoy', None)

        # convert wavelength to default scale (nanometers)
        self.wavelength = Magnitude.convert(self.wavelength_scale, Magnitude.nano, wavelength)

        # compute probability of emitting different states (for BB84 with decoy stated and COW)
        if self.probability_decoy is None:
            self.probability_vacuum = 1 - self.probability_signal
        elif self.probability_signal + self.probability_decoy > 1:
            raise ValueError(f"Sum of state probabilities exceed 1."
                             f"\nSignal={self.probability_signal}"
                             f"\nDecoy={self.probability_decoy}"
                             f"\nVacuum={1 - (self.probability_signal + self.probability_decoy)}")
        else:
            self.probability_vacuum = 1 - (self.probability_signal + self.probability_decoy)

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
    def repetition_rate(self):
        return self._repetition_rate

    @repetition_rate.setter
    def repetition_rate(self, value):
        self._repetition_rate = value

    @property
    def efficiency(self):
        return self._efficiency

    @efficiency.setter
    def efficiency(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Efficiency value must be numeric.")

        if value < 0 or value > 1:
            raise ValueError("Efficiency value must be between 0 and 1.")

        self._efficiency = value

    @property
    def mean_photon_number_signal(self):
        return self._mean_photon_number_signal

    @mean_photon_number_signal.setter
    def mean_photon_number_signal(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Mean Photon Number Signal value must be numeric.")

        self._mean_photon_number_signal = value

    @property
    def mean_photon_number_vacuum(self):
        return self._mean_photon_number_vacuum

    @mean_photon_number_vacuum.setter
    def mean_photon_number_vacuum(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Mean Photon Number Vacuum value must be numeric.")

        self._mean_photon_number_vacuum = value

    @property
    def mean_photon_number_decoy(self):
        return self._mean_photon_number_decoy

    @mean_photon_number_decoy.setter
    def mean_photon_number_decoy(self, value):
        if(value is not None) and not np.issubdtype(type(value), np.number):
            raise TypeError("Mean Photon Number Decoy value must be numeric.")
        self._mean_photon_number_decoy = value

    @property
    def state_preparation_error(self):
        return self._state_preparation_error

    @state_preparation_error.setter
    def state_preparation_error(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Mean Photon Number Vacuum value must be numeric.")

        self._state_preparation_error = value

    @property
    def g2(self):
        return self._g2

    @g2.setter
    def g2(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Auto-correlation of emitted photon at zero delay value must be numeric.")

        self._g2 = value

    @property
    def probability_signal(self):
        return self._probability_signal

    @probability_signal.setter
    def probability_signal(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Probability signal value must be numeric.")

        if value < 0 or value > 1:
            raise ValueError("Probability signal value must be between 0 and 1.")

        self._probability_signal = value

    @property
    def probability_vacuum(self):
        return self._probability_vacuum

    @probability_vacuum.setter
    def probability_vacuum(self, value):
        if not np.issubdtype(type(value), np.number):
            raise TypeError("Probability vacuum value must be numeric.")

        if value < 0 or value > 1:
            raise ValueError("Probability vacuum value must be between 0 and 1.")

        self._probability_vacuum = value

    @property
    def probability_decoy(self):
        return self._probability_decoy

    @probability_decoy.setter
    def probability_decoy(self, value):
        if (value is not None) and not np.issubdtype(type(value), np.number):
            raise TypeError("Probability decoy value must be numeric.")

        if (value is not None) and (value < 0 or value > 1):
            raise ValueError("Probability decoy value must be between 0 and 1.")

        self._probability_decoy = value

