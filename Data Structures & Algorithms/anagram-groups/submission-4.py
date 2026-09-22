class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs: # let n be number of words this is O(n) because each operation is O(1)
            sorted_s = ''.join(sorted(s)) # O(1) because s is max 10 000
            if sorted_s in strs_dict:
                strs_dict[sorted_s] += [s]
            else:
                strs_dict[sorted_s] = [s]
        return list(strs_dict.values()) # O(n)
