class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return True

        max_jump = [i + nums[i] for i, num in enumerate(nums)]
        curr = 0
        while curr < len(nums): # condition change later
            i = curr + 1
            best_pos = curr # stay same spot
            curr_furthest = max_jump[curr]
            while i <= min(max_jump[curr], len(nums) - 1):
                if curr_furthest < max_jump[i]:
                    best_pos = i
                    curr_furthest = max_jump[i]
                i += 1
            if curr_furthest >= len(nums) - 1:
                return True
            elif best_pos == curr: # stuck, no move will make it move further
                return False
            curr = best_pos
        return False
        



        # we start with a preprocessing step where we create an array with the furthest index u can travel from if u are in that index. And then with a while loop we iterate from the current index and go up one by one until the current index + value in that idnex, and keep track of the max distance from the preprocessed array we created. And then take the step that allows u to travel the furthest. This works because whatever index the other location allows u to jump to, thsi step covers it. And if there are ties, take the one further down the array. And if it finds an index that's over the len(nums)- 1 it means that if it goes there it can finish immediately. 

        # runtime of this is O(n) and space is O(n) but i think i can make it O(1) but im gonna make an O(n) space version first. 
# [4 0 3 1 0 3 0]

# [4 0 5 4 0 8 0]

# [5 4 3 2 1 0]
# [5 5 5 5 5 5]