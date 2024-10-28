def serachInsert(nums, target):
    ind = 0
    while ind < len(nums):
        if nums[ind] == target:
            return ind
        elif nums[ind] > target:
            return ind - 1
        
        ind += 1

    return len(nums)    





print(serachInsert(nums=[1,3,5,6], target=5))
