#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
# h


def timeInWords(h, m):
    num_to_words = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "quarter",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
    ]
    time_dict = {"half": 30}
    # Write your code here1
    if m == 0:
        return f"{num_to_words[h]} o' clock"
    elif m == time_dict["half"]:
        return f"half past {num_to_words[h]}"
    elif m > time_dict["half"]:
        if num_to_words[60 - m] == "quarter":
            return f"quarter to {num_to_words[h+1]}"
        return f"{num_to_words[60-m]} minutes to {num_to_words[h+1]}"
    elif m < time_dict["half"]:
        if m == 15:
            return f"{num_to_words[m]} past {num_to_words[h]}"
        elif m > 1:
            return f"{num_to_words[m]} minutes past {num_to_words[h]}"
        else:
            return f"{num_to_words[m]} minute past {num_to_words[h]}"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
