#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict1 = dict.fromkeys(a + b, 0)
    for aa in a:
        dict1[aa] += 1
    for bb in b:
        dict1[bb] -= 1
    count = 0
    for v in dict1.values():
        count += abs(v)
    #print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
