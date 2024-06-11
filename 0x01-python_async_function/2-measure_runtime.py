#!/usr/bin/env python3

import asyncio
import time

"""
This module contains a function asynchronously measures the approximate total
execution time of running wait_n(n, max_delay) and returns the average time
per coroutine (total_time / n).
"""

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function asynchronously measures the approximate total execution time
    of running wait_n(n, max_delay) and returns the average time per coroutine
    (total_time / n).

    It's important to note that due to limitations of the time.time() function
    and the way coroutines are scheduled, this measurement might not be
    perfectly accurate. It provides an approximate idea of the average
    execution time per coroutine.

    Args:
        n (int): The number of wait_random coroutines to spawn concurrently.
        max_delay (int, optional): The maximum delay for each wait_random
            coroutine in seconds. Defaults to 10.

    Returns:
        float: The approximate average execution time per coroutine
        (total_time / n).
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
