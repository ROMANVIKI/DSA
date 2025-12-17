class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            if str1 > str2:
                return str1[: len(str1) - len(str2)]
            else:
                return str2[: len(str2) - len(str1)]
        return ""


sol = Solution()
# print(sol.gcdOfStrings(str1="ABCABC", str2="ABC"))
# print(sol.gcdOfStrings(str1="LEET", str2="CODE"))
# print(sol.gcdOfStrings(str1="ABABAB", str2="ABAB"))
print(
    sol.gcdOfStrings(
        str1="CXTXNCXTXNCXTXNCXTXNCXTXN",
        str2="CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN",
    )
)
