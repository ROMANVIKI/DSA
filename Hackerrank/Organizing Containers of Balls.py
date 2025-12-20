
import math
import os
import random
import re
import sys


def organizingContainers(container):
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()
