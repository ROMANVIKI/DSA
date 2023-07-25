#!/bin/python3
from quicksort_algorithm import quicksort
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code 
    arr = quicksort(arr)
    min = 0
    max = 0
    for i in range(1,len(arr)):
        max = arr[i] + max
    for j in range(len(arr)-1):
        min = arr[j] + min
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
