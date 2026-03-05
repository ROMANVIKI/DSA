def bigSorting(unsorted):
    # Write your code here
    ret_list = sorted(unsorted)
    i = 0
    while i <= len(ret_list) - 1:
        print(ret_list[i])
        i += 1


if __name__ == "__main__":
    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = int(input())
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    print(result)
