#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cip_alphabet = alphabet[k:] + alphabet[:k]
    sol = ""
    cip_dict = {}
    for ind, val in enumerate(alphabet):
        cip_dict[val] = cip_alphabet[ind]

    for crr_str in s:
        if crr_str.isalpha():
            if crr_str.isupper():
                sol += cip_dict[crr_str.lower()].upper()
            else:
                sol += cip_dict[crr_str]
        else:
            sol += crr_str

    return sol


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()
