import sys
import time
from array import array

"""
A. Puzzles
time limit per test1 second
memory limit per test256 megabytes

n, m(2<=n<=m<=50)
f1,f2,...,fm(4<=fi<=1000)

#input1:
4 6
10 12 10 7 5 22

#output1:
5
"""
nm     = map(int, raw_input().split())
pieces = array('I', [ int(x) for x in raw_input().split() ])

#start = time.clock()

n = nm[1] - nm[0] + 1
spieces = sorted( pieces, reverse=True )
min_diff = spieces[0] - spieces[nm[0]-1]

for i in xrange(n):
  diff = spieces[i] - spieces[i+nm[0]-1]
  if diff < min_diff:
    min_diff = diff

#end = time.clock()
#print end - start

print min_diff
sys.exit(0)
