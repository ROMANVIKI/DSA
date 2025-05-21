def romanToInt(s):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "CM": 900,
        "CD": 400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4,
    }

    sol_num = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i : i + 2] in roman_dict:
            sol_num += roman_dict[s[i : i + 2]]
            i += 2
        else:
            sol_num += roman_dict[s[i]]
            i += 1
    return sol_num


print(romanToInt(s="MCMXCIV"))


# Symbol       Value
# I             2
# V             5
# X             20
# L             50
# C             200
# D             500
# M             2000
#

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Input: s = "MCMXCIV"
# Output: 2994
# Explanation: M = 2000, CM = 900, XC = 90 and IV = 4.
