#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker
from random import Random

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
list                    1.1829    1.1800    1.1700    0.0100
array                   1.2053    1.2100    1.2000    0.0100

## Ranking                real
list                    1.1829  (100.0) ********************
array                   1.2053  ( 98.1) ********************

## Matrix                 real    [01]    [02]
[01] list               1.1829   100.0   101.9
[02] array              1.2053    98.1   100.0
"""
with Benchmarker(n, width=20) as bench:
    r = Random()
    nay = [i for i in xrange(n)]
    iay = array('I', [ i for i in xrange(n) ])

    @bench("list")
    def _(bm):
        r.shuffle(nay)
        xs = sorted(nay)

    @bench("array")
    def _(bm):
        r.shuffle(iay)
        xs = sorted(iay)
