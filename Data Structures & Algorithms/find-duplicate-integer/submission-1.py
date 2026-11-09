class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        for key in counter:
            if counter[key] > 1:
                return key
        # 1. set O(n) and O(n) space
        # 2. 

# [1 2 1 3]
# [1 5 2 3 4 5]