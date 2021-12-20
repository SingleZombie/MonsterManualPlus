import math

from numpy import sign


def floor(x):
    x_sign = sign(x)
    return int(x_sign * math.floor(abs(x)))
