class Solution:
    def smallerNumberThanCurrent(self, nums):
        sor_nums = sorted(nums)

        nums_dict = {}
        for i, num in enumerate(sor_nums):
            if num not in nums_dict:
                nums_dict[num] = i
        retr = []
        for i in nums:
            retr.append(nums_dict[i])
        return retr


sol = Solution()
print(sol.smallerNumberThanCurrent(nums=[8, 1, 2, 2, 3]))
