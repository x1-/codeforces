#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from benchmarker import Benchmarker
from array import array

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

"""
## benchmarker:         release 4.0.1 (for python)
## python version:      2.7.5
## python compiler:     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)
## python platform:     Darwin-13.4.0-x86_64-i386-64bit
## python executable:   ~/.virtualenvs/v2.7.5/bin/python
## cpu model:           Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz
## parameters:          loop=1000000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list append             0.1027    0.1000    0.0900    0.0100
for                     0.0416    0.0500    0.0400    0.0100
[None]                  0.0492    0.0500    0.0500    0.0000
[None] only             0.0058    0.0100    0.0100    0.0000
[0]                     0.0058    0.0000    0.0000    0.0000
array 1                 0.0990    0.1000    0.0900    0.0100
array 2                 0.1029    0.1000    0.1000    0.0000

## Ranking                real
[0]                     0.0058  (100.0) ********************
[None] only             0.0058  ( 99.3) ********************
for                     0.0416  ( 13.8) ***
[None]                  0.0492  ( 11.7) **
array 1                 0.0990  (  5.8) *
list append             0.1027  (  5.6) *
array 2                 0.1029  (  5.6) *

## Matrix                 real    [01]    [02]    [03]    [04]    [05]    [06]    [07]
[01] [0]                0.0058   100.0   100.7   722.2   853.7  1717.1  1782.8  1786.0
[02] [None] only        0.0058    99.3   100.0   717.2   847.9  1705.2  1770.5  1773.7
[03] for                0.0416    13.8    13.9   100.0   118.2   237.7   246.8   247.3
[04] [None]             0.0492    11.7    11.8    84.6   100.0   201.1   208.8   209.2
[05] array 1            0.0990     5.8     5.9    42.1    49.7   100.0   103.8   104.0
[06] list append        0.1027     5.6     5.6    40.5    47.9    96.3   100.0   100.2
[07] array 2            0.1029     5.6     5.6    40.4    47.8    96.1    99.8   100.0
"""
with Benchmarker(n, width=20) as bench:
    @bench("list append")
    def _(bm):
        xs = []
        for i in xrange(n):
            xs.append(i)

    @bench("for")
    def _(bm):
        xs = [i for i in xrange(n)]

    @bench("[None]")
    def _(bm):
        xs = [None] * n
        for i in xrange(n):
            xs[i]

    @bench("[None] only")
    def _(bm):
        xs = [None] * n

    @bench("[0]")
    def _(bm):
        xs = [0] * n

    @bench("array 1")
    def _(bm):
        xs = array('I', [ 0 for _ in xrange(n) ])

    @bench("array 2")
    def _(bm):
        xs = array('I', [ i for i in xrange(n) ])
