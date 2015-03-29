import sys
#import time
from array import array

def incr_dict( dt, key ):
  if key == 1:
    return dt

  v = dt.setdefault( key, 0 )
  dt[key] += 1
  return dt

def decr_dict( dt, key ):
  if dt[key] == 1:
    del dt[key]
  else:
    dt[key] -= 1
  return dt

"""
    C. Glass Carving
    time limit per test2 seconds
    memory limit per test256 megabytes
    inputstandard input
    outputstandard output

    input1:
4 3 4
H 2
V 2
V 3
V 1

    output1:
8
4
4
2
    input2:
7 6 5
H 4
V 3
V 5
H 2
V 1
    output2:
28
16
12
6
4

    input3:
15 5 10
V 13
V 10
V 3
H 2
V 9
V 7
V 2
H 1
V 4
H 3
    output3:
65
50
35
21
18
12
12
12
9
6
"""

sizes = map(int, raw_input().split())

#start = time.clock()

a = array('I', [0 for _ in xrange(sizes[2])])
t = array('c', [' ' for _ in xrange(sizes[2])])

dtV = array('B', [0 for _ in xrange(sizes[0]+1)])
dtV[0] = 1
dtV[sizes[0]] = 1
dtH = array('B', [0 for _ in xrange(sizes[1]+1)])
dtH[0] = 1
dtH[sizes[1]] = 1

setV = {sizes[0]: 1, 1: 1}
setH = {sizes[1]: 1, 1: 1}

N = sizes[2]

for x in xrange(N):
  (k, v) = raw_input().split()

  t[x] = k
  a[x] = int(v)

# ----------------------------------------------------------
for x in xrange(N):

  pos = a[x]

  f = 1
  b = 1
  if t[x] == 'V':
    while( True ):
      if dtV[pos-f] == 1:
        break
      f += 1
    while( True ):
      if dtV[pos+b] == 1:
        break
      b += 1
    dtV[pos] = 1

    decr_dict( setV, b + f )
    incr_dict( setV, f )
    incr_dict( setV, b )
  else:
    while( True ):
      if dtH[pos-f] == 1:
        break
      f += 1

    while( True ):
      if dtH[pos+b] == 1:
        break
      b += 1
    dtH[pos] = 1

    decr_dict( setH, b + f )
    incr_dict( setH, f )
    incr_dict( setH, b )

  a[x] = max(setH.keys()) * max(setV.keys())

#end = time.clock()

for ans in a:
  print ans

#print end - start
