#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jumps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER flagHeight
#  2. INTEGER bigJump
#

def jumps(flagHeight, bigJump):
    # Write your code here
    # print(flagHeight)
    # print(bigJump)
    if flagHeight == bigJump:
        return 0

    elif flagHeight % bigJump == 0:
        return int(flagHeight / bigJump)

    else:
        # print(flagHeight%bigJump)
        return flagHeight // bigJump + (flagHeight % bigJump)


if __name__ == '__main__':
    flagHeight = int(input().strip())

    bigJump = int(input().strip())

    print(jumps(flagHeight, bigJump))
