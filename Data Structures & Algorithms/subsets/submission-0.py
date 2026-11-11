class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursion hlper with param nums and combination so far and a combiantions list outside
        # in each recursion we add an item to the combination so far and then add that new combination to combinations and call subsets again
        # after each iteration it deletes what it added

        combinations = [[]]
        def helper(nums: list[int], path: list[int]):
            if len(nums) == 0:
                return
            print(f'nums: {nums}  path: {path}')
            for i in range(len(nums)):
                path.append(nums[i])
                combinations.append(path.copy())
                helper(nums[i+1:], path)
                path.pop()
        helper(nums, [])
        return combinations



# [1 2]