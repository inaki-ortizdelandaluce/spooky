import spiceypy
import spooky.spice as spice
import os

def test_lla2enu():
    import spiceypy
    import spooky.spice as spice
    import numpy as np

    spice.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')
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


def test_geometry_finder():
    # start = '2024-05-21 15:00:00'
    # end = '2024-05-21 20:00:00'
    start = '2024-05-23 15:00:00'
    end = '2024-05-23 20:00:00'
    # start = '2020-05-01 11:36:00'
    # end = '2020-05-02 13:36:00'

    spice.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')

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
        print(f"Window {i+1}:{spice.et2utc(window_start)} - {spice.et2utc(window_end)}")


def test_plot_spacecraft_altitude():
    # plot ISS as seen from cebreros
    spice.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')
    et_start = spiceypy.str2et('2024-05-15T17:15:24')
    et_end = spiceypy.str2et('2024-05-15T18:15:24')
    import numpy as np
    et = np.arange(et_start, et_end, 180)
    pos = spice.position('-125544', et, 'ITRF93', 'DSA2')
    altitudes = [p[2] for p in pos]
    ts = [spiceypy.et2utc(t, 'C', 0) for t in et]

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(ts, altitudes, label='Altitude (km)')
    plt.xlabel('Time (UTC)')
    plt.ylabel('Altitude (km)')
    plt.title(f'Altitude of ISS as seen from CEBREROS')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def test_write_spk09():
    spice.load(['mar097.bsp', '/Users/iortiz/spice/kernels/spooky/lsk/naif0012.tls'])
    et = spice.str2et("2018 Apr 03 08:35")
    time = et
    step = 60
    delta = 10.0
    steps = 800

    import math
    import numpy as np
    epochs = np.zeros(steps)
    states = np.zeros(shape=(steps, 6))
    for i in range(steps):
        pos, vel = spice.state("PHOBOS", time, "J2000", "MARS")
        states[i] = np.concatenate((pos, vel), axis=0)
        epochs[i] = time + 3600.0  # object follows phobos 1 hour later
        time = time + step + math.sin(0.5 * math.pi * i / 2.0) * delta  #
    spice.write_spk09("spkw09_ex1.bsp", epochs, states, 403, "MARS", "J2000", 3)


def test_compare_spk09():
    spice.load(['mar097.bsp', '/Users/iortiz/spice/kernels/spooky/lsk/naif0012.tls'])
    et = spice.str2et("2018 Apr 03 08:35")
    et = et + 43200.0  # plus 12 hours
    pos, vel = spice.state("PHOBOS", et, "J2000", "MARS")
    import numpy as np
    state = np.concatenate((pos, vel), axis=0)
    print(f"Epoch(s) : {et}\nPosition(km) : {state[0]:13.5f}, {state[1]:13.5f}, {state[2]:13.5f}\nVelocity (km/s): "
          f"{state[3]:13.5f}, {state[4]:13.5f}, {state[5]:13.5f}")

    et = et + 3600.0  # plus 13 hours
    spice.load(['spkw09_ex1.bsp'])
    pos, vel = spice.state("403", et, "J2000", "MARS")
    state = np.concatenate((pos, vel), axis=0)
    print(f"Epoch(s) : {et}\nPosition(km) : {state[0]:13.5f}, {state[1]:13.5f}, {state[2]:13.5f}\nVelocity (km/s): "
          f"{state[3]:13.5f}, {state[4]:13.5f}, {state[5]:13.5f}")


def test_llat2spk():
    spice.load_metakernel('/Users/iortiz/spice/kernels/spooky/mk/spooky_ops.tm')
    filenames = ['100kmOrbitLLAT.txt', '100kmSSOrbitLLAT.txt', '500kmOrbitLLAT.txt', '500kmSSOrbitLLAT.txt',
                 '1000kmSSOrbitLLAT.txt', '2000kmSSOrbitLLAT.txt', '3000kmSSOrbitLLAT.txt', '4000kmSSOrbitLLAT.txt',
                 '5000kmSSOrbitLLAT.txt']
    dir_path = os.path.dirname(os.path.realpath(__file__))
    obj_id = -100000
    et0 = spice.str2et('2023-01-01T00:00:00')

    for idx, name in enumerate(filenames):
        path = os.path.join(dir_path, '../data/orbits/', name)
        obj_id = obj_id - idx
        spk_file = f"spooky_{-obj_id}_{name.split('.')[0]}.bsp"

        spice.llat2spk(obj_id, path, spk_file, et0=et0)
        print(f"SPK {spk_file} created")


if __name__ == '__main__':
    # test_write_spk09()
    # test_compare_spk09()
    test_llat2spk()
