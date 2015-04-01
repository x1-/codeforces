import sys
#import time
from array import array

"""
search greater than zero
"""
def search_gt_zero(xs, start, end, step, ignores):
  i = start
  while(True):
    if step < 0 and i < end:
      i = end
      break
    if step > 0 and i > end:
      i = end
      break
    if ignores.has_key(i):
      i = ignores[i] + step
      continue
    if xs[i] > 0:
      break
    if start == end:
      break
    i = i + step
  return i


"""
search max range
"""
def search_max( poses, n ):

  s = sorted( poses )
  si = { s[-1]: n }
  f_mita = {}
  b_mita = {}

  max_df = 0
  for x in xrange(n):
    si[s[x]] = x
    diff = s[x+1] - s[x]
    max_df = max(diff, max_df)

  mxes = array('I', [0 for _ in xrange(n)])
  mxes[n-1] = max_df

  low  = s[1]
  high = s[-2]

  thh = int(n/3)

  for x in xrange(n-1, 0, -1):
    pos = poses[x]
    i = si[pos]

    f = low
    fp = 0
    if pos > low:
      fp = search_gt_zero(s, i-1, si[low], -1, f_mita)
      f = s[fp]


    b = high
    bp = n
    if pos < high:
      bp = search_gt_zero(s, i+1, si[high], 1, b_mita)
      b = s[bp]

    if pos == low:
      low = b
      f = 0
    if pos == high:
      high = f
      b = s[-1]

    df = b - f
    max_df = max(df, max_df)
    mxes[x-1] = max_df

    f_mita[bp-1] = fp+1
    b_mita[fp+1] = bp-1
    s[i] = 0

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

#start = time.clock()

sizes = map(int, raw_input().split())

a = [None] * sizes[2]
t = array('c', [' ' for _ in xrange(sizes[2])])

sV = array('I', [0 for _ in xrange(sizes[0]+1)])
sH = array('I', [0 for _ in xrange(sizes[1]+1)])

N = sizes[2]

# collect inputs
nv = 1
nh = 1
for x in xrange(N):
  (k, v) = raw_input().split()

  t[x] = k
  n = int(v)
  a[x] = n
  if k == 'V':
    sV[nv] = n
    nv += 1
  else:
    sH[nh] = n
    nh += 1

sV = sV[0:nv+1]
sH = sH[0:nh+1]

sV[nv] = sizes[0]
sH[nh] = sizes[1]

# create max ranges
diffsV = search_max( sV, nv )
diffsH = search_max( sH, nh )

# calculate h x w
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
sys.exit(0)
