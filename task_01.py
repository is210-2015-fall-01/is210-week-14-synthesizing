#! usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibonacci sequence generator."""


def xfibo(count):
    """Docstring.
    Args:
        count(int): The number of Fibonacci numbers to return.
    Return:
        Number specified in the counter parameter.
    Example:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """
    i = 0
    lastnum, curnum = 0, 1
    while i < count:
        yield lastnum
        lastnum, curnum = curnum, lastnum + curnum
        i += 1
