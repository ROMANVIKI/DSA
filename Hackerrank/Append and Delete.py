def appendAndDelete(s, t, k):
    common_length = 0
    
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            break
        common_length += 1
    
    total_operations = len(s) + len(t) - 2 * common_length
    
    if total_operations <= k and (total_operations % 2 == k % 2 or len(s) + len(t) < k):
        return "Yes"
    else:
        return "No"

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)
    
    print(result)

    
