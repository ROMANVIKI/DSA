def isArraySortedOrder(a):
    if len(a) == 1:
        return True
    return a[0] <= a[1] and isArraySortedOrder(a[1:])

A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
print(isArraySortedOrder(A))


