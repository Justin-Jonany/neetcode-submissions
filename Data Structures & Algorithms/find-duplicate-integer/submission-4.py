class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        # 1. set O(n) and O(n) space
        # 2. 

# [1 2 1 3]
# [1 5 2 3 4 5]


# 1, 3, 4, 2, 2
# 1  3 2 4 2 4 2


# [1,4,3,2,2]
# slow: 1 4 2 3 2 3
# fast 1 2 2 2 2 2

# # [2,3,2,1]
# 2 2 2 2 2 