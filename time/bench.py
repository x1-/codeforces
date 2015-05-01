#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
import time
import string
import re
import random
from random import Random
from array import array

#start = time.clock()

n = int(sys.argv[1])

#"""
## list append
#100000	0.027873
#1000000	0.260543
#10000000	2.558889
#"""
##xs = []
##for i in xrange(n):
##  xs.append(i)
# 
#"""
#for
#100000	0.015099
#1000000	0.14847
#10000000	1.42081
#"""
##xs = [i for i in xrange(n)]
# 
#"""
#[None]
#100000	0.016606
#1000000	0.179783
#10000000	1.727175
#"""
##xs = [None] * n
##for i in xrange(n):
##  xs[i]
# 
#"""
#[None] only
#100000	0.000724
#1000000	0.006474
#10000000	0.071949
#"""
#xs = [None] * n

#"""
#[None]
#100000	0.000803
#1000000	0.006982
#10000000	0.074916
#"""
#xs = [0] * n

#"""
#array
#100000	0.018191
#1000000	0.164888
#10000000	1.853745
#"""
#xs = array('I', [ 0 for _ in xrange(n) ])

#"""
#array
#100000	0.024631
#1000000	0.232682
#10000000	2.49165
#"""
#xs = array('I', [ i for i in xrange(n) ])

#----------------------------
# random read
#----------------------------

#"""
#list
#10000000	4.209885
#"""
#xs = [i for i in xrange(n)]

#"""
#array
#10000000	3.29262
#"""
#xs = array('I', [ i for i in xrange(n) ])

#"""
#1byte array
#10000000	3.257461
#"""
#xs = array('b', [ 1 for _ in xrange(n) ])
#ix = [i for i in xrange(n)]
#r = Random()
#r.shuffle(ix)

#start = time.clock()
#tmp = 0
#for i in ix:
#  tmp = xs[i]

#----------------------------
# pop
#----------------------------
#"""
#list
#10000000	1.90925
#"""
#xs = [i for i in xrange(n)]

#"""
#array
#10000000	3.137967
#"""
#xs = array('I', [i for i in xrange(n)])

#start = time.clock()
#for i in xrange(n):
#  xs.pop()

#----------------------------
# pop(0)
#----------------------------
#"""
#list
#10000000	205.67833
#"""
#xs = [i for i in xrange(n)]

#"""
#array
#10000000	93.492565
#"""
#xs = array('I', [i for i in xrange(n)])
# 
#start = time.clock()
#for i in xrange(n):
#  xs.pop(0)

#----------------------------
# insert(0)
#----------------------------
#"""
#list
#1000000	263.220432
#"""
#xs = []

#"""
#array
#1000000	93.38436
#"""
#xs = array('I', [])

#start = time.clock()
#for i in xrange(n):
#  xs.insert(0, i)

#----------------------------
# sort
#----------------------------
#"""
#list
#1000000	0.671997
#"""
#xs = [i for i in xrange(n)]

#"""
#array
#1000000	0.730575
#"""
#xs = array('I', [ i for i in xrange(n) ])
#
#r = Random()
#r.shuffle(xs)
#
#start = time.clock()
#xs = sorted(xs)

#----------------------------
# string
#----------------------------
#"""
#string.ascii_letters = string.ascii_lowercase + string.ascii_uppercase
#string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#string.digits = '0123456789'
#string.hexdigits = '0123456789abcdefABCDEF'
#"""

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

start = time.clock()

#"""
#find
#1000000	330.579883
#"""
#for i in xrange(n):
#  idx = t.find(search)

#"""
#in
#1000000	329.516237
#"""
#for i in xrange(n):
#  idx = search in t

#"""
#re
#1000000	689.246231
#"""
#for i in xrange(n):
#  m = re.search(search, t)
#  idx = m.start()

#"""
#re 事前にコンパイル
#1000000	695.375025
#"""
#p = re.compile(search)
#for i in xrange(n):
#  m = p.search(t)
#  idx = m.start()



end = time.clock()
print end - start
sys.exit(0)
