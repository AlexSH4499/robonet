import math


import numpy as np



def ensure_length(coords=[]):

    return len(coords) == 6

def cartesian_to_radians(coords=[]):
    return np.array([x * math.pi for x in coords])
