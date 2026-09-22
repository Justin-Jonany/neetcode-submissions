from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]
        num_counter = Counter(nums)
        for i, num in enumerate(num_counter):
            buckets[num_counter[num]].append(num)

        res = []
        for group in reversed(buckets):
            needed = k - len(res)
            res += group[:needed]
        return res
            
            


        