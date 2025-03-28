#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    initial_sum = sum(int(num) for num in n) * k

    if initial_sum < 10:
        return initial_sum
    return superDigit(str(initial_sum), 1)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()
    #
    # n = first_multiple_input[0]
    #
    # k = int(first_multiple_input[1])

    result = superDigit(n="9875", k=4)
    print(result)

    # fptr.write(str(result) + '\n')

# fptr.close()
