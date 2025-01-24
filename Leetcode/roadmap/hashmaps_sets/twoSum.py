def twoSum(target, nums):
    diff_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in diff_map:
            return [diff_map[diff], i]
        diff_map[num] = i
    return []


# Test the function
target = 9
nums = [2, 7, 11, 15]
sol = twoSum(target, nums)
print(sol)  # Output: [0, 1]
