def factorial(n):
    assert n >= 0 and int(n) == n, 'the num should be a positive integer'
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-10))


