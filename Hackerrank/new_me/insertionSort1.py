def insertionSort1(n, arr):
    # Write your code here
    len_arr = len(arr) - 1
    while len_arr >= 0:
        if arr[len_arr] > arr[-1]:
            arr[len_arr - 1] = arr[len_arr]
            len_arr -= 1
        else:
            break
        print(arr)


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
