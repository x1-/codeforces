#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker

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
list                  181.7629  181.7700  181.7200    0.0500
array                  85.5718   85.5700   85.5600    0.0100

## Ranking                real
array                  85.5718  (100.0) ********************
list                  181.7629  ( 47.1) *********

## Matrix                 real    [01]    [02]
[01] array             85.5718   100.0   212.4
[02] list             181.7629    47.1   100.0
"""
with Benchmarker(n, width=20) as bench:
    nay = [i for i in xrange(n)]
    iay = array('I', [i for i in xrange(n)])

    @bench("list")
    def _(bm):
        for i in xrange(n):
            nay.pop(0)

    @bench("array")
    def _(bm):
        for i in xrange(n):
            iay.pop(0)
