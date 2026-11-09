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
            # print(f'{counter} left, right: {(left, right)} quota: {quota} current: {s[left: right]}')
            counter[s[right]] += 1
            focus = max(counter, key=counter.get) # most occurence
            # print(focus)
            right += 1
            non_focus = (right-left) - counter[focus]
            # print(f'(right-left) - counter[focus]: ({right-left}) - {counter[focus]}')
            quota = k - non_focus
            if quota < 0:
                # we have to trim our window
                counter[s[left]] -= 1
                left += 1

            
            max_l = max(max_l, (right - left))
            # print(f'{counter}  focus: {focus} left, right: {(left, right)} quota: {quota} current: {s[left: right]} max_l: {max_l}')
            # print()
        return max_l

# s="ABCCABAEA"
# k=2


