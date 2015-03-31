import sys
import time
import random
from random import Random
r = Random()

nums1 = range(190001, 200000)
nums2 = range(190001, 200000)
nums3 = range(1, 10001)
nums4 = range(1, 10001)
nums5 = range(10001, 190001)
nums6 = range(10001, 190001)
#r.shuffle(nums1)
#r.shuffle(nums2)
#r.shuffle(nums3)
#r.shuffle(nums4)
nums3.reverse()
nums4.reverse()
r.shuffle(nums5)
r.shuffle(nums6)

hv = ['H', 'V']

print ""

for i in xrange(200000):
  m = i % 2
  if i < 10000:
    r = i % 4
    if r == 0:
      n = nums1.pop()
    elif r == 1:
      n = nums2.pop()
    elif r == 2:
      n = nums3.pop()
    else:
      n = nums4.pop()
  else:
    n = nums5.pop() if m == 0 else nums6.pop()
  print "%s %d" % ( hv[m], n )

#print "V 1"
