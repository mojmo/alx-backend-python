#!/usr/bin/env python3

"""_
This script defines a function named floor that replicates the behavior
of the built-in math.floor function.
"""

import math


def floor(n: float) -> int:
    """
    This function returns the largest integer less than or equal to the
    given floating-point number.

    Args:
        n (float): The floating-point number to be converted to an integer.

    Returns:
        int: The largest integer less than or equal to n.
    """

    return math.floor(n)
