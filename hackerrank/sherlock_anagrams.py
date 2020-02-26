#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for x in range(1, len(s)):
        for i in range(0, len(s) - x):
            for j in range(i + 1, len(s) - x + 1):
                # print(f'x={x},i={i}, j={j}')
                s1 = sorted(s[i:i+x])
                s2 = sorted(s[j:j+x])
                # print(f'{s1} = {s2}')
                if s1 == s2:
                    count += 1

    # print(count)
    return count

if __name__ == '__main__':
    # sherlockAndAnagrams('mom')
    # sherlockAndAnagrams('abba')
    # sherlockAndAnagrams('abcd')
    # sherlockAndAnagrams('ifailuhkqq')
    # sherlockAndAnagrams('kkkk')
    # sherlockAndAnagrams('cdcd')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
