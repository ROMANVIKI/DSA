#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades, grades_count):
    for i in range(grades_count):
        if grades[i] < 38:
            # For grades less than 38, no rounding occurs, so we keep them as they are.
            pass
        else:
            # Round up the grade to the nearest multiple of 5 if the difference is less than 3.
            remainder = grades[i] % 5
            if remainder >= 3:
                grades[i] += 5 - remainder

    return grades


if __name__ == '__main__':
 

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades, grades_count)
    print(result)

