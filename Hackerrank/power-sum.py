def powerSum(X, N):
    def power_sum_recursive(X, N, num):
        # Calculate num^N
        value = num ** N
        if value > X:
            return 0
        if value == X:
            return 1
        
        # Recursively calculate without including num and including num
        return power_sum_recursive(X, N, num + 1) + power_sum_recursive(X - value, N, num + 1)
    
    # Start the recursion with the first number 1
    return power_sum_recursive(X, N, 1)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())
    N = int(input().strip())

    result = powerSum(X, N)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
