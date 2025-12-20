#!/bin/python3

import math
import os
import random
import re
import sys




def angryProfessor(k, a):
    # Write your code here
    no_students = 0
    print(a)
    for i in range(len(a)):
        if a[i] == 0 or a[i] < 0:
            no_students += 1
        else:
            n = ''
    if no_students == k or no_students > k:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)

        
