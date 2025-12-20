#!/bin/python3

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    repeats = n // len(s)
    remainder = n % len(s)

    a_count_in_remainder = s[:remainder].count('a') 

    total = repeats * s.count('a') + a_count_in_remainder

    return total
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
