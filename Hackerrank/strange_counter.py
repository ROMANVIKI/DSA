#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    cycle_start = 1
    initial_value = 3

    while t >= cycle_start + initial_value:
        cycle_start += initial_value
        initial_value *= 2

    time_offset = t - cycle_start
    counter_value = initial_value - time_offset
    return counter_value

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
