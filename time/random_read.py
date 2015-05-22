#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker
from random import Random

"""
## benchmarker:         release 4.0.1 (for python)
## python version:      2.7.5
## python compiler:     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)
## python platform:     Darwin-13.4.0-x86_64-i386-64bit
## python executable:   ~/.virtualenvs/v2.7.5/bin/python
## cpu model:           Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz
## parameters:          loop=1000000, cycle=1, extra=0

##                        real    (total    = user    + sys)
list                    0.2914    0.2800    0.2800    0.0000
array                   0.2077    0.2100    0.2100    0.0000
1byte array             0.1747    0.1800    0.1800    0.0000

## Ranking                real
1byte array             0.1747  (100.0) ********************
array                   0.2077  ( 84.1) *****************
list                    0.2914  ( 59.9) ************

## Matrix                 real    [01]    [02]    [03]
[01] 1byte array        0.1747   100.0   118.9   166.8
[02] array              0.2077    84.1   100.0   140.3
[03] list               0.2914    59.9    71.3   100.0
"""
n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

with Benchmarker(n, width=20) as bench:
    r = Random()
    ix = [i for i in xrange(n)]
    r.shuffle(ix)

    nay = [i for i in xrange(n)]
    iay = array('I', [ i for i in xrange(n) ])
    bay = array('b', [ 1 for _ in xrange(n) ])

    @bench("list")
    def _(bm):
        tmp = 0
        for i in ix:
            tmp = nay[i]

    @bench("array")
    def _(bm):
        tmp = 0
        for i in ix:
            tmp = iay[i]

    @bench("1byte array")
    def _(bm):
        tmp = 0
        for i in ix:
            tmp = bay[i]
