from types import coroutine


def count_vowels(curr_str):
    vowels_dict = {"a", "e", "i", "o", "u"}
    vowels_count = 0
    for s in curr_str:
        if s in vowels_dict:
            vowels_count += 1
    return vowels_count


def findSubstring(s, k):
    max_vowels = 0
    result_substring = ""

    for i in range(len(s) - k + 1):
        print(i)
        substring = s[i : i + k]
        vowels_count = count_vowels(substring)
        if vowels_count > max_vowels:
            max_vowels = vowels_count
            result_substring = substring
    return result_substring if max_vowels > 0 else "Not found!"


sol = findSubstring(s="azerdii", k=5)
print(sol)
