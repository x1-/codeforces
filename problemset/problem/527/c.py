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
"""

sizes = map(int, raw_input().split())

dt = { 'H': [sizes[1], 0], 'V': [sizes[0], 0] }
diffs = { 'H': [sizes[1]], 'V': [sizes[0]] }


for x in xrange(sizes[2]):
  (k, v) = raw_input().split()
  pos = int(v)

  if len(dt[k]) > 2 and pos > dt[k][1]:
    dt[k][1:1].insert( 0, pos )
    diffs[k].insert( 1, pos - dt[k][1] )
    diffs[k][0] = dt[k][0] - pos
  elif len(dt[k]) > 2 and dt[k][-2] > pos:
    dt[k].insert( -1,  pos )
    diffs[k].insert( -2, dt[k][-2] - pos )
    diffs[k][-1] = pos
  else:
    dt[k].append( pos )
    dt[k] = sorted( dt[k], reverse=True )
    diffs[k] = [ dt[k][i] - dt[k][i+1] for i in xrange(len(dt[k])-1) ]


  print max(diffs['H']) * max(diffs['V'])

