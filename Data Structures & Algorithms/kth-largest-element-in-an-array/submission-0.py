class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [-i for i in nums]
        heapq.heapify(num)

        for i in range(k):
            res = heapq.heappop(num)
        return -res