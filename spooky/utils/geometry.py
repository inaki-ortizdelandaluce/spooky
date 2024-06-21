import math
from geopy.point import Point
from geopy.distance import geodesic


def earth_los_distance(altitude: float, min_elevation: float, earth_radius=6371.0084):
    """
    Calculates the approximate maximum distance on the Earth's surface within which a satellite at a specified
    altitude can communicate from a ground station above a minimum elevation angle.
    Params:
        altitude: float
            Satellite's altitude in kilometers.
        min_elevation: float
            Minimum elevation in degrees above which ground station and satellite can communicate each other.
        earth_radius: float
            Earth radius in kilometers. Default value is the mean value of the Earth's tri-axial ellipsoid.
    Returns:
        Maximum distance on the Earth's surface in km.
    Example:
        import spooky.utils.geom
        distance = earth_los_distance(100, 15)
        print(angle) # expected value: 334.774 km
    """
    angle = earth_los_angle(altitude, min_elevation, earth_radius)
    return math.radians(angle) * earth_radius


def earth_los_angle(altitude: float, min_elevation: float, earth_radius=6371.0084):
    """
    Calculates the approximate maximum angular separation on the Earth's surface within which a satellite at a specified
    altitude can communicate from a ground station above a minimum elevation angle.
    Params:
        altitude: float
            Satellite's altitude in kilometers.
        min_elevation: float
            Minimum elevation in degrees above which ground station and satellite can communicate each other.
        earth_radius: float
            Earth radius in kilometers. Default value is the mean value of the Earth's tri-axial ellipsoid.
    Returns:
        Maximum angular separation on the Earth's surface in degrees.
    Example:
        import spooky.utils.geom
        angle = earth_los_angle(100, 15)
        print(angle) # expected value: 3.0107 degrees
    """
    e = math.cos(math.radians(min_elevation))
    re = earth_radius
    f = re / (re + altitude)

    # problem geometry is a scalene triangle of unknown angle theta with adjacent sides the distance to satellite
    # (re + altitude) and the earth radius (re), and other angles phi = (90 + elevation) and 180 - (theta + phi).
    # then using the cosine law equation and computing the opposite side as a function of trigonometric functions on
    # theta and phi and solving the resulting quadratic equation as a function of the distance ratio, f, and the cosine
    # of the elevation, e, we get the following formula:
    return math.degrees(math.acos(e**2 * f + math.sqrt(e**4 * f**2 - e**2 * (1 + f**2) + 1)))


def move_along_earth_surface(longitude: float, latitude: float, altitude: float, distance: float, bearing: float):
    """
    Move along Earth's surface a given distance from a starting position along a given direction via the corresponding
    geodesic.
    Params:
        longitude: float
            Longitude of the starting position in degrees.
        latitude: float
            Latitude of the starting position in degrees.
        altitude: float
            Altitude of the starting position in kilometers.
        distance: float
            The distance of the displacement in kilometers.
        bearing: float
            Bearing in degrees: 0 - North, 90 - East, 180 - South, 270 or -90 West.
    Returns:
        point (float, float, float)
        The longitude, latitude and altitude coordinates of the destination point using a starting position, bearing
        and a distance.
    Example:
         from spooky.utils.geometry import *
         distance = earth_los_distance(100, 15)
         lon, lat, alt = move_along_earth_surface(-3.319995, 55.909723, 0, distance, 0)
         print(lon. lat, alt)  # expected values: -3.319995, 58.915760, 0
    """
    # FIXME replace by analytic formula to get rid of geopy dependency
    p = Point(latitude, longitude, altitude)
    dest = geodesic(kilometers=distance).destination(p, bearing=bearing)  # uses WGS-84, aligned with spice
    return dest.longitude, dest.latitude, dest.altitude


