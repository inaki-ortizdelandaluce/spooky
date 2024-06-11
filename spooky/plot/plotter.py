import numpy as np
from spooky.components.detector import Detector, SpectralFilter, load_preset_name
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('TkAgg')


def plot_detector(detector: Detector):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 5), layout="constrained")

    # plot detection efficiency
    ax1.set_xlabel('Wavelength (nm)')
    ax1.set_ylabel('Detection efficiency')
    ax1.axvline(detector.wavelength, color='g', linestyle=(5, (10, 3)), linewidth=0.5)
    ax1.axhline(detector.detection_efficiency, color='g', linestyle=(5, (10, 3)), linewidth=0.5)
    ax1.set_ylim([0, 1])
    ax1.set_xlim([min(detector.wavelength_range), max(detector.wavelength_range)])
    ax1.plot(detector.wavelength_range, detector.efficiencies, label='Detection Efficiency', linewidth=0.5)
    ax1.text(detector.wavelength,
             max(detector.efficiencies),
             f'Detection Efficiency = {100 * detector.detection_efficiency:.1f}% at {detector.wavelength}nm',
             verticalalignment='bottom',
             horizontalalignment='center',
             fontname=plt.rcParams['font.family'],
             fontsize=8,
             color='g')
    ax1.set_yticks(np.linspace(0, 1, 3))
    ax1.yaxis.set_ticks_position('both')

    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(axis='both', direction='in', which="both")

    # plot spectral filter transmission
    transmissions = SpectralFilter.compute_transmission([detector.spectral_filter],
                                                        np.array([detector.wavelength]))
    transmission = transmissions[0, 0]
    ax2.set_xlabel('Wavelength (nm)')
    ax2.set_ylabel('Transmission')
    ax2.axvline(detector.wavelength, color='g', linestyle=(5, (10, 3)), linewidth=0.5)
    ax2.axhline(transmission, color='g', linestyle=(5, (10, 3)), linewidth=0.5)
    ax2.set_ylim([0, 1])
    ax2.set_xlim([min(detector.wavelength_range), max(detector.wavelength_range)])
    ax2.plot(detector.spectral_filter.wavelengths, detector.spectral_filter.transmission, linewidth=0.5)
    ax2.text(detector.wavelength,
             transmission,
             'Transmission = {:.1f}% at {}nm'.format(100 * transmission, detector.wavelength),
             verticalalignment='bottom',
             horizontalalignment='center',
             fontname=plt.rcParams['font.family'],
             fontsize=8,
             color='g')

    ax2.set_yticks(np.linspace(0, 1, 3))
    ax2.yaxis.set_ticks_position('both')

    ax2.xaxis.set_ticks_position('both')
    ax2.tick_params(axis='both', direction='in', which="both")

    # plot jitter histogram
    max_index, max_value = np.argmax(detector.jitter_histogram), np.max(detector.jitter_histogram)
    jitter_times = (np.arange(0, len(detector.jitter_histogram)) - max_index) * detector.histogram_bin_width

    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('PDF')
    ax3.axvline(-detector.time_gate_width / 2, color='b', linestyle=(5, (10, 3)), linewidth=0.5)
    ax3.axvline(detector.time_gate_width / 2, color='b', linestyle=(5, (10, 3)), linewidth=0.5)
    ax3.text(-detector.time_gate_width,
             max_value / 1.5,
             f'Time Gate Width = {detector.time_gate_width:.2g}s',
             verticalalignment='top',
             horizontalalignment='left',
             fontname=plt.rcParams['font.family'],
             fontsize=8,
             color='b')

    period = 1 / detector.repetition_rate
    ax3.set_ylim([0, max_value])
    ax3.set_xlim([-period, 2 * period])
    ax3.axvline(0, color='r', linestyle=(5, (10, 3)), linewidth=0.5)
    ax3.axvline(period, color='r', linestyle=(5, (10, 3)), linewidth=0.5)

    error_rate, _ = detector.get_jitter_performance()
    ax3.text(period,
             max_value / 2,
             f'Repetition Rate = {detector.repetition_rate:.2g}Hz'
             f'\nSignal Period = {period:.2g}s'
             f'\nQBER jitter={100 * error_rate:.3g}%',
             verticalalignment='top',
             horizontalalignment='left',
             fontname=plt.rcParams['font.family'],
             fontsize=8,
             color='r')

    ax3.plot(jitter_times, detector.jitter_histogram, linewidth=0.5)

    ax3.yaxis.set_ticks_position('both')
    ax3.xaxis.set_ticks_position('both')
    ax3.tick_params(axis='both', direction='in', which="both")

    if detector.preset is not None:
        plt.suptitle(f'{detector.preset.name} Detector Summary', fontsize=10)
    else:
        plt.suptitle('Detector Summary', fontsize=10)

    plt.show()


def plot_groundstation_los(altitude: float):
    pass


if __name__ == "__main__":
    """
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
    """

    import cartopy.crs as ccrs
    import cartopy.feature as cfeature

    # Define the latitude and longitude points
    lat = [34.05, 36.16, 40.71, 47.61]
    lon = [-118.24, -115.15, -74.00, -122.33]

    # Create a new plot with a specified projection
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent([-130, -65, 25, 50], crs=ccrs.PlateCarree())  # Set the extent (lon_min, lon_max, lat_min, lat_max)

    # Add geographic features
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)

    # Plot the data
    ax.plot(lon, lat, '-o', transform=ccrs.PlateCarree(), label='Path')

    # Add gridlines and labels
    ax.gridlines(draw_labels=True)

    # Add a title and legend
    plt.title('Geoplot Example')
    plt.legend()

    # Show the plot
    plt.show()
