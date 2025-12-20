#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr, n):
    # Write your code here
    lef_diag = 0
    right_diag = 0
    lef_count = 0
    rig_count = -1
    for s in arr:
        print(rig_count)
        lef_diag += s[lef_count]

        right_diag += s[rig_count]
        lef_count += 1
        rig_count -= 1
    return abs(lef_diag - right_diag)


if __name__ == "__main__":

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)
    print(result)
