ransomNote = "aa"
magazine = "aab"


def canConstruct():
    counter = {}
    for c in magazine:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1

    for c in ransomNote:
        if c in counter and counter[c] > 0:
            counter[c] -= 1
        else:
            return False

    return True


sol = canConstruct()

print(sol)
