def flatlandSpaceStations(n, c):
    return 0


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
