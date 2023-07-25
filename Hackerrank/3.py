# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonal_sum_right = 0
    diagonal_sum_left = 0

    for i in range(len(arr)):
        diagonal_sum_right += arr[i][i]
        diagonal_sum_left += arr[i][len(arr) - i - 1]

    diagonal_diff = abs(diagonal_sum_right - diagonal_sum_left)
    return diagonal_diff

# 11 2 4
# 4 5 6
# 10 8 -12

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)

print(result)