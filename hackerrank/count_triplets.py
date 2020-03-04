#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    cnt1 = dict()
    cnt2 = dict()
    for i in range(len(arr) - 1, -1, -1):
        a = arr[i]
        b = a * r
        c = b * r

        if b in cnt2:
            count += cnt2[b]

        if b in cnt1:
            if a in cnt2:
                cnt2[a] = cnt2[a] + cnt1[b]
            else:
                cnt2[a] = cnt1[b]

        if a in cnt1:
            cnt1[a] = cnt1[a] + 1
        else:
            cnt1[a] = 1

    # print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    # arr = [1,4,16,64]
    # r = 4

    # arr = [1,2,2,4]
    # r = 2

    # arr=[1, 3, 9, 9, 27, 81]
    # r = 3
    
    # arr = [1, 5, 5, 25, 125]
    # r = 5

    # arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # r = 1

    # arr = []
    # r=  1
    # for i in range(0, 100000):
    #     arr.append(1237)

    # arr = [1, 2, 1, 2, 4]
    # r = 2

    # arr = [1,1,1]
    # r = 1

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
