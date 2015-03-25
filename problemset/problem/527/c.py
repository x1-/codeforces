import sys
import time
import bisect
from array import array

def search( xs, target ):
  high = len(xs)-1
  low = 1
  idx = high/2

  if target < xs[low]:
    return low
  elif target > xs[high-1]:
    return high

  while(low<high):
    if xs[idx] > target and target > xs[idx-1]:
      break
    elif target > xs[idx]:
      low = idx + 1
    elif target < xs[idx]:
      high = idx - 1

    idx = (high + low)/2

  return idx

def incr_dict( dt, key ):
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

dt   =  { 'H': array('I', [0, sizes[1]]), 'V': array('I', [0, sizes[0]]) }
sets =  { 'H': {sizes[1]: 1}, 'V': {sizes[0]: 1} }

for x in xrange(sizes[2]):
  (k, v) = raw_input().split()

  pos = int(v)

  idx = bisect.bisect_left(dt[k], pos, lo=1, hi=len(dt[k])-1)

  diff1 = dt[k][idx] - pos
  diff2 = pos - dt[k][idx-1]
  diff = diff1 + diff2

  dt[k].insert( idx, pos )

  decr_dict( sets[k], diff )
  incr_dict( sets[k], diff1 )
  incr_dict( sets[k], diff2 )

  print max(sets['H'].keys()) * max(sets['V'].keys())

#end = time.clock()
#print end - start
