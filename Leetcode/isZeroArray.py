def isZeroArray(nums, queries):
    diff = [0] * (len(nums) + 1)
    for l, r in queries:
        print(l, r)
        diff[l] += 1
        if r + 1 < len(nums):
            diff[r + 1] -= 1
    cnt = 0
    for i in range(len(nums)):
        cnt += diff[i]
        if nums[i] > cnt:
            return False
    return True


print(isZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3], [0, 2]]))
print(isZeroArray(nums=[1, 0, 1], queries=[[0, 2]]))
print(isZeroArray(nums=[2], queries=[[0, 0], [0, 0]]))
