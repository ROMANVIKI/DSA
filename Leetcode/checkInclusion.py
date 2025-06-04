class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm_str = s1[::-1]
        n = len(s1)
        if perm_str in s2:
            return True
        return False


sol = Solution()
print(sol.checkInclusion(s1="ab", s2="eidbaooo"))
print(sol.checkInclusion(s1="ab", s2="eidboaoo"))
print(sol.checkInclusion(s1="a", s2="ab"))
print(sol.checkInclusion(s1="adc", s2="dcda"))
