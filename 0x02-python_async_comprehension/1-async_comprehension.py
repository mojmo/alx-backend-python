#!/usr/bin/env python3

"""
This script demonstrates asynchronous list comprehension to generate a list of
random floating-point numbers.

It assumes the existence of a separate module named `0-async_generator.py` that
provides the `async_generator` function, which yields random numbers.

The `async_comprehension` function asynchronously iterates over the
`async_generator` and collects the yielded numbers into a list.

This script serves as an example of utilizing asynchronous comprehensions for
efficient random number generation in asynchronous contexts.
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously generates a list of random floating-point numbers between
    0.0 (inclusive) and 10.0 (exclusive) by using an asynchronous
    comprehension.

    This function relies on the `async_generator` function (assumed to
    be defined in a separate module named `0-async_generator.py`) to
    yield random numbers.

    Returns:
        list[float]: A list containing the generated random numbers.
    """

    random_numbers = [i async for i in async_generator()]

    return random_numbers
