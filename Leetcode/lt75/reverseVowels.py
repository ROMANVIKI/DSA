class Solution:
    def reverseVowels(self, s: str) -> str:
        seen = set("aeiouAEIOU")
        i, j = 0, len(s) - 1
        str_list = []
        for char in s:
            str_list.append(char)
        while i < j:
            if str_list[i] in seen:
                if str_list[j] in seen:
                    str_list[i], str_list[j] = str_list[j], str_list[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            elif str_list[j] in seen:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(str_list)


sol = Solution()
print(sol.reverseVowels(s="IceCreAm"))
