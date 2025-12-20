#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    total = 0
    elements = set(arr)

    for number in arr:
        if (number + d in elements) and (number + 2 * d in elements):
            total += 1
    return total
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)
    # fptr.write(str(result) + '\n')
    print(result)
    #
    # fptr.close()

