def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    original_alph = "abcdefghijklmnopqrstuvwxyz"
    alt_alph = original_alph[k:] + original_alph[:k]

    dic_alph = {}
    for index, char in enumerate(original_alph):
        dic_alph[char] = alt_alph[index]

    result = ""
    for char in s:
        if char.lower() in dic_alph:
            if char.isupper():
                result += dic_alph[char.lower()].upper()
            else:
                result += dic_alph[char.lower()]
        else:
            result += char
    return result


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)

    # fptr.write(result + "\n")
    #
    # fptr.close()


# 11
# middle-Outz
# 2
#
# okffng-Qwvb
#
#
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab
#
# m -> o
# i -> k
# d -> f
# d -> f
# l -> n
# e -> g
# -    -
# O -> Q
# u -> w
# t -> v
# z -> b
