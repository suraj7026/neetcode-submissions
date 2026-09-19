class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = curmax = curmin = nums[0]
        for i in nums[1:]:
            candidates = (i,curmax*i,curmin*i)
            curmax = max(candidates)
            curmin = min(candidates)
            prod = max(prod,curmax)
        return prod