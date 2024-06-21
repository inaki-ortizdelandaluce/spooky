from spooky.components.detector import Detector, SpectralFilter, load_preset_name
from spooky.components.telescope import Telescope
from spooky.nodes.groundstation import GroundStation
from spooky.units.magnitude import Magnitude
from spooky.utils.geometry import earth_los_distance, move_along_earth_surface
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

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


def plot_groundstation_los(groundstation: GroundStation, altitude: float):
    """
    Plots satellite visibility from ground station in a plate carree map projection.
    Params:
        gs: spooky.nodes.groundstation.GroundStation
            Ground station object.
        altitude: float
            Satellite's altitude in kilometers.
    """
    delta_lon = 10
    delta_lat = 5

    # create a new plot with a specified projection
    _, ax = plt.subplots(subplot_kw={'projection': ccrs.Mercator()})
    ax.set_extent([groundstation.longitude - delta_lon, groundstation.longitude + delta_lon,
                   groundstation.latitude - delta_lat, groundstation.latitude + delta_lat],
                  crs=ccrs.PlateCarree())

    # add geographic features
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.LAND)

    # plot the ground station
    ax.plot(groundstation.longitude, groundstation.latitude, marker='+', markersize=10, color='b', linestyle='None',
            alpha=0.7, transform=ccrs.Geodetic(), label=groundstation.name)

    # plot the ground station's los distance and move along surface
    distance = earth_los_distance(altitude, groundstation.elevation_limit)

    los_lon = []
    los_lat = []
    for heading in range(0, 365, 5):
        lon, lat, _ = move_along_earth_surface(groundstation.longitude,
                                               groundstation.latitude,
                                               groundstation.altitude / 1000,
                                               distance,
                                               heading)
        los_lon.append(lon)
        los_lat.append(lat)

    ax.plot(los_lon, los_lat, 'g--', markersize=2, alpha=0.7, transform=ccrs.Geodetic())

    # add gridlines and labels
    ax.gridlines(draw_labels=True)

    # add a title and legend
    # plt.title(f'{gs.name} Line Of Sight visibility')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    wavelength = 780
    time_gate_width = 1e-9
    spectral_filter_width = 10
    repetition_rate = 1e8  # from transmitter
    preset = load_preset_name("PerkinElmer")

    detector = Detector(wavelength=wavelength,
                        repetition_rate=repetition_rate,
                        time_gate_width=time_gate_width,
                        spectral_filter=spectral_filter_width,
                        preset=preset)
    # plot_detector(detector)

    telescope = Telescope(diameter=1, wavelength=780, wavelength_scale=Magnitude.nano)
    ground_station = GroundStation(name='HOGS', lat=55.909723, lon=-3.319995, alt=10,
                                   telescope=telescope, detector=detector, elevation_limit=30)
    # plot_groundstation_los(ground_station, 100)
