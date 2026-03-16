def findMedian(arr):
    arr = sorted(arr)
    return arr[round(len(arr) // 2)]


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
    print(result)

    # fptr.write(str(result) + "\n")
    #
    # fptr.close()
