#!/usr/bin/env python3

"""
This script defines a function named make_multiplier that creates a new
function that multiplies a number by a given value.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function creates a new function that multiplies a number
    by a given value.

    Args:
        multiplier (float): The value used for multiplication in
        the returned function.

    Returns:
        Callable[[float], float]: A new function that takes a single
        float argument and returns the product of that argument and
        the multiplier.
    """

    def mult(n: float) -> float:
        """
        This function performs the multiplication by the given multiplier.
        (internal helper function)
        """
        return n * multiplier

    return mult
