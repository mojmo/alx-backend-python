#!/usr/bin/env python3

"""
This script defines a function named sum_list that calculates
the sum of elements in a list of floating-point numbers.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function calculates the sum of all elements in a list
    of floating-point numbers.

    Args:
        input_list (List[float]): The list of floating-point numbers
        to be summed.

    Returns:
        float: The sum of all elements in the list.
    """

    return sum(input_list)
