def marsExploration(s):
    # Write your code here
    og_char = int(len(s) / 3) * "SOS"
    i = 0
    count = 0
    while i < len(s):
        if s[i] != og_char[i]:
            count += 1
        i += 1
    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
