class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_multiplication = 1
        zero_counter = 0
        for num in nums:
            if num != 0:
                full_multiplication *= num
            else:
                zero_counter += 1
        
        for i, n in enumerate(nums):
            if (n == 0) and (zero_counter == 1):
                nums[i] = full_multiplication
            elif zero_counter > 0:
                nums[i] = 0
            else:
                nums[i] = full_multiplication // n

            
        return nums
