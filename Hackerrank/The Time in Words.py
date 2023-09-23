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
#h




def timeInWords(h, m):
    num_to_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    # Write your code here1
    if m == 0:
        return num_to_words[h] + "0' clock"
    elif m == 15:
        return "quarter past" + num_to_words[h]
    elif m == 30:
        return "half past" + num_to_words[h]
    elif m == 45:
        return "quarter to " + num_to_words[(h+1) % 12]
    elif m == 1:
        return "one minute past " + num_to_words[h]
    elif m == 59:
        return "one minute to " + num_to_words[(h+1) % 12]


    if m <= 20:
        if m == 1:
            minute_str = "minute"
        else:
            minute_str = "minutes"

        return num_to_words[m] + ' ' + minute_str + "past" + num_to_words[h]

    elif m < 30:
        return "twenty " + num_to_words[m-20] + "minute past" + num_to_words[h]
    else:
        if 60 - m == 1:
            minute_str = "minute"
        else:
            minute_str = "minutes"
        return num_to_words[60 - m] + " " + minute_str + " to " + num_to_words[(h+1) % 12]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
