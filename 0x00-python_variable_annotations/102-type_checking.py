#!/usr/bin/env python3

"""
This script defines a function named `zoom_array` that creates a new list by
repeating each element of an input tuple a specified number of times.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    This function creates a new list by repeating each element of an input
    tuple a specified number of times.

    Args:
        lst (Tuple): The input tuple containing the elements to be
        zoomed (repeated).
        factor (int, optional): The zoom factor (number of times to repeat
        each element).
        Defaults to 2.

    Returns:
        List: A new list containing each element from the input tuple
        repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
