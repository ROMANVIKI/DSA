#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
def minimumBribes(q):
    count = 0

    # Check if the queue is too chaotic
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:  # If a person has moved more than 2 positions forward
            print("Too chaotic")
            return

    # Count bribes by checking how many times a person has been overtaken
    for i in range(len(q)):
        # A person at index `i` could have started at `q[i]`, but they cannot have moved
        # more than 2 places ahead, so we only need to check the range max(0, q[i] - 2) to `i`
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:  # If someone in front has a larger number, they bribed q[i]
                count += 1

    print(count)


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
