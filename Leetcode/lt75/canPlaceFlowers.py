from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        length = len(flowerbed)
        while i < length:
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == length - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1
        if count >= n:
            return True
        return False


sol = Solution()
# print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
# print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(sol.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2))


# i, j = 0, 0
# psb_places = 0
# while j <= len(flowerbed) - 1:
#     if flowerbed[i] == 0 and flowerbed[j] == 0 and flowerbed[j + 1] == 0:
#         psb_places += 1
#         i += 2
#         j += 2
#     i += 1
#     j += 1
# if psb_places >= n:
#     return True
# return False

# fInd = 0
# while fInd <= len(flowerbed):
#     if flowerbed[fInd] == 1:
#         break
#     else:
#         fInd += 1
# avail_slots = 0
# while fInd <= len(flowerbed) and fInd + 2 <= len(flowerbed):
#     if avail_slots >= n:
#         return True
#     if flowerbed[fInd + 2] == 0 and flowerbed[fInd+1] != 1:
#         avail_slots += 1
#     fInd += 2
# return False
#


# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         cnt,prev=0,0
#
#         for x in flowerbed:
#             if x==1:
#                 if prev==1:
#                     cnt-=1
#                 prev=1
#             else:
#                 if prev==1:
#                     prev=0
#                 else:
#                     cnt+=1
#                     prev=1
#         return cnt>=n
