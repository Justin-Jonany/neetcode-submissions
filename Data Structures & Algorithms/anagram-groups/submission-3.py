class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in strs_dict:
                strs_dict[sorted_s] += [s]
            else:
                strs_dict[sorted_s] = [s]
        return list(strs_dict.values())
