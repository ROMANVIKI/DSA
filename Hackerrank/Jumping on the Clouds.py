

def jumpingOnClouds(c):
    # Write your code here
    step = 0
    for i in range(len(c)):
        try:
            if c[i+2] == 0 or c[i+1] == 0:
                step += 1
        except IndexError:
            step = step
    return step
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
