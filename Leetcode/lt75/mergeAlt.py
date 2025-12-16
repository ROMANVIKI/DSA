class Solution:
    def mergeAlternately(self, word1, word2):
        # my brute force solution ------->>>>>>
        i, j = 0, 0
        max_len_str = max(len(word1), len(word2))
        result_str = ""
        while i <= max_len_str or j <= max_len_str:
            try:
                result_str += word1[i]
                i += 1
            except IndexError:
                i += 1
                pass
            try:
                result_str += word2[j]
                j += 1
            except IndexError:
                j += 1
                pass
        return result_str

        # Leetcode Solution
        # n = min(len(word1), len(word2))
        # result_str = []
        # for i in range(n):
        #     result_str.append(word1[i])
        #     result_str.append(word2[i])
        # result_str.append(word1[n:])
        # result_str.append(word2[n:])
        # return "".join(result_str)


sol = Solution()
print(sol.mergeAlternately(word1="abc", word2="pqr"))
print(sol.mergeAlternately(word1="abcd", word2="pq"))
