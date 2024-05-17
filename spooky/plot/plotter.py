import numpy as np

from spooky.components.detector import Detector, load_preset_name
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def plot_detector(detector: Detector):
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Detection efficiency')
    ax.axvline(detector.wavelength, color='g', linestyle=(5, (10, 3)), linewidth=0.5)
    ax.axhline(detector.detection_efficiency, color='g', linestyle=(5, (10, 3)), linewidth=0.5)
    ax.set_ylim([0, 1])
    ax.set_xlim([min(detector.wavelength_range), max(detector.wavelength_range)])
    ax.plot(detector.wavelength_range, detector.efficiencies, label='Detection Efficiency', linewidth=0.5)
    ax.text(detector.wavelength,
            detector.detection_efficiency,
            f'Detection Efficiency = {100 * detector.detection_efficiency:.1f}% at {detector.wavelength}nm',
            verticalalignment='bottom',
            horizontalalignment='center',
            fontname=plt.rcParams['font.family'],
            fontsize=10)
    ax.set_yticks(np.linspace(0, 1, 3))
    ax.yaxis.set_ticks_position('both')

    ax.xaxis.set_ticks_position('both')
    ax.tick_params(axis='both', direction='in', which="both")

    plt.show()


if __name__ == "__main__":
    wavelength = 780
    time_gate_width = 1e-9
    spectral_filter_width = 10
    repetition_rate = 1e8  # from transmitter
    preset = load_preset_name("PerkinElmer")

    d = Detector(wavelength=wavelength,
                 repetition_rate=repetition_rate,
                 time_gate_width=time_gate_width,
                 spectral_filter=spectral_filter_width,
                 preset=preset)
    plot_detector(d)
