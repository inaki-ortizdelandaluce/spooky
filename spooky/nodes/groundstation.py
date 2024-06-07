import spooky.units.magnitude
from spooky.nodes.endpoint import QKDReceiver, QKDTransmitter
from spooky.components.source import Source
from spooky.components.detector import Detector
from spooky.components.telescope import Telescope


class GroundStation(QKDReceiver, QKDTransmitter):
    def __init__(self, name: str,
                 lat: float,
                 lon: float,
                 alt: float,
                 telescope: Telescope,
                 source: Source = None,
                 detector: Detector = None,
                 elevation_limit: float = 30):
        self._name = name
        self._source = source
        self._detector = detector
        self._telescope = telescope
        self._lla = [lat, lon, alt]
        self._elevation_limit = elevation_limit  # degrees
        # TODO add self._beacon, self._camera for beacon simulation
        # TODO add background count rate, atmosphere and sky brightness support, see HOGS example

        if not self._detector and not self._source:
            raise ValueError("GroundStation object must provide either a source or a detector")

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


