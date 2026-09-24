class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        ordered = sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)[:k]
        return [val for val, count in ordered]