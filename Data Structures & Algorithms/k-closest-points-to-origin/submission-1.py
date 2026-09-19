from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = 0
        ans = []
        def getDistance(x,y):
            return sqrt((x**2) + (y**2))
        
        heap = [(getDistance(x,y),[x,y]) for x,y in points]
        heapq.heapify(heap)
        
        for i in range(k):
            _,res = heapq.heappop(heap)
            ans.append(res)
        return ans