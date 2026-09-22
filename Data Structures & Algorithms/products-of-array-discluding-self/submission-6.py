class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        # [2, 4, 3, 5]

        # prefix: [1, 2, 8, 24]
        # suffix: [1, 5, 15, 60]
        # solutionL [60, 30, 40, 24]

        # full_multiplication = 1
        # zero_counter = 0
        # for num in nums: # O(n)
        #     if num != 0:
        #         full_multiplication *= num
        #     else:
        #         zero_counter += 1
        
        # for i, n in enumerate(nums): # O(n)
        #     if (n == 0) and (zero_counter == 1):
        #         nums[i] = full_multiplication
        #     elif zero_counter > 0:
        #         nums[i] = 0
        #     else:
        #         nums[i] = full_multiplication // n

            
        # return nums
