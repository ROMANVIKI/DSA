# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr, n):
    # Write your code here
    initial_arr = [0] * 100
    for val in arr:
        initial_arr[val] += 1
    return initial_arr


if __name__ == "__main__":

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr, n)

    print(result)
