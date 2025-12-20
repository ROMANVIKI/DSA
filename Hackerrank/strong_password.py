#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    count_of_existence = 0

    has_digits = any(char in numbers for char in password)
    has_lower_case = any(char in lower_case for char in password)
    has_upper_case = any(char in upper_case for char in password)
    has_special_characters = any(char in special_characters for char in password)


    if not has_digits:
        count_of_existence += 1

    if not has_lower_case:
        count_of_existence += 1

    if not has_upper_case:
        count_of_existence += 1

    if not has_special_characters:
        count_of_existence += 1
        
    result = max(count_of_existence, 6-n)
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
    #fptr.write(str(answer) + '\n')

   # fptr.close()
