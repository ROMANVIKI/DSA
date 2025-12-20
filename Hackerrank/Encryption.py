import math

def encryption(s):
    # Remove spaces from the input string
    s = s.replace(" ", "")
    
    # Calculate the number of rows and columns
    length = len(s)
    rows = int(math.floor(math.sqrt(length)))
    columns = int(math.ceil(math.sqrt(length)))
    
    # Check if the number of rows and columns needs to be adjusted
    if rows * columns < length:
        rows += 1
    
    # Create the grid
    grid = []
    for i in range(rows):
        row = s[i * columns: (i + 1) * columns]
        grid.append(row)
    
    # Transpose the grid to create the encrypted message
    encrypted_message = []
    for j in range(columns):
        column_text = ""
        for i in range(rows):
            if j < len(grid[i]):
                column_text += grid[i][j]
        encrypted_message.append(column_text)
    
    # Join the columns with spaces and return the result
    return " ".join(encrypted_message)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
