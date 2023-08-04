import math
import os
import random
import re
import sys

# 5 4 7
# 1 2 3 4
# 7 8 9 10
# 13 14 15 16
# 19 20 21 22
# 25 26 27 28

def matrixRotation(matrix, r):

    print(r)
    print(matrix)
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
