class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums) # O(n)
        max_cons = 0
        curr_cons = 0
        for num in nums: # O(n)
            if num - 1 not in hashset:
                while num in hashset: # O(1)
                    curr_cons += 1
                    max_cons = max(max_cons, curr_cons)
                    num += 1
                curr_cons = 0
        return max_cons
