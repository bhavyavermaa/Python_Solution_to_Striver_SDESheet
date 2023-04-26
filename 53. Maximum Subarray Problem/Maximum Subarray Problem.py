class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        val=nums[0]
        sum=0
        for ele in nums:
            sum+=ele
            val=max(val,sum)
            if sum<0:
                sum=0
        return val