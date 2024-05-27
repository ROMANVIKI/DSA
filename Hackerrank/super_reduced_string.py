def super_reduced_string(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if not stack:
        return "Empty String"
    else:
        return ''.join(stack)

# Example usage
if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    print(super_reduced_string(s))  # Output: "abd"
