def happyLadybugs(b, n):
    # Write your code here
    if n * "_" == b:
        return "YES"
    char_dict = {}
    for char in b:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    if "_" not in char_dict:
        print("hey")
        return "NO"
    for k in char_dict:
        if char_dict[k] > 1:
            continue
        elif char_dict[k] == "_":
            continue
        else:
            return "NO"
    return "YES"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b, n)
        print(result)

    #     fptr.write(result + '\n')
    #
    # fptr.close()
    #
