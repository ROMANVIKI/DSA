#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def quick_sort(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def pickingNumbers(a):
    # Write your code here
    a = quick_sort(a)
    start = 0 
    end = 0
    maxLength = 0
    while end < len(a):
        if abs(a[end] - a[start]) <= 1:
            maxLength = max(maxLength, end - start +1)
            end += 1
        else:
            start += 1
    return maxLength

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()






































































