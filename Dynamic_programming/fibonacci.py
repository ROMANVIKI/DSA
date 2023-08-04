def fibonacci(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Create an array to store the solutions of subproblems
    dp = [0] * (n + 1)

    # Initialize the first two Fibonacci numbers
    dp[0] = 0
    dp[1] = 1

    # Compute the Fibonacci numbers from the bottom up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Test the function
n = 10
print("Fibonacci number at position", n, "is:", fibonacci(n))
