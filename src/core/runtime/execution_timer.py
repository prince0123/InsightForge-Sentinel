"""
Execution Timer
"""

from time import perf_counter


class ExecutionTimer:

    def __init__(self):

        self._start = None

    def start(self):

        self._start = perf_counter()

    def stop(self):

        if self._start is None:

            return 0

        return round(

            perf_counter() - self._start,

            3

        )