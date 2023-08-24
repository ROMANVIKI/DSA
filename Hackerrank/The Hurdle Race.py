
def hurdleRace(k, height):
    # Write your code here
    max = height[0]
    for i in height:
        if i > max:
            max = i
    if max > k:
        
        return max - k
    else:
        return 0
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
