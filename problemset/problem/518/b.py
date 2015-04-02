import sys
import time

"""
"""
f = raw_input()
s = raw_input()

#start = time.clock()

ss = set([ x for x in list(f) ])

sl = list(s)

yay = 0
wps = 0

for x in sl:
  if x in ss:
    yay += 1
  else:
    wps += 1

print yay, wps

#end = time.clock()
#print end - start
sys.exit(0)
