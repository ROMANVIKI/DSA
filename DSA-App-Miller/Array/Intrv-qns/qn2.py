def findPairs(nums, t):
    # for i in range(len(nums)):
    #     for j in range(1, len(nums)):
    #         if nums[i] + nums[j] == t:
    #             return i, j

    i, j = 0, 1
    while j < len(nums):
        if nums[i] + nums[j] == t:
            return i, j
        else:
            j += 1


print(findPairs(nums=[1, 2, 3, 4, 5, 6], t=6))
