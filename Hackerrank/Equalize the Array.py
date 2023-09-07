

def equalizeArray(arr):
    # Write your code here
    dict  = {}
    for num in arr:
        if num in dict:
            dict[num] += 1

        else:
            dict[num] = 1
    max_freq = max(dict.values())
    min_dl = len(arr) - max_freq

    return min_dl, dict
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
