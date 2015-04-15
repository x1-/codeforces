import sys
import time

"""
"""
n = input()
ds = list(raw_input())

start = time.clock()

quoter = n / 4

#print "n/2", max_split
#print "p1: %d, p2: %d" % (p1, p2)
res = 'no'
for i in xrange(quoter):
  ok = True
  for j in xrange(4):
    pos = i + j * quoter
    print pos, ds[pos]
    if ds[pos] == '.':
      ok = False
      break
  if ok:
    res = 'yes'
    break

end = time.clock()
#print end - start

print res
sys.exit(0)
