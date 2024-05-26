#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    loaves_given = 0
     
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            loaves_given += 2

    if B[-1] % 2 != 0:
        return 'NO'
    
    return loaves_given
        




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
