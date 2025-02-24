class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        el_dict = set()
        for num in nums:
            if num in el_dict:
                return True
            else:
                el_dict.add(num)
        return False
