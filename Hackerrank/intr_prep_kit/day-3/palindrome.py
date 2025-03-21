#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def palindromeIndex(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:  # Found mismatch
            # Check if removing left index makes it a palindrome
            if s[left + 1 : right + 1] == s[left + 1 : right + 1][::-1]:
                return left
            # Check if removing right index makes it a palindrome
            if s[left:right] == s[left:right][::-1]:
                return right
            return -1  # No single removal can make it a palindrome

        left += 1
        right -= 1

    return -1  # Already a palindrome


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)

    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
