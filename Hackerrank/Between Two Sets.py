def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def get_factors(arr):
    factors = set()
    for num in arr:
        for i in range(1, num + 1):
            if num % i == 0:
                factors.add(i)
    return factors

def getTotalX(a, b):
    lcm_a = 1
    gcd_b = b[0]
    
    for num in a:
        lcm_a = lcm(lcm_a, num)
    
    for num in b[1:]:
        gcd_b = gcd(gcd_b, num)
    
    count = 0
    
    for i in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % i == 0:
            count += 1
    
    return count

# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Call the function and print the result
result = getTotalX(a, b)
print(result)
