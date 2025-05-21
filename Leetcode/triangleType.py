class Solution:
    def triangleType(self, nums):
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return None
        elif nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"

        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        return "scalene"


sol = Solution()
# print(sol.triangleType(nums=[3, 4, 5]))
print(sol.triangleType(nums=[3, 3, 3]))
# print(sol.triangleType(nums=[3, 3, 5]))
