import sys
import time
from array import array
import random
from random import Random

#start = time.clock()

n = int(sys.argv[1])

#"""
## list append
#100000	0.027873
#1000000	0.260543
#10000000	2.558889
#"""
##xs = []
##for i in xrange(n):
##  xs.append(i)
# 
#"""
#for
#100000	0.015099
#1000000	0.14847
#10000000	1.42081
#"""
##xs = [i for i in xrange(n)]
# 
#"""
#[None]
#100000	0.016606
#1000000	0.179783
#10000000	1.727175
#"""
##xs = [None] * n
##for i in xrange(n):
##  xs[i]
# 
#"""
#[None] only
#100000	0.000724
#1000000	0.006474
#10000000	0.071949
#"""
#xs = [None] * n

#"""
#[None]
#100000	0.000803
#1000000	0.006982
#10000000	0.074916
#"""
#xs = [0] * n

#"""
#array
#100000	0.018191
#1000000	0.164888
#10000000	1.853745
#"""
#xs = array('I', [ 0 for _ in xrange(n) ])

#"""
#array
#100000	0.024631
#1000000	0.232682
#10000000	2.49165
#"""
#xs = array('I', [ i for i in xrange(n) ])

r = Random()
xs = [i for i in xrange(n)]

nums = range(1, size+1)
r.shuffle(nums)


# random read
start = time.clock()

end = time.clock()
print end - start
sys.exit(0)
