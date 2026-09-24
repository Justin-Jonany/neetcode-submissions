class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. with division
        total = 1
        total_without_zero = 1
        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1
            else:
                total_without_zero *= num
            total *= num

        if zero_counter > 1:
            return [0] * len(nums)
        elif zero_counter == 1:
            return [0 if num != 0 else total_without_zero for num in nums]
        else:
            return [(total // num) for num in nums]

