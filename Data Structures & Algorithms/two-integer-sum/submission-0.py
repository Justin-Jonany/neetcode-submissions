from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, num in enumerate(nums):
            needed_pair = target - num
            pair = nums_dict.get(needed_pair) # this is O(1) on average
            if pair is not None:
                return [pair, index]
            nums_dict[num] = index
        # so in total O(n)
                