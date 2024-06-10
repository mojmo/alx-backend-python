#!/usr/bin/env python3

"""
This script defines an asynchronous coroutine named wait_random
that waits for a random delay and returns the delay value.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This asynchronous coroutine waits for a random delay between 0 and
    the specified max_delay (inclusive) in seconds. It then returns the
    actual delay that was waited for as a floating-point number.

    Args:
        max_delay (int, optional): The maximum delay to wait for in seconds.
            Defaults to 10.

    Returns:
        float: The actual delay that was waited for in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
