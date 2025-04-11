class Solution:
    def countSymmetricIntegers(self, low, high):
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left, right = s[:mid], s[mid:]
                if sum(map(int, left)) == sum(map(int, right)):

                    count += 1

        return count


sol = Solution()
print(sol.countSymmetricIntegers(low=1200, high=1230))
