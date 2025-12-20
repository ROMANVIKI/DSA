def minimumDistances(a):
    same_num_indices = []
    # Write your code here
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                pass
            else:
                if a[i] == a[j]:
                    min_value = i - j
                    if min_value > 0:

                        same_num_indices.append(min_value)
    if not same_num_indices:
        min_dist = -1
    else:
        min_dist = min(same_num_indices)
    return min_dist
    # return same_num_indices


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
