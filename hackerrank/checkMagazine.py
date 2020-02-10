#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
  magazine_dict = dict.fromkeys(magazine, 0)
  for m in magazine:
    magazine_dict[m] += 1
  for n in note:    
    if n in magazine_dict:
      magazine_dict[n] -= 1
      if magazine_dict[n] == 0:
        del magazine_dict[n]
    else:
      print('No')
      return
  print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
