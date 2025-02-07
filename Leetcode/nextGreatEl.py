class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        final_arr = [next_greater[num] for num in nums1]
        return final_arr


sol = Solution()
print(sol.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
