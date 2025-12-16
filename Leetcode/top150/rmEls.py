from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        match_count = 0
        for i in range(len(nums)):
            if nums[i] - val == 0:
                match_count += 1
                nums[i] = "_"
        print(match_count)
        print(sorted(nums))
        return len(nums) - match_count


sol = Solution()
print(sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
