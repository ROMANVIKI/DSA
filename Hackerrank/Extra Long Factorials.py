
def extraLongFactorials(n):
    # Write your code here
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

if __name__ == '__main__':
    n = int(input().strip())

    result = extraLongFactorials(n)
    print(result)