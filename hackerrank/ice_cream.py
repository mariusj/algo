#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    n = len(cost)
    cc = dict()
    for i in range(n - 1, -1, -1):
        if cost[i] in cc:
            cc[cost[i]].append(i + 1)
        else:
            cc[cost[i]] = [i+1]
    for i in range(0, n - 1):
        m = money - cost[i]
        if m in cc:
            arr = cc[m]
            for j in arr:
                if i + 1 != j:
                    print(f"{i + 1} {j}")
                    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
