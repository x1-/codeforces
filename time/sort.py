#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker
from random import Random

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

with Benchmarker(1000*1000, width=20) as bench:
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
