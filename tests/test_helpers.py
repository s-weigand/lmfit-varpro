import math
import numpy as np


def assert_epsilon(wanted_value, given_value):
    """
    Test helper function to assert, if not all values of wanted_value and given_value
    are smaller than epsilon.
    Epsilon is 3 orders of magnitude smaller than the minimum of the absolute
    values of  wanted_value.

    Parameters
    ----------
    wanted_value: np.array, float, int
        Wanted value
    given_value: np.array, float, int
        Given Value
    """
    min_want = np.min(np.abs(wanted_value))
    epsilon = 10**(math.floor(math.log10(min_want)) - 3)
    msg = 'Want: {} Have: {} with epsilon {}'.format(wanted_value, given_value, epsilon)
    assert np.any(np.abs(wanted_value - given_value) < epsilon), msg
