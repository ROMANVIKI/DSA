def summaryChanges(nums):
    ans = []
    i = 0

    while i < len(nums):
        start = nums[i]

        while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
            i += 1

        if start != nums[i]:
            ans.append(f"{start}->{nums[i]}")

        else:
            ans.append(f"{start}")

        i += 1

    return ans


new = summaryChanges([0, 1, 2, 4, 5, 7])

print(new)
