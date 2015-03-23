import sys
import time

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

start = time.clock()

dt =    { 'H': [sizes[1], 0], 'V': [sizes[0], 0] }
diffs = { 'H': [sizes[1]], 'V': [sizes[0]] }
#diffs = { 'H': sizes[1], 'V': sizes[0] }
ct =    { 'H': 2, 'V': 2 }

for x in xrange(sizes[2]):
  (k, v) = raw_input().split()
  pos = int(v)

  if ct[k] > 2 and pos > dt[k][1]:
    diffs[k].insert( 1, pos - dt[k][1] )
    diffs[k][0] = dt[k][0] - pos
    dt[k].insert( 1, pos )
  elif ct[k] > 2 and dt[k][-2] > pos:
    diffs[k].insert( -1, dt[k][-2] - pos )
    diffs[k][-1] = pos
    dt[k].insert( -1,  pos )
  else:
    for i in xrange(ct[k]-1):
      if pos > dt[k][i+1] and pos < dt[k][i]:
        diffs[k][i] = dt[k][i] - pos
        diffs[k].insert( i+1, pos - dt[k][i+1] )
        dt[k].insert( i+1, pos )
        break

  ct[k] += 1

  print dt
  print diffs

  print max(diffs['H']) * max(diffs['V'])

end = time.clock()
print end - start
