class Solution:
    def maxSubArray(self, nums):
        max_arr = nums[0]
        curr_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_arr = max(max_arr, curr_max)
        return max_arr


sol = Solution()
print(sol.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
