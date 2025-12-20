class Solution:
    def refineStr(self, s):
        ref_str = ""
        is_space = False
        i = 0
        for char in s:
            if char == " " and not is_space:
                if ref_str[-1] != " ":
                    ref_str += char
                    is_space = True
            elif char != " ":
                ref_str += char
                is_space = False
        return ref_str

    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = self.refineStr(s).strip()

        revrs_str = ""
        i = len(s) - 1
        r, l = 0, 0
        is_space = False
        while i >= 0:
            if s[i] != " " and not is_space:
                r = i
                i -= 1
            elif s[i] == " ":
                is_space = True
                revrs_str += " "
                l = i + 1
                revrs_str += s[l:r]
                i -= 1
        return revrs_str


sol = Solution()
print(sol.reverseWords(s="  hello world  "))
# print(sol.reverseWords(s="a good   example"))
