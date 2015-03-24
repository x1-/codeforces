import sys
import time
import heapq

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

h = []
for i in [(7,15),(3, 22),(9, 4),(0, 4),(2, 15),(3, 16),(2, 2),(5, 6)]:
  heapq.heappush( h, i )

for i in xrange(len(h)):
  print heapq.heappop(h)

sys.exit
"""

sizes = map(int, raw_input().split())

#start = time.clock()

ct =    { 'H': sizes[2], 'V': sizes[2] }
dt =    { 'H': [], 'V': [] }
diffs = { 'H': [], 'V': [] }

heapq.heappush( dt['V'], 0 )
heapq.heappush( dt['V'], sizes[0] )
heapq.heappush( dt['H'], 0 )
heapq.heappush( dt['H'], sizes[1] )

heapq.heappush( diffs['V'], (sizes[2], sizes[0]) )
heapq.heappush( diffs['H'], (sizes[2], sizes[1]) )

for x in xrange(sizes[2]):
  (k, v) = raw_input().split()

  pos = int(v)
  heapq.heappush( dt[k], pos )

  dt[k] = [heapq.heappop(dt[k]) for i in xrange(len(dt[k]))]
  for i in xrange(len(dt[k])-2, 0, -1):
    if dt[k][i] == pos:
      diff1 = dt[k][i+1] - pos
      diff2 = pos - dt[k][i-1]
      diff = diff1 + diff2

      tmp = []
      for j in xrange(len(diffs[k])):
        x = heapq.heappop( diffs[k] )
        heapq.heappush( tmp, x )
        if x[1] == diff:
          heapq.heappush( tmp, (x[0]-1, diff1) )
          heapq.heappush( tmp, (x[0]-1, diff2) )
          ct[k] -= 1

      diffs[k] = tmp
#      for j in xrange(len(diffs[k])):
#        if diffs[k][j] == diff:
#          del diffs[k][j]
#          break

#      diffs[k].append( diff1 )
#      diffs[k].append( diff2 )
      break

#  print sorted(diffs['H'], reverse=True)[0] * sorted(diffs['V'], reverse=True)[0]

  print diffs
#  print sorted(diffs['H'], cmp=lambda x, y: x[0] < y[0] and x[1] > y[1])
#  print sorted(diffs['V'], cmp=lambda x, y: x[0] < y[0] and x[1] > y[1])

#end = time.clock()
#print end - start
