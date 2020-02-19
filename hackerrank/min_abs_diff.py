#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    mindif = pow(10, 9)
    arr.sort()
    for i in range(0, len(arr) - 1):
        d = abs(arr[i] - arr[i + 1])
        if d < mindif:
            mindif = d
    # print(mindif)
    return mindif

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    # arr = [random.randrange(-1000000000, 1000000001) for x in range(0, pow(10, 5))]

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
