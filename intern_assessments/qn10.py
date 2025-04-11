def programCheck(inp):
    stack = []
    mapping = {")": "("}

    for char in inp:
        if char in mapping.values():  # opening brackets
            stack.append(char)
        elif char in mapping:  # closing brackets
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack  # stack should be empty if balanced


print(sol)

sol = programCheck(inp="(())")
