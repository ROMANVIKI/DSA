def cutTheSticks(arr, arr2, n):
    result = []

    while arr:

        result.append(len(arr))

        min_length = min(arr)

        arr = [x - min_length for x in arr if x - min_length > 0]
    
    return result
if __name__ == '__main__':  
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    arr2 = [0]

    result = cutTheSticks(arr, arr2, n)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
