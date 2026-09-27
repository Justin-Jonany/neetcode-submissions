import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starters = set()
        for num in nums: #O(n)
            if num - 1 not in nums_set:
                starters.add(num)

        max_sequence = 0
        print(starters)
        for starter in starters: # at worst n iteration
            curr_sequence = 1
            while True: # in total this will loop n + num_starters times. because for one starter it will check keep looping as long as the next number exist and then it will check a number that doesnt exist once before stopping. So it's gonna cehck all the number plus num_starter number of extra starters.
                starter += 1
                if starter in nums_set: # O(1)
                    curr_sequence += 1
                else:
                    max_sequence = max(max_sequence, curr_sequence)
                    break

        return max_sequence
        # []
        # [1]
        # [1 1 1 2 2 3]


        # with heap but i could have just sorted it and then iterate. much simpler
        # if len(nums) == 0:
        #     return 0
        # heapq.heapify(nums) # O(n)
        # longest_sequence = 1
        # curr_sequence = 1
        # last_num = heapq.heappop(nums)
        # while nums: # n times so O(nlogn)
        #     curr_num = heapq.heappop(nums) # O(logn)
        #     if curr_num == last_num+1:
        #         curr_sequence += 1
        #         longest_sequence = max(curr_sequence, longest_sequence)
        #     elif curr_num > last_num + 1: # not consecutive
        #         curr_sequence = 1 # reset
        #     last_num = curr_num
        #     # elif curr_num == last_num: # nothing happens
        # return longest_sequence
            



# [1, 2, 3, 4]

# [1, 2, 3, 4, 6, 7]


1 
6
