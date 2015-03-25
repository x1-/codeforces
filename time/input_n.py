import sys
import time

"""
import heapq

size = int( raw_input() )
start = time.clock()

h = {'H':[], 'V':[]}
for x in xrange(size):
  (k, v) = raw_input().split()
  h[k].append(v)
  heapq.heappush(h[k], v)

#sorted(h['H'], reverse=True)
#sorted(h['V'], reverse=True)

#print max(h['H'])
#print max(h['V'])

print heapq.nlargest(1, h['H'])
print heapq.nlargest(1, h['V'])

end = time.clock()
print end - start

"""

import random
from random import Random
r = Random()

size = input()

nums = range(1, size)
r.shuffle(nums)

hv = ['H', 'V']

print "2 %d %d" % ( size, size - 1 )

for n in nums:
  print "H %d" % ( n )

print "V 1"
