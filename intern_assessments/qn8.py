def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # only try to build sequence if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest


sol = longestConsecutive(nums=[100, 4, 200, 1, 3, 2])
print(sol)
