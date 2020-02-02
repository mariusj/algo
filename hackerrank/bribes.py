#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
  count = 0
  qq = [ x for x in range(1, len(q) + 1)]
  for i, v in enumerate(q):
    if (q[i] == qq[i]):
      # print("%d no change" % i)
      continue
    elif (i < len(q) - 1 and q[i] == qq[i + 1]):
      count += 1
      qq[i + 1] = qq[i]
      qq[i] = q[i]
      # print("%d ch 1 " % i)
      # print(qq)
    elif (i < len(q) - 2 and q[i] == qq[i + 2]):
      count += 2
      qq[i + 2] = qq[i + 1]
      qq[i + 1] = qq[i]
      qq[i] = q[i]
      # print("%d ch 2 " % i)
      # print(qq)
    else:
      print("Too chaotic")
      return

  print(count)
  

if __name__ == '__main__':
    # minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
    # minimumBribes([2, 1, 5, 3, 4])
    # minimumBribes([2, 5, 1, 3, 4])
    # 1 2 3 4 5 6 7 8
    # 1 2 3 5 4 6 7 8
    # 1 2 5 3 4 6 7 8
    # 1 2 5 3 4 7 6 8
    # 1 2 5 3 7 4 6 8
    # 1 2 5 3 7 4 8 6
    # 1 2 5 3 7 8 4 6
    # 1 2 5 3 7 8 6 4

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
