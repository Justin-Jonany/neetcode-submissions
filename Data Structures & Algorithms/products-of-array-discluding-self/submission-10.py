class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. with division
        # total_without_zero = 1
        # zero_counter = 0
        # for num in nums:
        #     if num == 0:
        #         zero_counter += 1
        #     else:
        #         total_without_zero *= num

        # if zero_counter > 1:
        #     return [0] * len(nums)
        # elif zero_counter == 1:
        #     return [0 if num != 0 else total_without_zero for num in nums]
        # else:
        #     return [(total_without_zero // num) for num in nums]

        # 2. no division
        prefixes = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1]
        
        suffixes = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]

        result = [prefix * suffix for prefix, suffix in zip(prefixes, suffixes)]
        return result

# [1 1 6 1]
# [3 2 4 5]

# [1       , 3    , 2 * 3, 2 3 * 2 * 4]
# [2 * 4 *5, 4 * 5, 5    , 1 ]

# [8 12 6]


# what can we store
# [1 8 16 64 ]

