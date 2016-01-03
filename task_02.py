#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 14 synthesizing task_01."""

import task_01


def fibo(count):
    """This function going to use list comprehension to wrap Fibonacci numbers.

    Args:
        count(int): fibonacci numbers.

    Return:
        return list of Fibonacci numbers.

    Examples:
        >>>fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
