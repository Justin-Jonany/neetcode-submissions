import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums) # O(n)
        longest_sequence = 1
        curr_sequence = 1
        last_num = heapq.heappop(nums)
        while nums: # n times so O(nlogn)
            curr_num = heapq.heappop(nums) # O(logn)
            if curr_num == last_num+1:
                curr_sequence += 1
                longest_sequence = max(curr_sequence, longest_sequence)
            elif curr_num > last_num + 1: # not consecutive
                curr_sequence = 1 # reset
            last_num = curr_num
            # elif curr_num == last_num: # nothing happens
        return longest_sequence
            



# [1, 2, 3, 4]

# [5, 2, 1, 3, 4]