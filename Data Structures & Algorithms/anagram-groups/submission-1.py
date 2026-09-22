class Solution:
    ALPHABET_START_ORD: int = 97
    def hash(self, string: str) -> tuple[int]:
        identity = [0] * (26) # O(1)
        for c in string:
            index = ord(c) - self.ALPHABET_START_ORD
            identity[index] += 1
        return tuple(identity)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}
        for s in strs: # O(m)
            identity = self.hash(s) # O(n)
            if identity not in strs_map:
                strs_map[identity] = []
            strs_map[identity].append(s)
        return list(strs_map.values() )