
def saveThePrisoner(n, m, s):
    # Write your code here
    remainder = (m - 1) % n # (10 - 1) % 7  = 2
    
    start_position = (s - 1 + remainder) % n + 1 # (2 - 1 + 2) % 7 + 1 =
    
    return start_position
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)
        
        print(result)
    #     fptr.write(str(result) + '\n')

    # fptr.close()
