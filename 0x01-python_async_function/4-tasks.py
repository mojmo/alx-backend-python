#!/usr/bin/env python3

"""
spawns n asyncio.Tasks that call wait_random concurrently
and returns a list of the delays
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    This function spawns n asyncio.Tasks that call wait_random concurrently
    and returns a list of the delays in ascending order.

    Args:
        n (int): The number of tasks to spawn concurrently.
        max_delay (int, optional): The maximum delay for each wait_random
            coroutine in seconds. Defaults to 10.

    Returns:
        List[float]: A list of delays (in ascending order) experienced by
            each spawned task_wait_random coroutine.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
