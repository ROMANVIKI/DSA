def twosum(nums, target):
    h_map = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in h_map:
            return [h_map[complement], i]
        h_map[nums[i]] = i

    return []


sol = twosum(nums=[1, 3, 7, 9, 2], target=11)
print(sol)
