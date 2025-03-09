class Solution:
    # My first bruteforce solution which is not optimal sol
    def missingNumber(self, nums):
        for i in range(0, len(nums) + 1):
            if i in nums:
                continue
            else:
                return i

    def missingNumber1(self, nums):
        return sum(range(len(nums) + 1)) - sum(nums)


sol = Solution()
print(sol.missingNumber1(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
