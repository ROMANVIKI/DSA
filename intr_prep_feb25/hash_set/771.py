class Solution:
    def numJewelsInStones(self, jewels, stones):
        count = 0
        s = set(jewels)
        for stone in stones:
            if stone in s:
                count += 1
        return count


sol = Solution()
print(sol.numJewelsInStones(jewels="ebd", stones="bbb"))
