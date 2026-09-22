class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums_dict.get(target - nums[i]) is not None:
                ans = [nums_dict.get(target - nums[i]), i]
                break
            nums_dict[nums[i]] = i
        return ans