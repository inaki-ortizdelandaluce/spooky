import spooky.units.magnitude
from spooky.components.telescope import Telescope
from spooky.components.source import Source
from spooky.components.detector import Detector
from spooky.nodes.endpoint import QKDReceiver, QKDTransmitter


class Satellite(QKDReceiver, QKDTransmitter):
    def __init__(self, name, telescope: Telescope, source: Source = None, detector: Detector = None):
        self._name = name
        self._source = source
        self._detector = detector
        self._telescope = telescope
        self._position = np.empty((0, 3))
        self._velocity = np.empty((0, 3))
        # TODO add self._beacon, self._camera for beacon simulation

        if not self._detector and not self._source:
            raise ValueError("Satellite object must provide either a source or a detector")

    @property
    def source(self) -> Source:
        return self._source

    @property
    def telescope(self) -> Telescope:
        return self._telescope

    @property
    def detector(self) -> Detector:
        return self._detector

    def compute_total_background_count_rate(self, background_sources, qkd_transmitter, headings, elevations,
                                            smarts_configuration, count_map):
        pass

    def plot_background_count_rates(self, plotting_indices, x_axis):
        pass

    def set_wavelength(self, wavelength: float, wavelength_scale: spooky.units.magnitude.Magnitude):
        if not self._source:
            self._source.set_wavelength(wavelength, wavelength_scale)
        if not self._detector:
            self._detector.set_wavelength(wavelength, wavelength_scale)
        self._telescope.set_wavelength(wavelength, wavelength_scale)

    def set_position(self, position):
        position = np.asarray(position)

        if position.ndim == 2 and position.shape[1] == 3:
            self._position = position
        else:
            raise ValueError("Position must be a 2D array with shape (n,3)")

    def set_velocity(self, velocity):
        velocity = np.asarray(velocity)

        if velocity.ndim == 2 and velocity.shape[1] == 3:
            self._velocity = velocity
        else:
            raise ValueError("Velocity must be a 2D array with shape (n,3)")

    def set_state(self, position, velocity):
        self.set_position(position)
        self.set_velocity(velocity)


if __name__ == "__main__":
    from spooky.components.telescope import *
    from spooky.components.source import *
    from spooky.components.detector import *
    from spooky.nodes.satellite import *
    wl = 780
    transmitter_source = Source(wavelength=wl, repetition_rate=1e8, mean_photon_number_signal=0.1)
    transmitter_telescope = Telescope(diameter=0.1, wavelength=wl)
    satellite = Satellite(name='-141731', telescope=transmitter_telescope, source=transmitter_source)
