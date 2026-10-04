class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # nums_dict = {}
        # results = []

        # for i in range(len(nums)):
        #     if nums[i] in nums_dict:
        #         nums_dict[nums[i]] += 1
        #     else:
        #         nums_dict[nums[i]] = 1

        # left = 0
        # right = len(nums) - 1




        # return [[]]

        nums.sort() # need sort for duplicate checking
        nums_dict = defaultdict(int)
        results = []

        for num in nums:
            nums_dict[num] += 1

        for i in range(len(nums)): # O(n^2)
            nums_dict[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, len(nums)): # O(n)
                nums_dict[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if nums_dict[target] > 0:
                    results.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                nums_dict[nums[j]] += 1
        # print(results)
        return results


