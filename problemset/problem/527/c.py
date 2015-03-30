import sys
#import time
from array import array


def max_diff( poses, n ):
  mx = 0
  s = sorted( poses )
  for x in xrange(n):
    diff = s[x+1] - s[x]
    mx = max(diff, mx)

  return mx


def search_max( poses, bits, n ):
  max_df = max_diff( poses, n )
  mxes = array('I', [0 for _ in xrange(n)])
  mxes[n-1] = max_df

  for x in xrange(n-1, 0, -1):
    pos = poses[x]

    f = 1
    b = 1

    bits[pos] = 0

    while( True ):
      if bits[pos-f] == 1:
        break
      f += 1
    while( True ):
      if bits[pos+b] == 1:
        break
      b += 1

    max_df = max(f+b, max_df)
    mxes[x-1] = max_df

  return mxes


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

sV = array('I', [0 for _ in xrange(sizes[0]+1)])
sH = array('I', [0 for _ in xrange(sizes[1]+1)])

N = sizes[2]
nv = 1
nh = 1
for x in xrange(N):
  (k, v) = raw_input().split()

  t[x] = k
  n = int(v)
  a[x] = n
  if k == 'V':
    dtV[n] = 1
    sV[nv] = n
    nv += 1
  else:
    dtH[n] = 1
    sH[nh] = n
    nh += 1

sV = sV[0:nv+1]
sH = sH[0:nh+1]

sV[nv] = sizes[0]
sH[nh] = sizes[1]

diffsV = search_max( sV, dtV, nv )
diffsH = search_max( sH, dtH, nh )

nv = 0
nh = 0
for x in xrange(N):
  k = t[x]
  if k == 'V':
    nv += 1
  else:
    nh += 1
  a[x] = diffsV[nv] * diffsH[nh]

#end = time.clock()

for ans in a:
  print ans

#print end - start
