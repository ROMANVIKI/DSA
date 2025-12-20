def findDigits(n):
    # Write your code here
    str_n = str(n)
    digit = 0
    for i in str_n:
        try:
            if n % int(i) == 0:
                digit += 1
        except ZeroDivisionError:
            digit = digit
    return digit

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)
