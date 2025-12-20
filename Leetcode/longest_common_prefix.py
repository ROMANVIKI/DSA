def longestCommonPrefix(str):
    common_strs = ''
    for i in range(len(str) - 1):
        if str[i][0] == str[i+1][0] and str[i+2][0]:
            return True


strs = ["flower", "flow", "flight"]


print(longestCommonPrefix(str=strs))
