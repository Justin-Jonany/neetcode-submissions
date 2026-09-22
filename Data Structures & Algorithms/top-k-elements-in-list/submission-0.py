from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solutions
        # 1. Counter? --> not sorted from largest
            # after counter, we get the value that's largest (O(n))
            # O(n^2) worst case
        # 2. Sorting --> O(nlogn)
        # 3. 
        frequencies = Counter(nums)
        def foo(s):
            return s['freq']
        frequencies_list = [{'val': key, 'freq': frequencies[key]} for key in frequencies]
        frequencies_list.sort(key=foo, reverse=True)
        return [c['val'] for c in frequencies_list[:k]]

            


        