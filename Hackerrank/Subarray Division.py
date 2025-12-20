
#

def birthday(s, d, m):
    # Write your code here
    ways = 0 
    n = len(s)
    for i in range(n -m + 1):
        segment_sum = 0 
        for j in range(i, i + m):
            segment_sum += s[j]
            
        if segment_sum == d:
            ways += 1
    
    return ways
        

if __name__ == '__main__':
    

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)
