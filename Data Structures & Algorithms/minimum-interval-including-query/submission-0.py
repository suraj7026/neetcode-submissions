class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        
        minHeap = []
        hashmap={}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minHeap,(r-l+1,r))
                i+= 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            if minHeap:
                hashmap[q] = minHeap[0][0]
            else:
                hashmap[q] = -1
            
        return [hashmap[q] for q in queries]

        