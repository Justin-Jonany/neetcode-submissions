class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums = sorted(nums)
        def dfs(nums_index: int, subset: list[int], curr_target:int, t=""):
            # print(f'{t}results: {results} subset: {subset} curr_target: {curr_target} curr_nums: {nums[nums_index:]}')
            # if len(nums) - nums_index == 0:
            #     return
            if curr_target == 0:
                # print(f'{t}HIT')
                results.append(subset.copy())
                # numbers to the right are larger than current num.
                return
            elif curr_target < 0: # no point on continuing
                return
            elif nums_index > len(nums) - 1: # no more numbers to add
                return
            else: # still haven't reached target yet
                while nums_index < len(nums) and curr_target - nums[nums_index] >= 0:
                    subset.append(nums[nums_index])
                    # print(f'{t}checking subset: {subset} target: {curr_target - nums[nums_index]}')
                    dfs(nums_index, subset, curr_target - nums[nums_index], t + "\t")
                    subset.pop()
                    nums_index += 1
                # print(f'{t}backtracked: curr_nums: {nums[nums_index:]} subset: {subset} target: {curr_target}')

        dfs(0, [], target)
        return results

# [1, 2, 3] target = 3
# results = [1, 1, 1]
# curr_target = 0
# curr_nums = [1, 2, 3]
# subset = [1, 2]
# target = []
            


# key thing is:
# 1. we can use each number multiple times
# 2. list is not sorted
#     - sorting it may matter (and likely the true algo will be more complex so this is not an overhead) because if sum is already over the target for the number we are currently looking at, then we dont need to check anything the right of it

# algo:
# 1. sort it first
# 2. have a current subset and a current subset sum
# 3. recursion that carries the subset and current subset
#     - add numbers one by one to subset and update the sum as well.
#     - or maybe divide target by current num to see how much we can fit in (maybe cause issue with backtracking)
#     - if we can't get target, we remove item and see if we can add the next item, if we can then recurse on that, otherwise backtrack and check again.
#     - anytiem subset sum hits target then add to results
# runtime: O(n * target/min(nums)) because we will add items to list target/min(nums) time for the smallest number at most, and then say we do that for everything, then that's n times that. thsi is based on if i add numbers one by one. space is O(target/min(nums)) since it's bounded by the target, and we can make a subset the longest if we buidl it with the min. 