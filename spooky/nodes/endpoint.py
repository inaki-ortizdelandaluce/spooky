from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List

from spooky.components.telescope import Telescope
from spooky.components.source import Source
from spooky.components.detector import Detector


class OpticalNode(ABC):

    @property
    @abstractmethod
    def telescope(self) -> Telescope:
        pass


class QKDTransmitter(OpticalNode):
    @property
    @abstractmethod
    def source(self) -> Source:
        pass

    @abstractmethod
    def compute_total_background_count_rate(self,
                                            background_sources,
                                            qkd_receiver,
                                            headings,
                                            elevations,
                                            smarts_configuration,
                                            count_map):
        pass

    @abstractmethod
    def plot_background_count_rates(self, plotting_indices, x_axis):
        pass


@dataclass
class QKDReceiver(OpticalNode):

    background_rates: Dict[str, List[float]] = \
        field(default_factory=lambda: {'heading': [], 'elevation': [], 'count_rate': []})
    light_pollution_count_rates: List[float] = field(default_factory=lambda: [0.0])
    dark_count_rates: List[float] = field(default_factory=lambda: [0.0])
    reflection_count_rates: List[float] = field(default_factory=lambda: [0.0])
    directed_count_rates: List[float] = field(default_factory=lambda: [0.0])

    @property
    @abstractmethod
    def detector(self) -> Detector:
        pass

    @abstractmethod
    def compute_total_background_count_rate(self,
                                            background_sources,
                                            qkd_transmitter,
                                            headings,
                                            elevations,
                                            smarts_configuration,
                                            count_map):
        pass

    @abstractmethod
    def plot_background_count_rates(self, plotting_indices, x_axis):
        pass
