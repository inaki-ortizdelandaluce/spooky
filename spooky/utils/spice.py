import spiceypy
import spiceypy.utils.support_types as stypes
import numpy as np
import re
import os.path as path
import tempfile


class Spice:

    def __init__(self):
        pass

    @staticmethod
    def version():
        return spiceypy.tkvrsn('TOOLKIT')

    @staticmethod
    def load(kernels):
        spiceypy.furnsh(kernels)

    @staticmethod
    def load_metakernel(kernel):

        with open(kernel, 'r') as f:
            content = f.read()

            # read kernel path values
            regexp = r'(PATH_VALUES\s+=\s+\(\s+\')(.*?)(\'\s+\))'
            result = re.search(regexp, content)
            path_values = result.group(2)

            if path_values == '..':
                # copy kernel to temporary file with updated path value
                path_values_new = path.abspath(path.join(kernel, '../..'))
                content_new = re.sub(regexp, r'\1' + path_values_new + r'\3', content, flags=re.M)
                kernel_new = tempfile.NamedTemporaryFile(mode='w', delete=False)
                with kernel_new as mk:
                    mk.write(content_new)
                    print('Temporary metakernel {} created'.format(mk.name))
                Spice.load(kernel_new.name)
            else:
                Spice.load(kernel)

    @staticmethod
    def clear():
        spiceypy.kclear()

    @staticmethod
    def et2utc(et):
        return spiceypy.et2utc(et, 'ISOC', 0)

    @staticmethod
    def utc2et(utc):
        return spiceypy.utc2et(utc)

    @staticmethod
    def str2et(s):
        return spiceypy.str2et(s)

    @staticmethod
    def body_radius(body):
        """Returns body radius in kilometers
        Params:
            body: the body name
        Returns:
            The body radius in kilometers
        """
        dim, radii = spiceypy.bodvrd(body, 'RADII', 3)
        return np.mean(radii)

    @staticmethod
    def position(target, et, frame, observer):
        """Finds the position of the target body relative to the observing body for the times
            specified.
        Params:
            target: name of the target body
            et: ephemeris times for the positions to be computed
            frame: reference frame relative to which the position vector should be expressed
            observer: name of the observing body
        Returns:
            Array of position vectors of the target body relative to an observing body.
        """
        pos, lt = spiceypy.spkpos(target, et, frame, 'NONE', observer)
        return pos

    @staticmethod
    def state(target, et, frame, observer):
        """Finds the state (position and velocity) of the target body relative to the observing body for the times
            specified.
        Params:
            target: name of the target body
            et: ephemeris times for the positions to be computed
            frame: reference frame relative to which the position vector should be expressed
            observer: name of the observing body
        Returns:
            Tuple of position and velocity vectors of the target body relative to an observing body.
        """
        state, lt = spiceypy.spkezr(target, et, frame, 'NONE', observer)

        if isinstance(state, list):
            state = np.asarray(state)
            return state[:, 0:3], state[:, 3:6]
        else:
            return state[0:3], state[3:6]

    def closest_approach(self, target, observer, utc_start, utc_end, multiple, step):
        """Finds closest approaches of the target to the observer during the time period specified.
        Params:
            target: name of the target body
            observer: name of the observing body
            utc_start: start time of the applicable time period in UTC format, e.g. 2021-08-09T14:00:00
            utc_end: end time of the applicable time period in UTC format, e.g. 2021-08-11T14:00:00
            multiple: if true computes all closest distances at a local minima for the applicable time period,
                if false computes the closest approach at the absolute minimum.
            step: step size for this search in seconds. The step must be shorter than the shortest interval over which
                the target-observer distance is increasing or decreasing.
        Returns:
            Array of ephemeris times for the closest approaches matching the search criteria, None if no closest
            approach is found.
        """
        et_start = self.utc2et(utc_start)
        et_end = self.utc2et(utc_end)

        confine = stypes.SPICEDOUBLE_CELL(2)
        spiceypy.wninsd(et_start, et_end, confine)

        ca_win = spiceypy.gfdist(target, 'NONE', observer, 'LOCMIN' if multiple else 'ABSMIN', 0.0, 0.0, step, 1000,
                              confine)
        win_size = spiceypy.wncard(ca_win)

        if win_size == 0:
            return None
        else:
            return [spiceypy.wnfetd(ca_win, i)[0] for i in range(win_size)]


