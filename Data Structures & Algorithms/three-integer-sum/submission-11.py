class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i, num in enumerate(nums):
            print(num)
            if num > 0:
                break 
            if i > 0 and num == nums[i - 1]: # skips the same instance to prevent dupes
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]+ nums[i]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[right], nums[left]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # temp = right
                    # while temp > left and nums[temp] == nums[right]:
                    #     results += [nums[i], nums[right], nums[left]]
                    #     temp -= 1

        return results
        #     if nums[i] in nums_dict:
        #         nums_dict[nums[i]] += 1
        #     else:
        #         nums_dict[nums[i]] = 1

        # left = 0
        # right = len(nums) - 1

# [-4, -1, -1,0,1,2, 2]


        # return [[]]

        # nums.sort() # need sort for duplicate checking
        # nums_dict = defaultdict(int)
        # results = []

        # for num in nums:
        #     nums_dict[num] += 1

        # for i in range(len(nums)): # O(n^2)
        #     nums_dict[nums[i]] -= 1
        #     if i and nums[i] == nums[i - 1]: # we skip if it's the same to prevent duplicate entries. and also cus we are practically doing the same thing as the previous iteration
        #         continue # it's sroted so checkign with previous works
        #     for j in range(i+1, len(nums)): # O(n)
        #         nums_dict[nums[j]] -= 1
        #         if j - 1 > i and nums[j] == nums[j - 1]: # same reasoning like before but for second digit
        #             continue
        #         target = -(nums[i] + nums[j])
        #         if nums_dict[target] > 0:
        #             results.append([nums[i], nums[j], target])

        #     for j in range(i + 1, len(nums)): # reset
        #         nums_dict[nums[j]] += 1
        # # print(results)
        # return results


