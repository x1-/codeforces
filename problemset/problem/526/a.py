import sys
import time

n = input()
ds = list(raw_input() + "*")

start = time.clock()

res = 'no'

for i in xrange(n-3):

  q = (n-i) / 4
  #if q <= i:
  #  break
  for j in xrange(q, q+i+1):
    fall = False
    count = 0
    for k in xrange(i, n+1, j):
      print k, ds[k]
      if ds[k] == '*':
        count += 1
      else:
        fall = True
        break

    if count == 5 and not fall:
      res = 'yes'
      break
  if res == 'yes':
    break

end = time.clock()
#print end - start

print res
sys.exit(0)
