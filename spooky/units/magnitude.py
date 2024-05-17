from enum import Enum


class Magnitude(Enum):
    pico = -12
    nano = -9
    micro = -6
    milli = -3
    none = 0
    Kilo = 3
    Mega = 6
    Giga = 9
    Tera = 12

    @staticmethod
    def exponent(magnitude):
        if not isinstance(magnitude, Magnitude):
            raise ValueError("Input must be a member of the Magnitude enumeration.")

        return magnitude.value

    @staticmethod
    def ratio(a, b):
        if not isinstance(a, Magnitude) or not isinstance(b, Magnitude):
            raise ValueError("Input variables 'a' and 'b' must be members of the Magnitude enumeration.")

        return Magnitude.exponent(b) - Magnitude.exponent(a)

    @staticmethod
    def factor(a, b):
        if not isinstance(a, Magnitude) or not isinstance(b, Magnitude):
            raise ValueError("Input variables 'a' and 'b' must be members of the Magnitude enumeration.")

        return 10 ** Magnitude.ratio(a, b)

    @staticmethod
    def convert(a, b, values):
        if not isinstance(a, Magnitude) or not isinstance(b, Magnitude):
            raise ValueError("Input variables 'a' and 'b' must be members of the Magnitude enumeration.")

        return values * Magnitude.factor(a, b)
