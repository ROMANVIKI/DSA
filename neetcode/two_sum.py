class Solution:
    def twoSum(self, nums, target):
        prev_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i


sol = Solution()
print(sol.twoSum(nums=[4, 5, 6], target=10))
