#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker
from collections import deque
import heapq

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

"""
--------------------------------------------------------------------------------
## 10,000の場合
## benchmarker:         release 4.0.1 (for python)
## python version:      2.7.5
## python compiler:     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)
## python platform:     Darwin-13.4.0-x86_64-i386-64bit
## python executable:   ~/.virtualenvs/v2.7.5/bin/python
## cpu model:           Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz
## parameters:          loop=10000, cycle=1, extra=0

##                        real    (total    = user    + sys)
list                    0.0149    0.0100    0.0100    0.0000
array                   0.0083    0.0100    0.0100    0.0000
heappop                 0.0462    0.0500    0.0500    0.0000
deque                   0.0011    0.0000    0.0000    0.0000

## Ranking                real
deque                   0.0011  (100.0) ********************
array                   0.0083  ( 13.8) ***
list                    0.0149  (  7.7) **
heappop                 0.0462  (  2.5)

## Matrix                 real    [01]    [02]    [03]    [04]
[01] deque              0.0011   100.0   726.1  1293.6  4021.3
[02] array              0.0083    13.8   100.0   178.2   553.9
[03] list               0.0149     7.7    56.1   100.0   310.9
[04] heappop            0.0462     2.5    18.1    32.2   100.0

--------------------------------------------------------------------------------
## 1,000,000の場合
## benchmarker:         release 4.0.1 (for python)
## python version:      2.7.5
## python compiler:     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)
## python platform:     Darwin-13.4.0-x86_64-i386-64bit
## python executable:   ~/.virtualenvs/v2.7.5/bin/python
## cpu model:           Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz
## parameters:          loop=1000000, cycle=1, extra=0

##                        real    (total    = user    + sys)
list                  180.3090  180.3100  180.2700    0.0400
array                  85.2537   85.2600   85.2500    0.0100
heappop                 6.3716    6.3700    6.3700    0.0000
deque                   0.1068    0.1000    0.1000    0.0000

## Ranking                real
deque                   0.1068  (100.0) ********************
heappop                 6.3716  (  1.7)
array                  85.2537  (  0.1)
list                  180.3090  (  0.1)

## Matrix                 real    [01]    [02]    [03]    [04]
[01] deque              0.1068   100.0  5963.8 79797.2 168768.7
[02] heappop            6.3716     1.7   100.0  1338.0  2829.9
[03] array             85.2537     0.1     7.5   100.0   211.5
[04] list             180.3090     0.1     3.5    47.3   100.0

"""
with Benchmarker(n, width=20) as bench:
    nay = [i for i in xrange(n)]
    iay = array('I', [i for i in xrange(n)])
    day = deque(nay)
    hay = []
    for i in xrange(n):
      heapq.heappush(hay, i)

    @bench("list")
    def _(bm):
        for i in bm:
            nay.pop(0)

    @bench("array")
    def _(bm):
        for i in bm:
            iay.pop(0)

    @bench("heappop")
    def _(bm):
        for i in bm:
            heapq.heappop(hay)

    @bench("deque")
    def _(bm):
        for i in bm:
          day.popleft()
