from collections import defaultdict
import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left = 0
        right = 0
        quota = k
        max_l = 0

        right = 0
        while right < len(s):
            counter[s[right]] += 1
            focus = max(counter, key=counter.get) # most occurence O(1) because capped at counter having 26 characters
            right += 1
            non_focus = (right-left) - counter[focus]
            quota = k - non_focus
            if quota < 0:
                # we have to trim our window
                counter[s[left]] -= 1
                left += 1

            
            max_l = max(max_l, (right - left))

        return max_l

# s="ABCCABAEA"
# k=2


