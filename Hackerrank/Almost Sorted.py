def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
def almostSorted(arr, n):
    # Write your code here
    sorted_arr = quicksort(arr)

    if arr == sorted_arr:
        print('yes')
        return

    l, r = -1, -1    
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            l = i
            break

    for i in range(n-1, -1, -1):
        if arr[i] != sorted_arr[i]:
            r = i
            break
    
    arr[l], arr[r] = arr[r], arr[l]


    if arr == sorted_arr:
        print("yes")
        print("swap" , l+1, r+1)
        return
    

    arr[l], arr[r] = arr[r], arr[l]
    
    reversed_subarray = arr[l:r+1][::-1]
    temp_arr = arr[:1] +reversed_subarray

    if temp_arr == sorted_arr:
        print("yes")
        print("reverse", l+1, r+1)
        return
    
    print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr, n)
 