#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    brackets = dict()
    brackets["{"] = "}"
    brackets["["] = "]"
    brackets["("] = ")"
    stack = []
    for c in s:
        if c in brackets.keys():
            stack.append(brackets[c])
        else:
            if len(stack) == 0 or stack.pop() != c:
                return "NO"
    if len(stack) == 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        #print(result)

        fptr.write(result + '\n')

    fptr.close()
