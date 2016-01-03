#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a Fibonacci sequence generator"""


def xfibo(count):
    """A function that generates a Fibonacci sequence.

    Args:
        Has one argument count, that takes the count to be calculated until.

    Returns:
        A sequence of Fibonacci numbers, vertically listed.

    Example:
        >>>
        0
        1
        1
        2
        3
    """
    lastnum, curnum = 0, 1
    yield lastnum
    counter = 1
    while counter < count:
        yield curnum
        lastnum, curnum = curnum, lastnum + curnum
        counter += 1

if __name__ == "__main__":
    for varnum in xfibo(5):
        print varnum
