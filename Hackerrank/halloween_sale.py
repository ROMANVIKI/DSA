# p = 20
# d = 3
# m = 6
# s = 80

def howManyGames(p, d, m, s):
    count = 0
    while s >= p:   
        s-=p
        count += 1
        p = max(p - d, m)
        print(p)
    print(count)    


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    # fptr.write(str(answer) + '\n')

    # fptr.close()

# p - intial price
# d - dollars less than prev price
# m - less than or equal to this value 
# s - budget