from re import S
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result_arr = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        num1_lst = []
        num2_lst = []
        for char1 in nums1:
            if char1 not in nums2:
                num1_lst.append(char1)

        for char2 in nums2:
            if char2 not in nums1:
                num2_lst.append(char2)
        result_arr.append(num1_lst)
        result_arr.append(num2_lst)
        return result_arr


s = Solution()
print(s.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(s.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
