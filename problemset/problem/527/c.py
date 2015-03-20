import sys

"""
    C. Glass Carving
    time limit per test2 seconds
    memory limit per test256 megabytes
    inputstandard input
    outputstandard output

    input1:
4 3 4
H 2
V 2
V 3
V 1

    output
8
4
4
2
"""

#hs = [0,2,3]
#vs = [0,2,3,1,4]

hs = []
vs = []

sizes = list(raw_input())
print sizes
counter=sizes(2)

while counter==0:
  s = list(raw_input())
  if s[0] == "H":
    hs.append.append(s[1])
    hs = sorted(hs, reverse=True)
  elif s[0] == "V":
    vs.append.append(s[1])
    vs = sorted(vs, reverse=True)

  hs2 = [0] + hs + [size[1]]
  hdiffs = [ hs2[i] - hs2[i+1] for i in xrange(len(hs2)-1) ]
  maxh = max(hdiffs)

  vs2 = [0] + hv + [size[0]]
  vdiffs = [ vs2[i] - vs2[i+1] for i in xrange(len(vs2)-1) ]
  maxv = max(vdiffs)

  print maxh * maxv
  counter-=1
