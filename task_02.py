#! usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple list comprehension."""

import task_01


def fibo(count):
    """A list comprehension.
    Args:
        count(int): Total number of Fibonacci numbers to return.
    Return:
        A list comprehension using Fibonacci numbers.
    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    fibnum = [i for i in task_01.xfibo(count)]
    return fibnum
