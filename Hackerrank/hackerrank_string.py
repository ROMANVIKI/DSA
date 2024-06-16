

def hackerrankInString(s):
    # Write your code here
    target = 'hackerrank'
    target_index = 0

    for char in s:
        if char == target[target_index]:
            target_index += 1
        
        if target_index == len(target):
            return "YES"
        
    return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()
