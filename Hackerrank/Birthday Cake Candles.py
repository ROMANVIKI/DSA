#!/bin/python3

import math
import os
import random
import re
import sys

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



def birthdayCakeCandles(candles, candles_count):
    max_num = []
    candles = quicksort(candles)
    print(candles)
    if candles[candles_count-1] == candles[candles_count-2]:
        max_num = [candles[candles_count-1]]
        max_num.append(candles[candles_count-2])
        print(len(max_num))
    # Write your code here

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles, candles_count)

    
