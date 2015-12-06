#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a list comprehension"""


import task_01


def fibo(count):
    """A function that generates a Fibonacci list comprehension.

    Args:
        Has one argument count, that takes the count to be calculated until.

    Returns:
        A sequence of Fibonacci numbers, horizontally listed.

    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