if __name__ == '__main__':
    # start = '2024-05-21 15:00:00'
    # end = '2024-05-21 20:00:00'
    start = '2024-05-23 15:00:00'
    end = '2024-05-23 20:00:00'
    # start = '2020-05-01 11:36:00'
    # end = '2020-05-02 13:36:00'

    sp = Spice()
    sp.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')

    start_time = spiceypy.str2et(start)
    end_time = spiceypy.str2et(end)
    target = '-125544'  # ISS
    # target = '-100000'  # MATLAB example
    # frame  = 'DSA2_TOPO'
    # frame  = 'GS0002_TOPO'
    # frame = 'GS0001_TOPO'
    frame = 'DSA2_TOPO'
    abcorr = 'CN+S'
    # obsrvr = 'DSA2' # -399002
    # obsrvr = 'GS0001'  # -399001
    # obsrvr = 'GS0002'  # -399003
    obsrvr = 'DSA2'
    crdsys = 'LATITUDINAL'
    coord  = 'LATITUDE'
    relate = '>'
    # refval = 10. * spiceypy.rpd()
    refval = 0. * spiceypy.rpd()
    adjust = 0
    step = 60
    nintvls = 10000

    cnfine = spiceypy.stypes.SPICEDOUBLE_CELL(2)
    spiceypy.wninsd(start_time, end_time, cnfine)
    result = spiceypy.stypes.SPICEDOUBLE_CELL(10000)

    spiceypy.gfposc(target, frame, abcorr, obsrvr, crdsys, coord, relate, refval, adjust, step, nintvls, cnfine, result)
    count = spiceypy.wncard(result)
    print(f"{count} window(s) found")
    for i in range(count):
        window_start, window_end = spiceypy.wnfetd(result, i)
        print(f"Window {i+1}:{sp.et2utc(window_start)} - {sp.et2utc(window_end)}")

    import spiceypy
    from spooky.utils.spice import Spice
    import numpy as np

    sp = Spice()
    sp.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')
    _, radii = spiceypy.bodvrd('EARTH', 'RADII', 3)
    re = radii[0]
    rp = radii[2]
    f = (re - rp) / re

    lon = spiceypy.convrt(118.0, 'DEGREES', 'RADIANS')
    lat = spiceypy.convrt(30, 'DEGREES', 'RADIANS')
    alt = 0.0

    x, y, z = spiceypy.georec(lon, lat, alt, re, f)

    lla0 = [46.017, 7.750, 1673]  # Zermatt, Switzerland
    lla = [45.976, 7.658, 4531]  # Matterhorn, , Switzerland
    pos0 = spiceypy.georec(spiceypy.convrt(lla0[1], 'DEGREES', 'RADIANS'),
                           spiceypy.convrt(lla0[0], 'DEGREES', 'RADIANS'),
                           lla0[2]/1000, re, f)
    pos1 = spiceypy.georec(spiceypy.convrt(lla[1], 'DEGREES', 'RADIANS'),
                           spiceypy.convrt(lla[0], 'DEGREES', 'RADIANS'),
                           lla[2] / 1000, re, f)
    dxyz = np.array(pos1) - np.array(pos0)

    def ecef_to_enu_matrix(lat_rad, lon_rad):
        """
        Rotation matrix to convert from Earth-Centered Earth-Fixed Frame (ECEF/ITRF93)
        to Earth Topocentric
        """
        sin_lat = np.sin(lat_rad)
        cos_lat = np.cos(lat_rad)
        sin_lon = np.sin(lon_rad)
        cos_lon = np.cos(lon_rad)

        return np.array([
            [-sin_lon, cos_lon, 0],
            [-sin_lat * cos_lon, -sin_lat * sin_lon, cos_lat],
            [cos_lat * cos_lon, cos_lat * sin_lon, sin_lat]
        ])


    rotation_matrix = ecef_to_enu_matrix(spiceypy.convrt(lla0[0], 'DEGREES', 'RADIANS'),
                                         spiceypy.convrt(lla0[1], 'DEGREES', 'RADIANS'))

    enu = rotation_matrix @ dxyz
    print(f'ENU Coordinates: {enu}')

    # plot ISS as seen from cebreros
    sp = Spice()
    sp.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')
    et_start = spiceypy.str2et('2024-05-15T17:15:24')
    et_end = spiceypy.str2et('2024-05-15T18:15:24')
    et = np.arange(et_start, et_end, 180)
    pos = sp.position('-125544', et, 'ITRF93', 'DSA2')
    altitudes = [p[2] for p in pos]
    times = [spiceypy.et2utc(t, 'C', 0) for t in et]

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(times, altitudes, label='Altitude (km)')
    plt.xlabel('Time (UTC)')
    plt.ylabel('Altitude (km)')
    plt.title(f'Altitude of ISS as seen from CEBREROS')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
