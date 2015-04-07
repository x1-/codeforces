import sys
import time

"""
"""
f = raw_input()
s = raw_input()

#start = time.clock()

les = list('abcdefghijklmnopqrstuvwxyz')
ues = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ldc = dict( zip( les, ues ) )
udc = dict( zip( ues, les ) )

ss = {}
for x in list(s):
  if ss.has_key(x):
    ss[x] += 1
  else:
    ss[x] = 1

fl = sorted(list(f))
n  = len(fl)
sl = [None] * n
sn = n - 1

yay = 0
wps = 0

# yay
for i in xrange(n):
  x = fl.pop()
  if ss.has_key(x) and ss[x] > 0:
    ss[x] -= 1
    yay += 1
  else:
    sl[sn] = x
    sn -= 1

# woops
n  = len(sl)
for i in xrange(n):
  x = sl.pop()
  if x is None:
    break

  xc = ldc[x] if ldc.has_key(x) else udc[x]
  if ss.has_key(xc) and ss[xc] > 0:
    ss[xc] -= 1
    wps += 1

print yay, wps

#end = time.clock()
#print end - start
sys.exit(0)
