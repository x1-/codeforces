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
"X won" (the game is over, and X won)
"O won" (the game is over, and O won)
"Draw" (the game is over, and it ended in a draw)
"Game has not completed" (the game is not over yet)
"""
cases = int(raw_input())
n = cases * 5

tests = [None]*(cases*4)
ans = [None]*cases

c = 0
for i in xrange( n ):
  r = raw_input()
  if i % 5 == 4:
    continue

  tests[c] = list(r)
  c += 1

start = time.clock()

for i in xrange(cases):
  s = i * 4
  # rows
  tenth = tests[s:s+4]

  # cols
  for j in xrange(4):
    cols = []
    for k in xrange(4):
      cols.append( tenth[k][j] )
    tenth.append( cols )

  tenth.append( [
      tenth[0][0],
      tenth[1][1],
      tenth[2][2],
      tenth[3][3]
  ])
  tenth.append( [
      tenth[0][3],
      tenth[1][2],
      tenth[2][1],
      tenth[3][0]
  ])

  ans[i] = judge(tenth)

end = time.clock()
print end - start

for i in xrange(cases):
  print "Case #%d: %s" % (i+1, ans[i])

sys.exit(0)
