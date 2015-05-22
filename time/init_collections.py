#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker
from collections import deque
import heapq

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
list append             0.0989    0.1000    0.0900    0.0100
for                     0.0411    0.0300    0.0300    0.0000
[None] only             0.0073    0.0200    0.0100    0.0100
array                   0.1047    0.1000    0.1000    0.0000
heappush                0.4908    0.4900    0.4800    0.0100
deque                   0.1107    0.1100    0.1100    0.0000

## Ranking                real
[None] only             0.0073  (100.0) ********************
for                     0.0411  ( 17.8) ****
list append             0.0989  (  7.4) *
array                   0.1047  (  7.0) *
deque                   0.1107  (  6.6) *
heappush                0.4908  (  1.5)

## Matrix                 real    [01]    [02]    [03]    [04]    [05]    [06]
[01] [None] only        0.0073   100.0   560.8  1349.8  1430.0  1510.9  6701.8
[02] for                0.0411    17.8   100.0   240.7   255.0   269.4  1195.1
[03] list append        0.0989     7.4    41.5   100.0   105.9   111.9   496.5
[04] array              0.1047     7.0    39.2    94.4   100.0   105.7   468.7
[05] deque              0.1107     6.6    37.1    89.3    94.6   100.0   443.6
[06] heappush           0.4908     1.5     8.4    20.1    21.3    22.5   100.0
"""
with Benchmarker(n, width=20) as bench:

    @bench("list append")
    def _(bm):
        xs = []
        for i in bm:
            xs.append(i)

    @bench("for")
    def _(bm):
        xs = [i for i in bm]

    @bench("[None] only")
    def _(bm):
        xs = [None] * n

    @bench("array")
    def _(bm):
        xs = array('I', [ i for i in bm ])

    @bench("heappush")
    def _(bm):
        xs = []
        for i in bm:
          heapq.heappush(xs, i)

    @bench("deque")
    def _(bm):
        xs = deque()
        for i in bm:
          xs.append( i )
