# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a_distance = x - z
    cat_b_distance = y - z
    if cat_a_distance < 0:
        cat_a_distance = cat_a_distance * -1
    if cat_b_distance < 0:
        cat_b_distance = cat_b_distance * -1
    if cat_a_distance == cat_b_distance:
        return 'Mouse C'
    elif cat_a_distance < cat_b_distance :
        return 'Cat A'
    else:
        return 'Cat B'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
