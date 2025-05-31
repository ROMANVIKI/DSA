import numpy as np


myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def arrayRotate(matrix):
    print("------------")

    print("------------")

    print(myArray)
    print("------------")

    print("------------")
    n = len(myArray)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(
                f"first loop with index {i}{j}, with value {matrix[i][j]}{matrix[j][i]}"
            )
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
    return matrix


print(arrayRotate(myArray))
