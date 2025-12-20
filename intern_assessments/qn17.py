def maxSubSum(arr):
    res = arr[0]
    for i in range(len(arr)):
        curr = 0
        for j in range(i, len(arr)):
            curr = curr + arr[j]
            res = max(res, curr)
    return res


sol = maxSubSum(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(sol)
