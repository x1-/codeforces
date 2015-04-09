import sys
import time

def judge(board):
  res = 'Draw'
  for t in board:
    st = set(t)
    if len( st ) == 2:
      if 'T' in st and 'X' in st:
        res = 'X won'
        break
      elif 'T' in st and 'O' in st:
        res = 'O won'
        break
    elif len( st ) == 1:
      if 'X' in st:
        res = 'X won'
        break
      elif 'O' in st:
        res = 'O won'
        break
    if '.' in st:
      res = 'Game has not completed'

  return res


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

print tests
start = time.clock()

res = 'YES'

for x in xrange(cases):
  (n, m, test ) = tests[x]
  for i in xrange(n):
    f = test[i][0]
    for j in xrange(1,m):
      cell = test[i][j]
      print i, j
      print f, cell
      if cell != f and i == n-1:
        print "cell != f and i == n-1"
        res = 'NO'
        break
      elif cell != f and i < n-1:
        if test[i+1][j] != cell:
          print "test[i+1][j] != cell"
          res = 'NO'
          break

end = time.clock()
print end - start

for i in xrange(cases):
  print "Case #%d: %s" % (i+1, ans[i])

sys.exit(0)
