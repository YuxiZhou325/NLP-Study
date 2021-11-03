#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#
import collections


def getMinimumDifference(a, b):
    # Here is my solution
    ans = []
    if len(a) != len(b):
        ans.append(-1)
        return ans
    else:
        for i in range(len(a)):
            count = 0
            if len(a[i]) != len(b[i]):
                ans.append(-1)
            else:
                record = collections.Counter(a[i])
                for c in b[i]:
                    if c in record:
                        if record[c]:
                            record[c] -= 1
                        else:
                            count += 1
                    else:
                        count += 1
                ans.append(count)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ[''], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    result = getMinimumDifference(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
