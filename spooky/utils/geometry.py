import math


def earth_los_angle(altitude: float, elevation: float, earth_radius=6371.0084):
    """
    Calculates the approximate angular separation on the Earth's surface within which a satellite at a specified
    altitude can communicate from a ground station (i.e. above a minimum elevation angle)
    Params:
        altitude: float
            Satellite's altitude in kilometers.
        elevation: float
            Minimum elevation in degrees above which ground station and satellite can communicate each other.
        earth_radius: float
            Earth radius in kilometers. Default value is the mean value of the Earth's triaxial ellipsoid.
    Returns:
        Angular separation on the Earth's surface in degrees.
    Example:
        import spooky.utils.geom
        angle = earth_los_angle(100, 15)
        print(angle) # expected value: 3.0107 degrees
    """
    e = math.cos(math.radians(elevation))
    re = earth_radius
    f = re / (re + altitude)

    # problem geometry is a scalene triangle of unknown angle theta with adjacent sides the distance to satellite
    # (re + altitude) and the earth radius (re), and other angles phi = (90 + elevation) and 180 - (theta + phi).
    # then using the cosine law equation and computing the opposite side as a function of trigonometric functions on
    # theta and phi and solving the resulting quadratic equation as a function of the distance ratio, f, and the cosine
    # of the elevation, e, we get the following formula:
    return math.degrees(math.acos(e**2 * f + math.sqrt(e**4 * f**2 - e**2 * (1 + f**2) + 1)))
