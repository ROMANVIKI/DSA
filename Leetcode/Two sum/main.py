# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (i != j and nums[i] + nums[j] == target):
#                     return [i, j]
#         return []



def twoSum( nums: list[int], target: int) -> list[int]:
    dict={}
    for i,n in enumerate(nums):
        if n in dict:
            return dict[n],i
        else:
            dict[target-n]=i


if __name__ == "__main__":
    twoSum(nums = [2,7,11,15], target = 9)
#please upvote me it would encourage me alot


# Example 1:

# Input: nums = [2,7,11,15],target = 9 
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
