def funnyString(s):
    # Write your code here
    return s


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)

    #     fptr.write(result + '\n')
    #
    # fptr.close()
    #
