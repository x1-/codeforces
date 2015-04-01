import sys
import time

"""
in = int( raw_input() )
start = time.clock()

end = time.clock()
print end - start
"""

import random
from random import Random
r = Random()

size = int(sys.argv[1]) if len(sys.argv) > 1 else input()


nums = range(1, size+1)
r.shuffle(nums)

print "%d %d" % ( size, size )
print " ".join(map(str, nums))
