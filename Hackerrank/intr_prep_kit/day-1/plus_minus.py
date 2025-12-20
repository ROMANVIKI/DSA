#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    el_count = len(arr)
    dic = {"neg": 0, "pos": 0, "zero": 0}
    for num in arr:
        if num < 0:
            dic["neg"] += 1
        elif num > 0:
            dic["pos"] += 1
        elif num == 0:
            dic["zero"] += 1
    for k in dic:
        result = dic[k] / el_count
        print(f"{result:.6f}")


if __name__ == "__main__":
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr=[1, 1, 0, -1, -1]))
