def introTutorial(V, arr):
    # Write your code here
    len_arr = len(arr)
    arr = sorted(arr)
    for i, char in enumerate(arr):
        if char == V:
            return i


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    #
