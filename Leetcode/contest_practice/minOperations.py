class Solution:
    def minOperations(self, nums, k):
        return sum(nums) % k


sol = Solution()
print(sol.minOperations(nums=[19], k=10))  # 9
