
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#



def aVeryBigSum(ar):
    total_sum = 0
    for num in ar:
        total_sum += num
    return total_sum

print(
aVeryBigSum(ar=[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))