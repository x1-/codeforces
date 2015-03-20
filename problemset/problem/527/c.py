import sys

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

    output
8
4
4
2
"""

dt = { 'H': [], 'V': [] }

sizes = map(int, raw_input().split())
n = sizes[2]

for x in xrange(n):
  (k, v) = raw_input().split()
  dt[k].append( int(v) )
  dt[k] = sorted( dt[k], reverse=True )

  hs = [sizes[1]] + dt['H'] + [0]
  hdiffs = [ hs[i] - hs[i+1] for i in xrange(len(hs)-1) ]
  maxh = max(hdiffs)

  vs = [sizes[0]] + dt['V'] + [0]
  vdiffs = [ vs[i] - vs[i+1] for i in xrange(len(vs)-1) ]
  maxv = max(vdiffs)

  print maxh * maxv
