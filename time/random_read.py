#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker
from random import Random

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

with Benchmarker(1000*1000, width=20) as bench:
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
