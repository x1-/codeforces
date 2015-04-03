import sys
import time

"""
"""
f = raw_input()
s = raw_input()

#start = time.clock()

if f == s:
  print 'No such string'
  sys.exit(0)

les = list('abcdefghijklmnopqrstuvwxyz')
pos = { les[i]: i for i in xrange(len(les)) }

fl = list(f)
f2 = list(fl)
up = 1

for i in xrange(len(fl)-1, -1, -1):
  if up == 1:
    if pos[fl[i]] == 25:
      fi = 0
    else:
      fi = pos[fl[i]] + 1
      up = 0
    f2[i] = les[fi]
  else:
    f2[i] = fl[i]

ff = "".join(f2)
if s > ff and up == 0:
  print ff
else:
  print 'No such string'

#end = time.clock()
#print end - start
sys.exit(0)
