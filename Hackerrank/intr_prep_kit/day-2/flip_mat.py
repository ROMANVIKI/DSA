#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
# 1               q = 1
# 2               n = 2
# 112 42 83 119   matrix = [[112, 42, 83, 119], [56, 125, 56, 49], \
# 56 125 56 49              [15, 78, 101, 43], [62, 98, 114, 108]]
# 15 78 101 43
# 62 98 114 108

# To create this group for all elements in the upper-left
# quadrant, use 2 for loops.
#
# groups = [] for x in range(n): for y in range(n):
# groups.append([matrix[x][y], matrix[2*n-1-x][y],
# matrix[x][2*n-1-y],
# matrix[2*n-1-x][2*n-1-y]])
#
# Then loop through groups to find max of each list, and sum them up


def flippingMatrix(matrix, n):
    groups = []
    for x in range(n):
        for y in range(n):
            groups.append(
                [
                    matrix[x][y],
                    matrix[2 * n - 1 - x][y],
                    matrix[x][2 * n - 1 - y],
                    matrix[2 * n - 1 - x][2 * n - 1 - y],
                ]
            )

    sol = 0
    for arr in groups:
        sol += max(arr)
    return f"{groups} - groups -- the sol {sol}"


if __name__ == "__main__":

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix, n)

        print(result)
