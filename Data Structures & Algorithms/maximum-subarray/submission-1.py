class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            curSum += num
            maxSub = max(curSum, maxSub)
            if curSum < 0:
                curSum = 0
        return maxSub
