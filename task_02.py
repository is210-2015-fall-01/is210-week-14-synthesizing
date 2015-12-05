#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk14 synthensizing task02"""

import task_01


def fibo(count):
    """Return Fibonacci numbers.
    Args:
        count(int): the total number of Fibonacci numbers
    Returns: a list of Fibonacci numbers
    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
