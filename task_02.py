#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_02 docstring."""


import task_01


def fibo(count):
    """This is a fibo function.

    Args:
        count (int): Maximum number of fibonacci numbers.

    Returns:
        list (list): A list of fibonacci numbers.

    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
