#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module has a new Fibonacci sequence generator."""


def xfibo(count):
    """This produces a variable number of Fibonacci numbers.
    Args:
        count(int): # of Fibonacci numbers to return
    Returns:
        Fibo sequences up to the # given
    Examples:
        >>>for i in xfibo(6):
            print i
            0
            1
            1
            2
            3
            5
    """
    counter = 0
    lastnum, curnum = 0, 1
    while counter < count:
        yield lastnum
        lastnum, curnum = curnum, curnum + lastnum
        counter += 1
