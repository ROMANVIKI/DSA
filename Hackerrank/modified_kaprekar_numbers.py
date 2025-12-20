#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def is_kaprekar_number(n):
    if n == 1:
        return True
    squared = n * n
    str_sq = str(squared)
    for i in range(1, len(str_sq)):
        left = int(str_sq[:i]) if str_sq[:i] else 0
        right = int(str_sq[i:]) if str_sq[:i] else 0
        if right != 0:
            if left + right == n:
                return True
    return False

def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar_numbers = []
    for i in range(p, q+1):
        if is_kaprekar_number(i):
            kaprekar_numbers.append(i)

    for num in kaprekar_numbers:
        return num 

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    print(kaprekarNumbers(p, q))
