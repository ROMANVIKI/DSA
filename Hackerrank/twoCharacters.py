# Complete the 'alternate' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.


def alternate(s):
    max_length = 0
    distinct_chars = set(s)

    for char1 in distinct_chars:
        for char2 in distinct_chars:
            if char1 != char2:
                filtered = [ch for ch in s if ch == char1 or ch == char2]

                is_alternating = True
                for i in range(1, len(filtered)):
                    if filtered[i] == filtered[i - 1]:
                        is_alternating = False
                        break
                if is_alternating:
                    max_length = max(max_length, len(filtered))

    return max_length


sol = alternate(s="beabeefeab")
print(sol)


# if __name__ == "__main__":
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     l = int(input().strip())
#
#     s = input()
#
#     result = alternate(s)
#     print(result)
#
#     # fptr.write(str(result) + '\n')
#     #
#     # fptr.close()
