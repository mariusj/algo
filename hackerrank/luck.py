#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    important = []
    for c in contests:
        if c[1] == 1:
            important.append(c[0])
        else:
            luck += c[0]
    important.sort()
    wins = len(important) - k
    for i, c in enumerate(important):
        if i < wins:
            luck -= c
        else:
            luck += c
    #print(luck)
    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
