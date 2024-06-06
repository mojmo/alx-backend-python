#!/usr/bin/env python3

"""
This script defines a function named sum_mixed_list that calculates the sum
of elements in a list containing either integers or floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function calculates the sum of all elements in a list containing
    either integers or floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers or floats
        to be summed.

    Returns:
        float: The sum of all elements in the list, which will be a float.
    """

    return sum(mxd_lst)
