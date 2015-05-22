#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
from benchmarker import Benchmarker

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

with Benchmarker(n, width=22, cycle=3) as bench:
    @bench("no buffering")
    def _(bm):
        for i in xrange(n):
            x = int(raw_input()) / 10
            print x

    @bench("buffering output")
    def _(bm):
        res = []
        for i in xrange(n):
            res.append( int(raw_input()) / 10 )
        for i in res:
            print i

    @bench("buffering input")
    def _(bm):
        xs = [ int(raw_input()) for _ in xrange(n) ]
        for i in xs:
            x = i / 10
            print x

    @bench("buffering both")
    def _(bm):
        xs = [ int(raw_input()) / 10 for _ in xrange(n) ]
        for i in xs:
            print i
