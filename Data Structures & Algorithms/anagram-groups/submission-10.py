class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs: # O(nk)  and space is O(nk)
            identity = [0] * 26
            for c in s: #O(k)
                identity[ord(c) - ord('a')] += 1
            key = tuple(identity)
            if key in strs_dict:
                strs_dict[key].append(s)
            else:
                strs_dict[key] = [s]
        return list(strs_dict.values()) # O(n)
        # strs_dict = {}
        # for s in strs: # O(nklogk)  and space is O(nk)
        #     sorted_s = ''.join(sorted(s)) # O(klogk)
        #     if sorted_s in strs_dict:
        #         strs_dict[sorted_s].append(s)
        #     else:
        #         strs_dict[sorted_s] = [s]
        # return list(strs_dict.values()) # O(n)
