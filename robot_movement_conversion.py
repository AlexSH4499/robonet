import math


import numpy as np
from niryo_one_python_api.niryo_one_api import *
import rospy

def ensure_length(coords=[]):
    return len(coords) == 6

def cartesian_to_radians(coords=[]):
    return np.array([x * math.pi for x in coords])
