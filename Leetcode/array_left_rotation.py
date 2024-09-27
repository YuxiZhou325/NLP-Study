#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    alist = list(arr)
    rotated_list = alist[d:] + alist[:d]
    """
    when d is 4
    [d:] is 5
    [:d] is [1, 2, 3, 4] means element 1 to the dth element (without 0th element)
    """
    return rotated_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
