#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker
from collections import deque

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

"""
--------------------------------------------------------------------------------
## 10,000件の場合
## benchmarker:         release 4.0.1 (for python)
## python version:      2.7.5
## python compiler:     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)
## python platform:     Darwin-13.4.0-x86_64-i386-64bit
## python executable:   ~/.virtualenvs/v2.7.5/bin/python
## cpu model:           Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz
## parameters:          loop=10000, cycle=1, extra=0

##                        real    (total    = user    + sys)
list                    0.0260    0.0200    0.0200    0.0000
array                   0.0083    0.0200    0.0100    0.0100
deque                   0.1191    0.1100    0.1100    0.0000

## Ranking                real
array                   0.0083  (100.0) ********************
list                    0.0260  ( 32.1) ******
deque                   0.1191  (  7.0) *

## Matrix                 real    [01]    [02]    [03]
[01] array              0.0083   100.0   311.5  1426.7
[02] list               0.0260    32.1   100.0   458.0
[03] deque              0.1191     7.0    21.8   100.0

--------------------------------------------------------------------------------
## 1,000,000件の場合
## benchmarker:         release 4.0.1 (for python)
## python version:      2.7.5
## python compiler:     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)
## python platform:     Darwin-13.4.0-x86_64-i386-64bit
## python executable:   ~/.virtualenvs/v2.7.5/bin/python
## cpu model:           Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz
## parameters:          loop=1000000, cycle=1, extra=0

##                        real    (total    = user    + sys)
list                  240.1593  240.1700  240.0900    0.0800
array                  86.6021   86.6000   86.5900    0.0100
deque                   0.1176    0.1200    0.1100    0.0100

## Ranking                real
deque                   0.1176  (100.0) ********************
array                  86.6021  (  0.1)
list                  240.1593  (  0.0)

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.1176   100.0 73671.9 204302.1
[02] array             86.6021     0.1   100.0   277.3
[03] list             240.1593     0.0    36.1   100.0
"""
with Benchmarker(n, width=20) as bench:
    nay = []
    iay = array('I', [])
    day = deque()

    @bench("list")
    def _(bm):
        for i in xrange(n):
            nay.insert(0, i)

    @bench("array")
    def _(bm):
        for i in xrange(n):
            iay.insert(0, i)

    @bench("deque")
    def _(bm):
        for i in bm:
          day.appendleft( i )
