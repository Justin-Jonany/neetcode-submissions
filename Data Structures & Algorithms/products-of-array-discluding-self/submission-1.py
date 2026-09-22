class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        suffixes = [1]
        for num in nums[:-1]:
            prefixes.append(num * prefixes[-1])
        for num in reversed(nums[1:]):
            suffixes.append(num * suffixes[-1])

        sums = [(pref * suffix) for pref, suffix in zip(prefixes , reversed(suffixes))]
        return sums
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
