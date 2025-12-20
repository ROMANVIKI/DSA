#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    total_num_days_non_leap_yr = 243
    total_num_days_leap_yr = 244
    if year == 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
          print("gregorian leap year")
          no_days = 231
          day_of_programmer = 256 - no_days
          return f'{day_of_programmer}.09.{year}'
        else:
            no_days = 230
            day_of_programmer = 256 - no_days
            return f'{day_of_programmer}.09.{year}'
    elif year <= 1917:

        if year % 4 == 0 :
            no_days = total_num_days_leap_yr
            day_of_programmer  = 256 - no_days
            return f'{day_of_programmer}.09.{year}'
        else:
            no_days = total_num_days_non_leap_yr
            day_of_programmer = 256 - no_days
            return f'{day_of_programmer}.09.{year}'
    else:

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
          print("gregorian leap year")
          no_days = total_num_days_leap_yr
          day_of_programmer = 256 - no_days
          return f'{day_of_programmer}.09.{year}'
        else:
            no_days = total_num_days_non_leap_yr
            day_of_programmer = 256 - no_days
            return f'{day_of_programmer}.09.{year}'
            
    # Write your code here

if __name__ == '__main__':


    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)

