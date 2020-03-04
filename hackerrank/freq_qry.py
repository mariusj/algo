#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    arr = dict()
    freq = dict()
    res = []
    for q in queries:
        op = q[0]
        v = q[1]
        if op == 1:            
            cnt = arr.setdefault(v, 0)
            arr[v] = cnt + 1
            if cnt > 0:
                freq[cnt].remove(v)
            freq.setdefault(cnt+1, [])
            freq[cnt+1].append(v)
        elif op == 2:
            cnt = arr.setdefault(v, 0)
            if cnt > 0:
                arr[v] = cnt - 1
                freq[cnt].remove(v)
                freq.setdefault(cnt-1, [])
                freq[cnt-1].append(v)
        elif op == 3:
            if v in freq and freq[v]:
                res.append(1)
            else:
                res.append(0)
        # print(f'arr={arr}')
        # print(f'freq={freq}')

    # print(res)
    return res

if __name__ == '__main__':
    # queries = [
    #     [1,  5],
    #     [1,  6],
    #     [3,  2],
    #     [1, 10],
    #     [1, 10],
    #     [1,  6],
    #     [2,  5],
    #     [3,  2]]

    # queries = [
    #     [3, 4],
    #     [2, 1003],
    #     [1, 16],
    #     [3, 1]
    # ]

    # queries = [
    #     [1, 3],
    #     [2, 3],
    #     [3, 2],
    #     [1, 4],
    #     [1, 5],
    #     [1, 5],
    #     [1, 4],
    #     [3, 2],
    #     [2, 4],
    #     [3, 2]
    # ]

    # queries = [ [1,1], [2,2], [3,2], [1,1], [1,1], [2,1], [3,2] ]

    # queries = []
    # ops = [1,2,3]
    # for i in range(0, 100000):
    #     op = random.choice(ops)
    #     if op == 3:
    #         val = random.randint(1, 10)
    #     else:
    #         val = random.randint(1, 1000000000)
    #     queries.append([op, val])

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
