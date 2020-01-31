#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
  count = 0
  for i, v in enumerate(q):
    if v == i + 2:
      count += 1
    if v == i + 3:
      count += 2
    if v > i + 3:
      count = -1
      break
  if count == -1:
    print("Too chaotic")
  else:
    print(count)
  

if __name__ == '__main__':
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
    1 2 3 4 5 6 7 8
    1 2 3 5 4 6 7 8
    1 2 5 3 4 6 7 8
    1 2 5 3 4 7 6 8
    1 2 5 3 7 4 6 8
    1 2 5 3 7 4 8 6
    1 2 5 3 7 8 4 6
    1 2 5 3 7 8 6 4
    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

    #     q = list(map(int, input().rstrip().split()))

    #     minimumBribes(q)
