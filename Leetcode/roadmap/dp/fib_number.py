def fib_func(num):
    count = 1
    current_val = 0
    if num >= 0:
        current_val += num - count
    return current_val


class Solution:
    def fib(self, n: int) -> int:
        total = 0
        for num in range(n + 1):
            total += fib_func(num) 


        return total




sol = Solution()

print(sol.fib(n=2))
