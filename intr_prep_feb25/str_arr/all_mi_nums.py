class Solution:
    def findDisappearedNumbers(self, nums):
        set_nums = set(nums)
        sol_arr = []
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                sol_arr.append(i)
        return sol_arr


sol = Solution()
print(sol.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))

# the nums list before the loop [4, 3, 2, 7, 8, 2, 3, 1]
# the nums list after the first loop [-4, -3, -2, -7, 8, 2, -3, -1]
# [5, 6]
