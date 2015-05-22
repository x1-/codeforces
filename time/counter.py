#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import string, sys
from benchmarker import Benchmarker
from collections import Counter
from random import Random

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

"""
word-count
## benchmarker:         release 4.0.1 (for python)
## python version:      2.7.5
## python compiler:     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)
## python platform:     Darwin-13.4.0-x86_64-i386-64bit
## python executable:   ~/.virtualenvs/v2.7.5/bin/python
## cpu model:           Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz
## parameters:          loop=1000000, cycle=1, extra=0

##                        real    (total    = user    + sys)
dict                    0.2395    0.2400    0.2400    0.0000
Counter1                0.3784    0.3800    0.3800    0.0000
Counter2                0.2940    0.3000    0.3000    0.0000

## Ranking                real
dict                    0.2395  (100.0) ********************
Counter2                0.2940  ( 81.5) ****************
Counter1                0.3784  ( 63.3) *************

## Matrix                 real    [01]    [02]    [03]
[01] dict               0.2395   100.0   122.8   158.0
[02] Counter2           0.2940    81.5   100.0   128.7
[03] Counter1           0.3784    63.3    77.7   100.0
"""
with Benchmarker(n, width=20) as bench:

    ix = [ i for i in xrange(n) ]
    r = Random()
    r.shuffle(ix)

    chs = list(string.ascii_letters)
    ws = []
    for i in ix:
        m = i % 52
        ws.append( chs[m] )

    @bench("dict")
    def _(bm):
        dt = dict()
        for i in bm:
            key = ws[i]
            v = dt.setdefault( key, 0 )
            dt[key] += 1

    @bench("Counter1")
    def _(bm):
        dt = Counter()
        for i in bm:
            key = ws[i]
            dt[key] += 1

    @bench("Counter2")
    def _(bm):
        dt = Counter( ws )
