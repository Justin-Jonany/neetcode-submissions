class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_consecutive = 1
        curr_consecutive = 1
        if len(nums) == 0:
            return 0
        prev = nums[0]
        for num in nums[1:]:
            if prev == num - 1:
                curr_consecutive += 1
            elif prev != num:
                curr_consecutive = 1
            max_consecutive = max(curr_consecutive, max_consecutive)
            prev = num
        return max_consecutive
