#!/usr/bin/env python3

"""
This script defines an asynchronous generator function `async_generator`
that iterates 10 times, yielding a random floating-point number between
0.0 (inclusive) and 10.0 (exclusive) with each iteration.

It leverages the `asyncio` library for asynchronous operations:

- `asyncio.sleep(1)` introduces a one-second delay between each yield.
- `random.uniform(0, 10)` generates a random floating-point number within
the specified range.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random floating-point numbers between
    0.0 (inclusive) and 10.0 (exclusive) with a one-second delay between
    each yield.

    Yields:
        float: A random floating-point number within the specified range.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
