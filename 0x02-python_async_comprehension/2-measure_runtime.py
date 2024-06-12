#!/usr/bin/env python3

"""
This script demonstrates asynchronous list comprehension to generate a list of
random floating-point numbers and measures the total runtime of parallel
executions.

The `async_comprehension` function asynchronously iterates over the
`async_generator` and collects the yielded numbers into a list.

The `measure_runtime` coroutine executes `async_comprehension` four times
in parallel using `asyncio.gather` and returns the total execution time.

# Explanation of Runtime

Even though each `async_comprehension` call involves a 1-second delay
using `asyncio.sleep(1)`, the total runtime won't necessarily be exactly
4 seconds (1 second * 4 executions). This is because of the asynchronous
nature of the code.

- The `asyncio.gather` function doesn't wait for each coroutine to finish
completely before moving on. It schedules them to run concurrently, taking
advantage of any available processing power.
- Each coroutine can potentially yield control back to the event loop while
waiting for I/O operations (like the sleep). During these yield points, other
coroutines can run, potentially overlapping their execution time.

Therefore, the total runtime will likely be **less than 4 seconds** due to this
concurrency. It might be slightly more than 1 second but shouldn't reach 4
seconds unless there are significant delays or limitations in your system's
processing capabilities.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
    Measures the total runtime of executing `async_comprehension`
    four times in parallel.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.time()  # Record start time

    # Run four instances of async_comprehension concurrently
    # using asyncio.gather
    await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension()
    )

    end_time = time.time()  # Record end time

    return end_time - start_time
