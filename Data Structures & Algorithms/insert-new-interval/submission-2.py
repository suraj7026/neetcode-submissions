class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        # print(intervals)

        result.append(intervals[0])

        for start,end in intervals[1:]:
            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start,end])

        return result