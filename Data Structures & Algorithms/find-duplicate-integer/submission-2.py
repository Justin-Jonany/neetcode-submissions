class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
        # 1. set O(n) and O(n) space
        # 2. 

# [1 2 1 3]
# [1 5 2 3 4 5]