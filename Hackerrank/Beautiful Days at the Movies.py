

def beautifulDays(i, j, k):
    # Write your code here
    beautiful_days_count  = 0
    for day in range(i, j+1):
        day_str  = str(day)
        reverse_str = day_str[::-1]
        reverse_int = int(reverse_str)

        n = (day - reverse_int) / k
        if n % 1 == 0:
            beautiful_days_count += 1


    return beautiful_days_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
