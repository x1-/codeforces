#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from array import array
from benchmarker import Benchmarker

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

with Benchmarker(1000*1000, width=20) as bench:
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
