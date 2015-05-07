#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
import time
import string
import re
import random
from random import Random
from array import array

n = int(sys.argv[1])

#----------------------------
# append
#----------------------------
start = time.clock()

"""
# list append
1000000	0.156414
"""
xs = []
for i in xrange(n):
  xs.append(i)

"""
for
1000000	0.0876
"""
xs = [i for i in xrange(n)]

"""
[None]
1000000	0.099896
"""
xs = [None] * n
for i in xrange(n):
  xs[i]

"""
[None] only
1000000	0.005255
"""
xs = [None] * n

"""
[0]
1000000	0.005359
"""
xs = [0] * n

"""
array
1000000	0.108973
"""
xs = array('I', [ 0 for _ in xrange(n) ])

"""
array
1000000	0.149061
"""
xs = array('I', [ i for i in xrange(n) ])

#----------------------------
# random read
#----------------------------
r = Random()
ix = [i for i in xrange(n)]
r.shuffle(ix)

nay = [i for i in xrange(n)]
iay = array('I', [ i for i in xrange(n) ])
bay = array('b', [ 1 for _ in xrange(n) ])

start = time.clock()

"""
list
10000000	0.367742
"""
tmp = 0
for i in ix:
  tmp = nay[i]

"""
array
10000000	0.263049
"""
tmp = 0
for i in ix:
  tmp = iay[i]

"""
1byte array
10000000	0.232178
"""
tmp = 0
for i in ix:
  tmp = bay[i]

#----------------------------
# pop
#----------------------------
nay = [i for i in xrange(n)]
iay = array('I', [i for i in xrange(n)])

start = time.clock()

"""
list
10000000	0.205749
"""
for i in xrange(n):
  nay.pop()

"""
array
10000000	0.302395
"""
for i in xrange(n):
  iay.pop()

#----------------------------
# pop(0)
#----------------------------
nay = [i for i in xrange(n)]
iay = array('I', [i for i in xrange(n)])

start = time.clock()

"""
list
10000000	182.47865
"""
for i in xrange(n):
  nay.pop(0)

"""
array
10000000	85.623589
"""
for i in xrange(n):
  iay.pop(0)

#----------------------------
# insert(0)
#----------------------------
nay = []
iay = array('I', [])

start = time.clock()

"""
list
1000000	241.515497
"""
for i in xrange(n):
  nay.insert(0, i)

"""
array
1000000	86.058389
"""
for i in xrange(n):
  iay.insert(0, i)

#----------------------------
# sort
#----------------------------
r = Random()
nay = [i for i in xrange(n)]
iay = array('I', [ i for i in xrange(n) ])

start = time.clock()

"""
list
1000000	1.13676
"""
r.shuffle(nay)
xs = sorted(nay)

"""
array
1000000	1.127885
"""
r.shuffle(iay)
xs = sorted(iay)

#----------------------------
# string
#----------------------------
"""
string.ascii_letters = string.ascii_lowercase + string.ascii_uppercase
string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits = '0123456789'
string.hexdigits = '0123456789abcdefABCDEF'
"""

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


"""
find
1000000	322.414854
"""
for i in xrange(n):
  idx = t.find(search)

"""
in
1000000	314.847081
"""
for i in xrange(n):
  idx = search in t

"""
re
1000000	674.792997
"""
for i in xrange(n):
  m = re.search(search, t)
  idx = m.start()

"""
re 事前にコンパイル
1000000	674.394229
"""
p = re.compile(search)
for i in xrange(n):
  m = p.search(t)
  idx = m.start()


#----------------------------
# raw_input & print
#----------------------------
start = time.clock()
"""
raw_input で 標準入力を受け取りながら出力
1000000	3.504401
"""
for i in xrange(n):
  x = int(raw_input()) / 10
  print x

"""
結果をバッファリング
1000000	3.268692
"""
res = []
for i in xrange(n):
  res.append( int(raw_input()) / 10 )
for i in res:
  print i

"""
raw_input で 標準入力をすべて受け取ってから出力
1000000	3.22516
"""
xs = [ int(raw_input()) for _ in xrange(n) ]
for i in xs:
  x = i / 10
  print x

"""
raw_input で 標準入力をすべて受け取りバッファリングした結果を出力
1000000	3.125762
"""
xs = [ int(raw_input()) / 10 for _ in xrange(n) ]
for i in xs:
  print i

end = time.clock()
print end - start
sys.exit(0)
