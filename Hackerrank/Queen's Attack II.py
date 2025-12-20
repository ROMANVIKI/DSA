#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.     
# - int n: the number of rows and columns in the board
# - nt k: the number of obstacles on the board
# - int r_q: the row number of the queen's position
# - int c_q: the column number of the queen's position
# - int obstacles[k][2]: each element is an array of 2 integers, the row and column of an obstacle 

# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    return n, k, r_q, c_q, obstacles

if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

