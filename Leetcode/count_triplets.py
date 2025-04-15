from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1

        return count


sol = Solution()

print(sol.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))


def count_good_triplets_optimized(arr: List[int], a: int, b: int, c: int) -> int:
    count = 0
    n = len(arr)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if abs(arr[i] - arr[j]) > a:
                continue
            for k in range(j + 1, n):
                # Now only check b and c
                if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
    return count
