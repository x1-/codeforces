#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import re, string, sys
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
with Benchmarker(n, width=20) as bench:
    search = '_SEARCH_'

    ix = [ i for i in xrange(n) ]
    r = Random()
    r.shuffle(ix)
    sp = int(n * 4 / 5)

    chs = list(string.ascii_letters)
    t = ''
    for i in ix[0:sp]:
        m = i % 52
        t += chs[m]

    t += search
    for i in ix[sp:]:
        m = i % 52
        t += chs[m]

    @bench("find")
    def _(bm):
        for i in xrange(n):
            idx = t.find(search)

    @bench("in")
    def _(bm):
        for i in xrange(n):
            idx = search in t

    @bench("re")
    def _(bm):
        for i in xrange(n):
            m = re.search(search, t)
            idx = m.start()

    @bench("pre-compiled re")
    def _(bm):
        p = re.compile(search)
        for i in xrange(n):
            m = p.search(t)
            idx = m.start()
