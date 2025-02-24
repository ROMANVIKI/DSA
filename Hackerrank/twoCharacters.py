# Complete the 'alternate' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

#
# def alternate(s):
#     max_length = 0
#     distinct_chars = set(s)
#
#     for char1 in distinct_chars:
#         for char2 in distinct_chars:
#             if char1 != char2:
#                 filtered = [ch for ch in s if ch == char1 or ch == char2]
#
#                 is_alternating = True
#                 for i in range(1, len(filtered)):
#                     if filtered[i] == filtered[i - 1]:
#                         is_alternating = False
#                         break
#                 if is_alternating:
#                     max_length = max(max_length, len(filtered))
#
#     return max_length
#
#
# sol = alternate(s="beabeefeab")
# print(sol)


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


def alternate(s):
    """
    Find the length of longest alternating sequence that can be formed using
    exactly two characters from the input string.

    Example:
    - Input: "beabeefeab"
    - Valid alternating sequences include: "babab" (using 'a' and 'b')
    - Return: 5 (length of "babab")
    """
    # Get all unique characters from the string
    unique_chars = set(s)
    max_length = 0

    # For each pair of unique characters
    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 >= char2:  # Skip duplicate pairs and same characters
                continue

            # Initialize variables for current sequence
            curr_length = 0
            last_char = None
            is_valid = True

            # Check each character in the original string
            for char in s:
                # If current character is one of our two chosen characters
                if char in (char1, char2):
                    # If it's the first character or different from last character
                    if last_char is None or char != last_char:
                        curr_length += 1
                        last_char = char
                    else:  # If same character appears consecutively
                        is_valid = False
                        break

            # Update max_length if current sequence is valid
            if is_valid and curr_length > max_length:
                max_length = curr_length

    return max_length


# Test the function
test_str = "beabeefeab"
result = alternate(test_str)
print(f"Input: {test_str}")
print(f"Longest alternating sequence length: {result}")
