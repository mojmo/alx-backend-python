#!/usr/bin/env python3

"""
This script measures the total runtime of executing an asynchronous
comprehension four times in parallel. The comprehension (assumed to
be defined in a separate module) iterates asynchronously, potentially
involving delays.

- `async_comprehension` (from 1-async_comprehension.py): Iterates
asynchronously.
- `measure_runtime`: Measures the total execution time of four parallel runs.

Even though individual iterations might involve delays, the asynchronous
nature can lead to a total runtime **less than 4 seconds** due to
concurrent execution.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing `async_comprehension`
    four times in parallel.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.time()  # Record start time

    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()  # Record end time

    return end_time - start_time
