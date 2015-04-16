import sys
import time

n = input()
ds = list(raw_input())

start = time.clock()

q = n / 4
res = 'no'

for i in xrange(n):

  for j in xrange(4, 6):
    quoter = n / j
    fall = False
    count = 0

    for k in xrange(i, n, quoter):
      #print k, ds[k]
      if ds[k] == '*':
        count += 1
      else:
        fall = True
        break

    if count == 4 and not fall:
      res = 'yes'
      break

  if res == 'yes':
    break

end = time.clock()
#print end - start

print res
sys.exit(0)
