class Solution:
    # Input: n = 3
    # Output: 3
    # Explanation: There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step
    def climbStairs(self, n):
        count = 1
        ones = n // 1
        twos = n // 2
        return f"count: {count} 1s: {ones} 2s: {twos}"


sol = Solution()
print(sol.climbStairs(n=8))
