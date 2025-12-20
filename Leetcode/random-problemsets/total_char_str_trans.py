def lengthAfterTransformation(s, t, nums):
    alpha_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    rev_alpha = {v:k for k, v in alpha_dict.items()}
    sol_str = [] 

    for i in range(t):
        for k in s:
            original_pos = alpha_dict[k]
            shift = nums[original_pos]
            new_pos = (original_pos + shift) % 26
            sol_str.append(rev_alpha[new_pos])

    return ''.join(sol_str)


print(lengthAfterTransformation(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
