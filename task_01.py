#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_01 docstring."""


def xfibo(count):
    """Function to create fibonacci numbers.

    This function contains a generator that creates
    fibonacci numbers.

    Args:
        count (int): Numbers to generate.

    Returns:
        list (int): A list of numbers.

    Example:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """
    last, current = 0, 1
    counter = 0

    while counter < count:
        yield last
        counter += 1
        last, current = current, last + current
