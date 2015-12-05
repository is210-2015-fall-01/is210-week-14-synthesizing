#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Docstring"""

import task_01


def fibo(count):
    """Return fibonacci generator as list
    Args:
        count (int): number of items to return
    Return:
        list of fibonacci sequence numbers up to given number
    Examples:
        >>> fibo(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    iterator = 0
    fibolist = [num for num in task_01.xfibo(count)]
    while iterator < count:
        iterator += 1
    return fibolist
