class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_arr = []
        for i in operations:
            if i == '+':
                final_arr.append(int(final_arr[-2]) + int(final_arr[-1]))
            elif i == 'D':
                final_arr.append(int(final_arr[-1]) * 2)
            elif i == 'C':
                final_arr.pop()
            else:
                final_arr.append(int(i))
        return sum(final_arr)
