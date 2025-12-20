class Solution:
    def minTimeToVisitAllPoints(self, points):
        res = 0
        ex = []
        for i in range(1, len(points)):
            res += max(
                abs(points[i][0] - points[i - 1][0]),
                abs(points[i][1] - points[i - 1][1]),
            )
            ex.append(res)
        return res, ex


sol = Solution()
print(sol.minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))
