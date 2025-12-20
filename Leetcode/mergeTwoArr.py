def mergeTwoArr(word1, word2):
    sol_str = ''
    if len(word1) == 0 and len(word2):
        return ''
    m_len = max(len(word1), len(word2))
    for i in range(m_len):
        try:
            sol_str += word1[i]
        except IndexError:
            pass
        try:
            sol_str += word2[i]
        except IndexError:
            pass
    return sol_str



print(mergeTwoArr(word1 = "ab", word2 = "pqrs"))

# Output: "apbqrs"
