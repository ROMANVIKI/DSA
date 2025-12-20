class Solution:

    def maxSubarraySumCircular(self, nums):
        max_sum = nums[0]
        min_sum = nums[0]
        curr_max_sum = nums[0]
        curr_min_sum = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            curr_max_sum = max(curr_max_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_max_sum)

            curr_min_sum = min(curr_min_sum + nums[i], nums[i])
            min_sum = min(min_sum, curr_min_sum)

            total += nums[i]

        circularSum = total - min_sum
        if circularSum == 0:
            return max_sum
        return max(max_sum, circularSum)


sol = Solution()
print(sol.maxSubarraySumCircular(nums=[1, -2, 3, -2]))
print(sol.maxSubarraySumCircular(nums=[-3, -2, -3]))
print(sol.maxSubarraySumCircular(nums=[5, -3, 5]))
