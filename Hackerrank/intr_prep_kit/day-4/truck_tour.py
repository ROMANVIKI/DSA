def truckTour(petrolpumps):
    # Write your code here
    print(petrolpumps)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    #
