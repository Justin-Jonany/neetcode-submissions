class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dict = {}
        results = []

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1

        for i in range(len(nums)): # O(n^2)
            # print(f'{nums[i]}:')
            for j in range(i+1, len(nums)): # O(n)
                need = 0 - nums[i] - nums[j]
                # print(f'\t{nums[j]}: {nums_dict} need {need}')
                if need not in nums_dict: # O(1)
                    continue
                else:
                    if (nums[i] == nums[j]) and (nums[i] == need):
                        if nums_dict[need] >= 3:
                            results.append(tuple(sorted([nums[i], nums[j], need])))
                    elif (nums[i] == need) or (nums[j] == need):
                        if nums_dict[need] >= 2:
                            print('enter')
                            results.append(tuple(sorted([nums[i], nums[j], need])))
                    else:
                        if nums_dict[need] >= 1:
                            results.append(tuple(sorted([nums[i], nums[j], need])))
        # print(results)
        return list(set(results))


