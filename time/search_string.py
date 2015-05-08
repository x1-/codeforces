#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import re, string, sys
from benchmarker import Benchmarker
from random import Random

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000*1000

with Benchmarker(1000*1000, width=20) as bench:
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
