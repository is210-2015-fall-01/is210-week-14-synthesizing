#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 synthesizing task_01"""


def xfibo(count):
    """This function is Fibonacci Sequence Generator.

    The generator should be able to produce a variable number of Fibonacci
    numbers as specified in the count parameter.

    Args:
        count(int): Fibonnaci Numbers.

    Returns:
        return fibonacci sequence.

    Examples:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """
    firstnum, lastnum = 0, 1
    iterations = 0
    while iterations < count:
        yield firstnum
        firstnum, lastnum = lastnum, firstnum + lastnum
        iterations += 1
