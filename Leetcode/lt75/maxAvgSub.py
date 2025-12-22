from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        max_sum = 0
        i = 0
        while i <= len(nums) / k + 1:
            sum_curr = sum(nums[i : i + k])
            if sum_curr > max_sum:
                max_sum = sum_curr
            i += 1
        return max_sum / k


sol = Solution()
print(sol.findMaxAverage(nums=[7, 4, 5, 8, 8, 3, 9, 8, 7, 6], k=7))
# print(sol.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
# print(sol.findMaxAverage(nums=[5], k=1))
