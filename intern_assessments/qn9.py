def stringRepeat(chars):
    char_dict = {}
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    for unique_char in char_dict:
        if char_dict[unique_char] == 1:
            return unique_char


sol = stringRepeat(chars="swiss")
print(sol)
