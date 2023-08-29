
def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumulative_likes = 0

    for day in range(1, n+1):
        liked_today = shared // 2
        cumulative_likes += liked_today
        shared = liked_today * 3
    return cumulative_likes

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
