#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import sys
import time
import random
from random import Random

"""
引数で指定された値以下の数値をランダムに出力します。
出力する個数は指定された数値の数です。
"""
r = Random()

size = int(sys.argv[1]) if len(sys.argv) > 1 else input()


nums = range(1, size+1)
r.shuffle(nums)

for x in nums:
  print "%d" % ( x )
