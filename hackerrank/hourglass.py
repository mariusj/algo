#!/bin/python3

import math
import os
import random
import re
import sys

def hsum(arr, x, y):
    sum = arr[y][x] + arr[y][x+1] + arr[y][x+2]
    sum += arr[y+1][x+1]
    sum += arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
    return sum

# Complete the hourglassSum function below.
def hourglassSum(arr):
    m = - sys.maxsize - 1
    for y in range(0, 4):
        for x in range(0, 4):
            s = hsum(arr, x, y)
            if s > m:
                m = s
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
