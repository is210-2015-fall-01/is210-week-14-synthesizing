#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""


def xfibo(count):
    """Fibonacci sequence generator
    Args:
        count (int): number of items to return
    Return:
        generator of fibo sequence up to given number
    Examples:
        >>> for i in xfibo(5):
        print i
        0
        1
        1
        2
        3
    """
    iterations = 0
    lastnum, curnum = 0, 1
    while iterations < count:
        yield lastnum
        lastnum, curnum = curnum, curnum + lastnum
        iterations += 1
