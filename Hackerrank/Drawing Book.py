
def pageCount(n, p):
    # Write your code here
    pages_front = p // 2
    
    pages_back = (n//2) - (p//2)
    
    return min(pages_front, pages_back)
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
