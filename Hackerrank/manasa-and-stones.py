#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    possible_values = set()
    for t in range(0, n):
        v = t * a + (n - 1 - t) * b
        possible_values.add(v)
    sorted_possible_values = sorted(possible_values)
    return sorted_possible_values

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(result)
    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()
