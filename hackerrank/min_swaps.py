#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # print(arr)
    swaps = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr)):
            if arr[i] != i + 1:
                e = arr[i]
                arr[i] = arr[e - 1]
                arr[e - 1] = e
                swaps += 1
                swapped = True
            # print(arr)
    # print(arr)
    # print(swaps)
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    # arr = [7, 1, 3, 2, 4, 5, 6]
    # arr = [4, 3, 1, 2]
    # arr = [2,3,4,1,5]
    # arr = [1,3,5,2,4,6,7]
    # arr = [2,31,1,38,29,5,44,6,12,18,39,9,48,49,13,11,7,27,14,33,50,21,46,23,15,26,8,47,40,3,32,22,34,42,16,41,24,10,4,28,36,30,37,35,20,17,45,43,25,19]

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
