def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    num_layers = min(m, n) // 2

    for layer in range(num_layers):
        # Calculate the number of elements in this layer
        elements_in_layer = 2 * (m + n - 4*layer) - 4

        # Flatten the layer into a 1D list
        layer_values = []
        for i in range(layer, m - layer):
            layer_values.append(matrix[i][layer])
        for i in range(layer + 1, n - layer - 1):
            layer_values.append(matrix[m - layer - 1][i])
        for i in range(m - layer - 1, layer - 1, -1):
            layer_values.append(matrix[i][n - layer - 1])
        for i in range(n - layer - 2, layer, -1):
            layer_values.append(matrix[layer][i])

        # Calculate the effective rotation
        effective_rotation = r % elements_in_layer

        # Rotate the 1D list anti-clockwise
        layer_values = layer_values[effective_rotation:] + layer_values[:effective_rotation]

        # Fill the layer with the rotated values
        index = 0
        for i in range(layer, m - layer):
            matrix[i][layer] = layer_values[index]
            index += 1
        for i in range(layer + 1, n - layer - 1):
            matrix[m - layer - 1][i] = layer_values[index]
            index += 1
        for i in range(m - layer - 1, layer - 1, -1):
            matrix[i][n - layer - 1] = layer_values[index]
            index += 1
        for i in range(n - layer - 2, layer, -1):
            matrix[layer][i] = layer_values[index]
            index += 1

    # Print the rotated matrix
    for row in matrix:
        print(" ".join(map(str, row)))




if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)





