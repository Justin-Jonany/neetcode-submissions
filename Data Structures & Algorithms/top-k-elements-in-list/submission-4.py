class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        freq = [[] for i in range(len(nums) + 1)]
        for val, count in nums_dict.items():
            freq[count].append(val)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            res.extend(freq[i])
            if len(res) >= k:
                break
        return res[:k]

        # counter = [0] * 2001 # -1000 to 1000 includes 0
        # for num in nums:
        #     counter[1000+num] += 1
        # indexed_counter = sorted(
        #     [(i - 1000, counter[i]) for i in range(2001)], 
        #     key=lambda item: item[1], 
        #     reverse=True
        # ) # O(1) because 2000 elements max
        # return [i[0] for i in indexed_counter[:k]]
        
        # counter = [0] * 2001 # -1000 to 1000 includes 0
        # for num in nums:
        #     counter[1000+num] += 1
        # indexed_counter = sorted(
        #     [(i - 1000, counter[i]) for i in range(2001)], 
        #     key=lambda item: item[1], 
        #     reverse=True
        # ) # O(1) because 2000 elements max
        # return [i[0] for i in indexed_counter[:k]]



        # 1 1 3 8 8 8 8
        # [0, ...., 2, 0, 1, 0,0 0, 0, 0, 4, 0 ,...]

        # nums_dict = {}
        # for num in nums:
        #     if num in nums_dict:
        #         nums_dict[num] += 1
        #     else:
        #         nums_dict[num] = 1
        # ordered = sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)[:k] #O(nlogn)
        # return [val for val, count in ordered]