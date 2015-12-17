#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses a list comprehension to build the list."""


import task_01


def fibo(count):
    """Builds list simply.
    Args:
        count(int): # of items to return
    Returns:
        list of fibonacci sequence numbers up to input #
    Examples:
        >>>fibo(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    fibolist = [num for num in task_01.xfibo(count)]
    return fibolist
