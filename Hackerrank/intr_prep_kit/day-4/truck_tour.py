def truckTour(petrolpumps):
    start_ind = 0
    curr_tank = 0
    total_tank = 0

    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        total_tank += petrol - distance
        curr_tank += petrol - distance

        if curr_tank < 0:
            start_ind = i + 1
            curr_tank = 0
    return start_ind


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    #
