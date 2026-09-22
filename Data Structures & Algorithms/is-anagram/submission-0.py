from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s) # O(n)
        t_counter = Counter(t) # O(m)

        if s_counter == t_counter: ## O(min(l, k)) where l is the number of elements in s and k is the number of elements in t
            return True
        else:
            return False