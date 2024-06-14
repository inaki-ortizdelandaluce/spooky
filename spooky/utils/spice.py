import spiceypy
import spiceypy.utils.support_types as stypes
import numpy as np
import re
import os.path as path
import tempfile
import math


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
                return kernel_new
            else:
                Spice.load(kernel)
                return kernel

    @staticmethod
    def unload_metakernel(kernel):
        spiceypy.unload(kernel)

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

    @staticmethod
    def lla2enu(frame, lla):
        """
        Transforms body-fixed geodetic coordinates to cartesian coordinates in a local East-North-Up (ENU) frame.
        Params:
            frame: str
                The local East-North-Up (ENU) frame, e.g. 'HOGS'. This reference frame should be available in the
                spice kernel dataset loaded.
            lla: list
                The geodetic coordinates (longitude, latitude and altitude) to be transformed to cartesian coordinates
                in the corresponding local ENU frame. Default geodetic coordinates units are degrees for longitude and
                latitude and kilometers for altitude.
        Returns:
            result: list
            The cartesian coordinates in the specified local East-North-Up (ENU) frame
        Example:
            from spooky.utils.spice import Spice
            lla  = [-5.0362, 56.6657, 0.931]  # Glen Coe, Three Sisters Beinn Fhada
            mk = Spice.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')
            enu = Spice.lla2enu('HOGS', lla)
            print(enu)  # expected [-105.2305, 85.4909, -0.5178]
            Spice.unload_metakernel(mk)
        """
        _, radii = spiceypy.bodvrd('EARTH', 'RADII', 3)
        re = radii[0]
        rp = radii[2]
        f = (re - rp) / re

        et = spiceypy.str2et('2024-11-30')

        frame_state, _ = spiceypy.spkezr(frame, et, 'ITRF93', 'NONE', 'EARTH')[:3]
        frame_center = frame_state[:3]
        rec = spiceypy.georec(spiceypy.convrt(lla[0], 'DEGREES', 'RADIANS'),
                              spiceypy.convrt(lla[1], 'DEGREES', 'RADIANS'),
                              lla[2], re, f)
        r = rec - frame_center

        xform = spiceypy.pxform('ITRF93', frame + '_TOPO',  et)
        return spiceypy.mxv(xform, r)

    @staticmethod
    def geo2enu(source, target, body='EARTH'):
        """
        Transforms body-fixed geodetic coordinates to cartesian coordinates in local East-North-Up (ENU) frame
        specifying the origin of the local ENU frame in geodetic coordinates. Default geodetic coordinates units are
        degrees for longitude and latitude and kilometers for altitude.
        Params:
            source: list of list
                A list where each element contains the geodetic coordinates of the origin of the local ENU frame,
                for example:
                [
                    [lon1, lat1, alt1],
                    [lon2, lat2, alt2],
                    ...
                ]
            target: list of list
                A list where each element contains the geodetic coordinates to be transformed to cartesian coordinates
                in the corresponding local ENU frame, for example:
                [
                    [lon1, lat1, alt1],
                    [lon2, lat2, alt2],
                    ...
                ]
        Returns:
            result: list of list
            A list of cartesian coordinates in the specified local East-North-Up (ENU) frames
        Example:
            from spooky.utils.spice import Spice
            geo0 = [[-3.319995, 55.909723, 0.010]]  # Heriot-Watt Optical Ground Station
            geo  = [[-5.0362, 56.6657, 0.931]]  # Glen Coe, Three Sisters Beinn Fhada
            mk = Spice.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')
            enu = Spice.geo2enu(geo0, geo)
            print(enu)  # expected [-105.2305, 85.4909, -0.5178]
            Spice.unload_metakernel(mk)
        """
        s_geo = np.asarray(source)
        t_geo = np.asarray(target)
        if s_geo.shape != t_geo.shape:
            raise TypeError(f"Centre {s_geo.shape} shape does not and match target shape {t_geo.shape}")
        if s_geo.shape[1] != 3 or s_geo.ndim != 2:
            raise TypeError(f"Input coordinates must be of shape (n,3)")

        _, radii = spiceypy.bodvrd(body, 'RADII', 3)
        re = radii[0]
        rp = radii[2]
        f = (re - rp) / re

        s_rec = [spiceypy.georec(spiceypy.convrt(s_geo[n, 0], 'DEGREES', 'RADIANS'),
                                 spiceypy.convrt(s_geo[n, 1], 'DEGREES', 'RADIANS'),
                                 s_geo[n, 2], re, f) for n in range(s_geo.shape[0])]
        t_rec = [spiceypy.georec(spiceypy.convrt(t_geo[n, 0], 'DEGREES', 'RADIANS'),
                                 spiceypy.convrt(t_geo[n, 1], 'DEGREES', 'RADIANS'),
                                 t_geo[n, 2], re, f) for n in range(t_geo.shape[0])]

        xyz = np.array(t_rec) - np.array(s_rec)
        if xyz.ndim == 1:
            xyz = xyz[np.newaxis, :]

        # compute body-fixed to topocentric frame rotation matrix
        # and apply to body-fixed target in cartesian coordinates
        rot = Spice.fixed2topo(s_geo[:, 0], s_geo[:, 1])
        return np.einsum('ijk,ik->ij', rot, xyz)

    @staticmethod
    def fixed2topo(lon, lat):
        """
        Rotation matrix to convert from body-fixed to topocentric frame given the geodetic coordinates of the
        topocentric frame's centre in degrees.
        Params:
            lon: float or np.ndarray
                Longitude of the topocentric frame's centre in degrees
            lat: float or np.ndarray
                Latitude of the topocentric frame's centre in degrees
        Returns:
        result: np.ndarray
            The rotation matrix which converts body-fixed to topocentric reference frame.

        """
        deg2rad = math.pi / 180

        sin_lat = np.sin(deg2rad * np.array(lat))
        cos_lat = np.cos(deg2rad * np.array(lat))
        sin_lon = np.sin(deg2rad * np.array(lon))
        cos_lon = np.cos(deg2rad * np.array(lon))

        return np.transpose(np.array([
            [-sin_lon, cos_lon, 0 * lon],
            [-sin_lat * cos_lon, -sin_lat * sin_lon, cos_lat],
            [cos_lat * cos_lon, cos_lat * sin_lon, sin_lat]
        ]), (2, 0, 1))


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
    print(f"dxyz = {dxyz}")

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
