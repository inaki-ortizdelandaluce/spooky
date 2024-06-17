import spiceypy
import re
import os.path as path
import tempfile
import math
import numpy as np


def version():
    return spiceypy.tkvrsn('TOOLKIT')


def load(kernels):
    spiceypy.furnsh(kernels)


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
            load(kernel_new.name)
            return kernel_new
        else:
            load(kernel)
            return kernel


def unload_metakernel(kernel):
    spiceypy.unload(kernel)


def clear():
    spiceypy.kclear()


def et2utc(et):
    return spiceypy.et2utc(et, 'ISOC', 0)


def utc2et(utc):
    return spiceypy.utc2et(utc)


def str2et(s):
    return spiceypy.str2et(s)


def body_radius(body):
    """
    Returns body radius in kilometers
    Params:
        body: the body name
    Returns:
        The body radius in kilometers
    """
    dim, radii = spiceypy.bodvrd(body, 'RADII', 3)
    return np.mean(radii)


def body_ellipsoid(body):
    _, radii = spiceypy.bodvrd(body, 'RADII', 3)
    req = radii[0]
    rf = radii[2]
    f = (req - rf) / req
    return req, f


def norad2naif(norad_id):
    return -100000 - norad_id


def position(target, et, frame, observer, correction='NONE'):
    """Finds the position of the target body relative to the observing body for the times
        specified.
    Params:
        target: str
            Name of the target body.
        et: float
            Ephemeris times for the positions to be computed.
        frame: str
            Reference frame relative to which the position vector should be expressed.
        observer: str
            Name of the observing body.
        correction: str
            The aberration corrections to be applied, either 'LT+S', 'CN+S' or 'NONE'.
    Returns:
        Array of position vectors of the target body relative to an observing body.
    """
    pos, lt = spiceypy.spkpos(target, et, frame, correction, observer)
    return pos


def state(target, et, frame, observer, correction='NONE'):
    """
    Finds the state (position and velocity) of the target body relative to the observing body for the times
    specified.
    Params:
        target: str
            Name of the target body
        et: float
            Ephemeris times for the positions to be computed.
        frame: str
            Reference frame relative to which the position vector should be expressed.
        observer: str
            Name of the observing body.
        correction: str
            The aberration corrections to be applied, either 'LT+S', 'CN+S' or 'NONE'.
    Returns:
        Tuple of position and velocity vectors of the target body relative to an observing body.
    """
    states, lt = spiceypy.spkezr(target, et, frame, correction, observer)

    if isinstance(states, list):
        states = np.asarray(states)
        return state[:, 0:3], state[:, 3:6]
    else:
        return states[0:3], states[3:6]


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
    from datetime import datetime
    et = spiceypy.str2et(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"))

    req, f = body_ellipsoid('EARTH')

    frame_state, _ = spiceypy.spkezr(frame, et, 'ITRF93', 'NONE', 'EARTH')[:3]
    frame_center = frame_state[:3]
    rec = spiceypy.georec(spiceypy.convrt(lla[0], 'DEGREES', 'RADIANS'),
                          spiceypy.convrt(lla[1], 'DEGREES', 'RADIANS'),
                          lla[2], req, f)
    xyz = rec - frame_center

    xform = spiceypy.pxform('ITRF93', frame + '_TOPO', et)
    return spiceypy.mxv(xform, xyz)


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

    req, f = body_ellipsoid(body)

    s_rec = [spiceypy.georec(spiceypy.convrt(s_geo[n, 0], 'DEGREES', 'RADIANS'),
                             spiceypy.convrt(s_geo[n, 1], 'DEGREES', 'RADIANS'),
                             s_geo[n, 2], req, f) for n in range(s_geo.shape[0])]
    t_rec = [spiceypy.georec(spiceypy.convrt(t_geo[n, 0], 'DEGREES', 'RADIANS'),
                             spiceypy.convrt(t_geo[n, 1], 'DEGREES', 'RADIANS'),
                             t_geo[n, 2], req, f) for n in range(t_geo.shape[0])]

    xyz = np.array(t_rec) - np.array(s_rec)
    if xyz.ndim == 1:
        xyz = xyz[np.newaxis, :]

    # compute body-fixed to topocentric frame rotation matrix
    # and apply to body-fixed target in cartesian coordinates
    rot = fixed2topo(s_geo[:, 0], s_geo[:, 1])
    return np.einsum('ijk,ik->ij', rot, xyz)


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


def sub_satellite_point(target, et, frame, observer, correction="XLT+S", method='NEAR POINT/ELLIPSOID'):
    """
    Compute the rectangular coordinates of the sub-observer point on a target body at a specified epoch,
    optionally corrected for light time and stellar aberration.

    Params:
        target: str
            The name of the target body, e.g. 'EARTH'. If the target body is represented by a tri-axial ellipsoid,
            it is assumed that a kernel variable representing the ellipsoid's radii is present in the kernel pool.
        et: list or np.ndarray
            Ephemeris times at which the observer times are computed. When aberrations are not used, is also the
            epochs  at which the position and orientation of the observer's state are computed.
        frame: str
            Body-fixed, body-centered target body frame, e.g. 'ITRF93'.
        observer: str
            The name of the observing body, typically the satellite, although iy could also be the earth or a
            surface point in the earth.
        correction: str
            The aberration corrections to be applied, either 'LT+S', 'CN+S' or 'NONE'.  The following values apply
            to the "transmission" case in which photons depart from the observer's location at `et' and arrive at
            the sub-observer point at the light-time corrected epoch et+lt: 'XLT', 'XLT+S', 'XCN' ans 'XCN+S'.
    Returns:
        result: np.ndarray
            Geodetic coordinates relative to the body-fixed target frame evaluated at the sub-observer epochs
    """
    times = np.asarray(et)
    if times.ndim != 1:
        raise TypeError(f"Input times must be a 1d array")

    positions = [spiceypy.subpnt(method, target, t, frame, correction, observer) for t in times]
    req, f = body_ellipsoid(target)
    geo = [spiceypy.recgeo(p, req, f) for p in positions]
    return np.asarray(geo)


def write_spk09(file, epochs, states, target, center='EARTH', frame='ITRF93', interpolation=5):
    epochs = np.asarray(epochs)
    states = np.asarray(states)

    if epochs.ndim != 1:
        raise TypeError(f"Input epochs must be a 1d array")

    if states.ndim != 2 or states.shape[1] != 6:
        raise TypeError(f"Input states must be of shape (n,6)")

    if epochs.shape[0] != states.shape[0]:
        raise TypeError(f"Number of input epochs and states must be equal (${epochs.shape[0]}!=${states.shape[0]})")

    # open a new SPK file handle
    name = f"SPK Type 9 - Target {target} ephemeris from {center} in {frame}"
    segment_id = f"SPK Type 9 - Segment 0"
    handle = spiceypy.spkopn(file, name, 5000)

    et0 = epochs[0]
    etn = epochs[-1]

    # write segment
    spiceypy.spkw09(handle, target, center, frame, et0, etn, segment_id, interpolation, len(epochs), epochs, states)

    # close the SPK file handle
    spiceypy.spkcls(handle)
