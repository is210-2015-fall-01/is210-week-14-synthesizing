#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk14 synthesizing task01"""


def xfibo(count):
    """Fibo sequence generator.
    Args:
        count (int): Number of integers to return in the sequence.
    Returns:
        list: A list of Fibonacci numbers.
    Example:
        >>> for i in xfibo(6):
        print i
        0
        1
        1
        2
        3
    """
    counter = 0
    lastnum, curnum = 0, 1
    while counter < count:
        yield lastnum
        counter += 1
        lastnum, curnum = curnum, lastnum + curnum
