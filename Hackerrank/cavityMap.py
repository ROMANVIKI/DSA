#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#
# 4
# 1112
# 1912
# 1892
# 1234




def cavityMap(grid):
    n = len(grid)
    result = grid.copy()

    for i in range(1, n - 1):
        row = list(grid[i])
        for j in range(1, n - 1):
            current = grid[i][j]
            # Check if it's greater than all 4 neighbors
            if (
                current > grid[i - 1][j] and
                current > grid[i + 1][j] and
                current > grid[i][j - 1] and
                current > grid[i][j + 1]
            ):
                row[j] = 'X'
        result[i] = ''.join(row)

    return result



if __name__ "__main__":

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print(result)
