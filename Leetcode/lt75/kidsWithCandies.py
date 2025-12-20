from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        i = 0
        while i <= len(candies) - 1:
            if candies[i] + extraCandies >= max_val:
                candies[i] = True

            else:
                candies[i] = False
            i += 1
        return candies


sol = Solution()
print(sol.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
