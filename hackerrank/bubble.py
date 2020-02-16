#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    n = len(a)
    for i in range(0, n):
        for j in range(0, n-1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
