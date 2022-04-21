#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    col = [[] for i in range(n)]
    res = []
    lastanswer = 0
    for q in queries:
        data = (q[1] ^ lastanswer) % n
        if q[0] == 1:
            col[data].append(q[2])
        elif q[0] == 2:
            ind_x = q[2] % len(col[data])
            lastanswer = col[data][ind_x]
            res.append(lastanswer)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()