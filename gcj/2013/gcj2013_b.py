import sys
import time

"""
Case #1: YES
Case #2: NO
Case #3: YES
"""
cases = int(raw_input())

tests = [None]*cases
ans = [None]*cases

c = 0
while( True ):
  n, m = map(int, raw_input().split())

  xs = [None]*n
  for i in xrange( n ):
    xs[i] = raw_input().split()

  tests[c] = (n, m, xs)
  c += 1
  if c == cases:
    break

start = time.clock()


for x in xrange(cases):
  res = 'YES'
  (n, m, test ) = tests[x]
  if n == 1 or m == 1:
    ans[x] = res
    continue

  for j in xrange(m):
    cell = test[0][j]
    f = test[0][j-1] if j > 0 else cell
    u = test[1][j]

    if j == 0:
      if cell < u and cell < test[0][1]:
        res = 'NO'
        break
    elif j == m-1:
      if cell < f and cell < test[1][j]:
        res = 'NO'
        break

    if cell < f and cell < u:
      res = 'NO'
      break

  if res == 'NO':
    ans[x] = res
    continue

  for j in xrange(m):
    cell = test[n-1][j]
    f = test[n-1][j-1] if j > 0 else cell
    b = test[n-2][j]

    if j == 0:
      if cell < b and cell < test[n-1][0]:
        res = 'NO'
        break
    elif j == m-1:
      #print "i:%s, j;%s" % (n-1, j)
      #print "f:%s, c;%s" % (f, cell)
      if cell < f and cell < test[n-2][j]:
        res = 'NO'
        break
      if cell > f and f < test[n-2][j-1]:
        res = 'NO'
        break

    if cell < f and cell < b:
      res = 'NO'
      break

  if res == 'NO':
    ans[x] = res
    continue

  for i in xrange(1, n-1):
    for j in xrange(m):

      #print i, j
      cell = test[i][j]
      f = test[i][j-1] if j > 0 else cell
      u = test[i+1][j]
      b = test[i-1][j]

      if j == 0:
        if cell < test[i][1] and ( cell < u or cell < b ):
          res = 'NO'
          break
#      elif j == m-1:
#        if cell > test[i][j-1] and ( test[i][j-1] ):
#          res = 'NO'
#          break

      if cell < f:
        if cell < u or cell < b:
          #print "cell", i, j, cell
          #print "no", f, u, b
          res = 'NO'
          break
        else:
          if cell < test[0][j] or cell < test[n-1][j]:
            res = 'NO'
            break

#      if cell != f:
#        check = i-1 if i == n-1 else i+1
##        if i == 1:
#        print "check2:", cell, test[check][j]
#        if cell != test[check][j]:
#          print "no"
#          res = 'NO'
#          break
#      f = test[i][j]
  ans[x] = res

end = time.clock()
print end - start

for i in xrange(cases):
  print "Case #%d: %s" % (i+1, ans[i])

sys.exit(0)
