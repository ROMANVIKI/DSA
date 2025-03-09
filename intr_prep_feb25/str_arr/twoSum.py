class Solution:
    # my bruteforce sol
    def twoSum(self, nums, t):
        s, e = 0, 1
        while s < len(nums):
            if nums[s] + nums[e] == t:
                return [s, e]
            else:
                s += 1
                e += 1

    def optTwoSum(self, nums, t):
        num_hashMap = {}
        n = len(nums)

        for i in range(n):
            complement = t - nums[i]
            if complement in num_hashMap:
                return [num_hashMap[complement], i]
            num_hashMap[nums[i]] = i
        return []


sol = Solution()
print(sol.optTwoSum(nums=[2, 7, 11, 15], t=9))
