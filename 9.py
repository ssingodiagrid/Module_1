# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 1. Sort intervals by start time
        intervals.sort()

        ans = []
        curr = intervals[0]

        for i in range(1, len(intervals)):
            if curr[1] >= intervals[i][0]:
                # Overlap → merge
                curr[1] = max(curr[1], intervals[i][1])
            else:
                # No overlap → store current and move ahead
                ans.append(curr)
                curr = intervals[i]

        # Add the last interval
        ans.append(curr)

        return ans