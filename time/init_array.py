#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from benchmarker import Benchmarker
from array import array

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

with Benchmarker(1000*1000, width=20) as bench:
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
