class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums =nums[0]
        run =0
        for num in nums:
            run = max(num,run+num)
            sums = max(run,sums)
        return sums