class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            last_merged_end = merged[-1][1]
            if interval[0] <= last_merged_end:
                merged[-1][1] = max(last_merged_end, interval[1])
            else:
                merged.append(interval)

        return merged


sol = Solution()

sol1 = sol.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
print(sol1)
