class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        used = [False] * len(nums)
        def dfs(path: list[int]):
            if len(path) == len(nums):
                results.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path)
                used[i] = False
                path.pop()
        
        dfs([])

        return results


# ok so instead of using nums_index, i just iterate through every num in nums. and the stopping condition that adds to results is when len of path is same as nums. rest stays the same

# now gonna test it on a smaller sample
# [1, 2]
# results = []
# path = [1, 1]
# dfs([]), dfs([1]), 

# wait no we still need something to keep track because otheerwise we would be adding the same thing. 
# - list? look and path checks would be O(n)... so from O(n^n) to O(n^{n+1})
# - set? can't permute it. so we would need to create a new copy each time so basically same like list
# let's do list




# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         results = []

#         def dfs(nums_index:int, path: list[int]):
#             if nums_index == len(nums):
#                 results.append(path.copy())

#             for i in range(nums_index, len(nums)):
#                 path.append(nums[i])
#                 dfs(nums_index + 1, path)
#                 path.pop()
        
#         dfs(0, [])

#         return results

# # [1, 2, 3]
# # [2, 3]
# # results = [[1, 2, 3]]
# # nums_index = 2
# # path = [2, 3]
# # dfs(0, []), dfs(1, [1, ]), dfs(2, [1, 2]), dfs(3, [1, 2, 3]), dfs(2, [2,]), dfs(3, [2,3])

# # will add to path when nums_index is 3
# # ah i see my mistake, I moved the num index and that instead disallows 2 3 1. 3 2 1. (just for the sake of this practice for claude because im not doign audio transript im gonna comment this out, and create new solution)

# # after
# # and we are gonna copy the array to results n! times, so run time is O(n^n + n.n!) NOT O(n^{n+1})


# # Notes before working
# # - permutation: order matters. (1,2,3), (3,2,1) is different
# # solution:
# # 1. backtracking
# # 2. dfs that keeps track of path and nums available
#     # - in each recursion step, it iterates the possible nums left and then call dfs again on the remaining number. everytime no more nums left, we add to results list
#     # - after we finish a recursion step, pop the number we just explroed
# # runtime: let n be the length of nums. so the depth is n because we only create arrays that use one of nums. and branching is n as well. so run time is O(n^n). and we are gonna copy the array to results, so run time is O(n^{n+1}). space is O(n) because that's the path. but if we consider the output, that's n! space. 