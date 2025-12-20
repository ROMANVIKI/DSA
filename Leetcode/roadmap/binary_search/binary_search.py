def search(nums, target):
    ind = 0
    while ind <= len(nums):
        if nums[ind] == target:
            return ind
        ind += 1
    return -1    
print(search(nums=[-1,0,3,5,9,12], target=9))
